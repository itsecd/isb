import argparse

from src.encryption.decryptors.decryptor_replace_one_letter import DecryptorReplaceOneLetter as DCrypt

CONST_LETTERS_MAX_IN_ENCODE = 20

def generate_command(parser: argparse.ArgumentParser) -> None:
    """
    Generate command line arguments for decryption of a cipher text.

    Creates command line arguments for decrypting a cipher text using the 
    following options:
    - Specify the alphabet for decryption either directly or from a file.
    - Provide the path to the cipher file to be decrypted.
    - Set the output file name for the decrypted text (existing file will be 
    overwritten).
    - Define the character delimiter in the cipher text.
    - Optionally export the decryption key to a JSON file.

    Parameters:
        parser (argparse.ArgumentParser): ArgumentParser object to add
        arguments to.

    Command line arguments:
        -a, --alphabet (str): Alphabet for decryption
        -fta, --file_for_txt_alphabet (str): Path to the file with alphabet for 
        decryption (.txt)
        -x, --encodeFile (str): Path to the cipher file
        -o, --file_for_export (str): Output file name (will overwrite existing)
        -dc, --character_delimetr_in_cihep (str): Character delimiter in the
        cipher
        -e, --export_key_json (str): Export key to file

    Returns:
        None
    """
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--alphabet', type=str, 
                       help='Alphabet for decryption')
    group.add_argument('-fta', '--file_for_txt_alphabet', type=str, 
                       help='Path to the file with alphabet for decryption .txt')

    parser.add_argument('-x', '--encodeFile', type=str, 
                        help='Path to the cipher file')
    parser.add_argument('-o', '--file_for_export', type=str, 
                        help='Output file name (will overwrite existing)')
    parser.add_argument('-dc', '--character_delimetr_in_cihep', type=str, 
                        help='Character delimiter in the cipher')
    parser.add_argument('-e', '--export_key_json', type=str, 
                        help="Export key to file")


def out_basic_info(decryptor: DCrypt, text: str, 
                   for_watch: dict, translate: str) -> None:
    """
    Output basic information about the decryption process.

    Display the following information:
    - Frequency analysis of the decrypted text.
    - Replacements made during decryption.
    - The original encrypted text.
    - The decrypted text.

    Parameters:
        decryptor (DCrypt): DCrypt object used for decryption.
        text (str): The original encrypted text.
        for_watch (dict): Dictionary of replacements made during 
        decryption.
        translate (str): The decrypted text.

    Returns:
        None
    """
    
    print("\n---------------------------------------------------------------")
    print("Frequency:\n")
    print(decryptor.analysis_text_and_sort_frequency())

    print("-----------------------------------------------------------------")
    print("\n\nReplacements:")
    print()
    print(list(for_watch.keys()))
    print(list(for_watch.values()))
    print(for_watch)

    print("-----------------------------------------------------------------")
    print("\n\nText:")
    print(text)

    print("-----------------------------------------------------------------")
    print("\n\nDecryption:")
    print(translate)
    

def out_plus_info(decryptor: DCrypt, translate: str, 
                  for_watch: dict, symbol: str):
    """
    Output additional information about the decryption process.

    Display the analysis of word sizes and frequencies for a specific symbol.

    Parameters:
        decryptor (DCrypt): DCrypt object used for decryption.
        translate (str): The decrypted text.
        for_watch (dict): Dictionary of replacements made during decryption.
        symbol (str): The symbol to analyze.

    Returns:
        None
    """

    print("---------------------------------------------------------------")
    print("\nAnalysis: (number of characters, number of words, frequency of all words)")

    for i in range(1, CONST_LETTERS_MAX_IN_ENCODE):

        length = decryptor.count_word_size_in_text([symbol], i)

        if length != 0:

            average = decryptor.word_size_in_text_frequency([symbol], i)
            print(f"\n{i}, {length}, {average}")
            print(decryptor.split_text_by_size([symbol], i))
            print(DCrypt.split_text_by_size_s(translate, [for_watch[symbol]], i))


def main(standart_out_in_file = "translate.out"):
    """
    Main function for decrypting text encrypted with a simple replacement using the alphabet.
    """
    parser = argparse.ArgumentParser(description='Program for decrypting with Enigma using a key')

    generate_command(parser)

    args = parser.parse_args()

    if args.alphabet:
        good_alphabet = args.alphabet
    elif args.file_for_txt_alphabet:
        with open(args.file_for_txt_alphabet, "r") as f:
            good_alphabet = f.read()

    with open(args.encodeFile, 'r') as file:
        text = file.read()
    text = text.replace("\n", "")

    decryptor = DCrypt(text)

    for_watch = decryptor.get_translate_dict_frequency(good_alphabet)
    translate = decryptor.decryption_sort_frequency(good_alphabet)

    out_basic_info(decryptor, text, for_watch, translate)

    if args.character_delimetr_in_cihep \
       and len(args.character_delimetr_in_cihep) == 1:
       out_plus_info(decryptor, translate, for_watch, args.character_delimetr_in_cihep)

    if args.export_key_json:
        decryptor.export_key_json(good_alphabet, args.export_key_json)


    if args.file_for_export:
        with open(args.file_for_export, 'w') as file:
            file.write(translate)
    else:
        with open(standart_out_in_file, 'w') as file:
            file.write(translate)

if __name__ == "__main__":
    
    try:
        main()
    except Exception as e:
        print("Error:", e)