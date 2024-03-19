import argparse

from src.encryption.decryptors.decryptor_replace_one_letter import DecryptorReplaceOneLetter as DCrypt

CONST_LETTERS_MAX_IN_ENCODE = 20

def generate_command(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--alphabet', type=str, help='Alphabet for decryption')
    group.add_argument('-fta', '--fileForTxtAlphabet', type=str, help='Path to the file with alphabet for decryption .txt')

    parser.add_argument('-x', '--encodeFile', type=str, help='Path to the cipher file')
    parser.add_argument('-o', '--fileForExport', type=str, help='Output file name (will overwrite existing)')
    parser.add_argument('-dc', '--characterDelimetrInCihep', type=str, help='Character delimiter in the cipher')
    parser.add_argument('-e', '--exportKeyJson', type=str, help="Export key to file")

    return

def out_basic_info(decryptor: DCrypt, text: str, forWatch: dict, translate: str) -> None:
    
    print("\n-------------------------------------------------------------------------------")
    print("Frequency:\n")
    print(decryptor.analysis_text_and_sort_frequency())

    print("-------------------------------------------------------------------------------")
    print("\n\nReplacements:")
    print()
    print(list(forWatch.keys()))
    print(list(forWatch.values()))
    print(forWatch)

    print("-------------------------------------------------------------------------------")
    print("\n\nText:")
    print(text)

    print("-------------------------------------------------------------------------------")
    print("\n\nDecryption:")
    print(translate)

    return

def out_plus_info(decryptor: DCrypt, translate: str, forWatch: dict, sumbole: str):

    print("-------------------------------------------------------------------------------")
    print("\nAnalysis: (number of characters, number of words, frequency of all words)")
    
    for i in range(1, CONST_LETTERS_MAX_IN_ENCODE):
        
        length = decryptor.count_word_size_in_text([sumbole], i)
        
        if length != 0:
            
            average = decryptor.word_size_in_text_frequency([sumbole], i)
            print(f"\n{i}, {length}, {average}")
            print(decryptor.split_text_by_size([sumbole], i))
            print(DCrypt.split_text_by_size_s(translate, [forWatch[sumbole]], i))

def main():
    
    parser = argparse.ArgumentParser(description='Program for decrypting with Enigma using a key')

    generate_command(parser)

    args = parser.parse_args()

    if args.alphabet:
        goodAlphabet = args.alphabet
    elif args.fileForTxtAlphabet:
        with open(args.fileForTxtAlphabet, "r") as f:
            goodAlphabet = f.read()

    with open(args.encodeFile, 'r') as file:
        text = file.read()
    text = text.replace("\n", "")

    decryptor = DCrypt(text)

    forWatch = decryptor.get_translate_dict_frequency(goodAlphabet)
    translate = decryptor.decryption_sort_frequency(goodAlphabet)

    out_basic_info(decryptor, text, forWatch, translate)

    if args.characterDelimetrInCihep and len(args.characterDelimetrInCihep) == 1:
        out_plus_info(decryptor, translate, forWatch, args.characterDelimetrInCihep)

    if args.exportKeyJson:
        decryptor.export_key_json(goodAlphabet, args.exportKeyJson)

    with open(args.fileForExport, 'w') as file:
        file.write(translate)

if __name__ == "__main__":
    
    try:
        main()
    except Exception as e:
        print("Error:", e)