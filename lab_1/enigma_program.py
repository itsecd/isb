import argparse

from typing import Dict

import src.encryption.encryptors.enigma as eni

STANDART_SEED="x(ГkшЪ+4sЩJpШ)0,хRCЕD`ьQEрP2уйXыj.HЙGгЖж*фЭzhfgч№VFтцСtмнХ ЗТ}\
               KЛ%»-Y1ПУ{кMНв3!oZепД;ЦS7:iu#яcЮmO]dОАзъ@8бБqлР/о'«9ЧvAщynЬbЁ[\
               UаI~LewюКэaМд56B&TWФиЯЫё^ВNсrlИ="

def generate_command(parser: argparse.ArgumentParser):
    """
    Generate command line arguments using the provided ArgumentParser object.

    Parameters:
        - parser (argparse.ArgumentParser): The ArgumentParser object used to
        define and parse command line arguments.

    Command line arguments:
        -k, --key (str): Key for text (random set of characters)
        -pk, --pathKey (str): Path to the file for text
        -x, --file_to_text (str): Path to the text file
        -o, --file_for_export (str): Output file name (will overwrite existing)
        --translate (bool): Flag indicating if text should be 
        encrypted(default: False)
        -e, --export_key_txt (str): Export key to file

        Seed options (choose one):
            -s, --seed (str): Seed for key generation
            -sft, --seed_file_txt (str): Seed for key generation in a file

    Note:
        - Either -k/--key or -pk/--pathKey is required.
        - Either -s/--seed or -sft/--seed_file_txt is required.

    Returns:
        None
    """
    
    group_first = parser.add_mutually_exclusive_group(required=True)
    group_first.add_argument('-k', '--key', type=str, 
                       help='Key for text (random set of characters)')
    group_first.add_argument('-pk', '--pathKey', type=str, 
                       help='Path to the file for text')

    parser.add_argument('-x', '--file_to_text', type=str, 
                        help='Path to the text file')
    parser.add_argument('-o', '--file_for_export', type=str, 
                        help='Output file name (will overwrite existing)')
    parser.add_argument('--translate', type=bool, default=False, 
                        help='Encrypt text')
    parser.add_argument('-e', '--export_key_txt', type=str,
                        help="Export key to file")

    group_second = parser.add_mutually_exclusive_group(required=True)
    group_second.add_argument('-s', '--seed', type=str, 
                        help="Seed for key generation")
    group_second.add_argument('-sft', '--seed_file_txt', type=str, 
                        help="Seed for key generation in a file")

def get_args(parser: argparse.ArgumentParser, file_to_fail_export: str = "cihep.out") -> dict:
    """
    Parse the command line arguments using the provided parser and return a 
    dictionary with the parsed arguments.

    Parameters:
        - parser (argparse.ArgumentParser): The ArgumentParser object used to 
        parse the command line arguments.
        - file_to_fail_export (str): The default output file name if no export 
        file is specified.

    Returns:
        dict: A dictionary containing the parsed arguments:
            - text (str): The text read from the input file.
            - seed (str): The seed for key generation.
            - key (str): The key for text encryption.
            - translate (bool): Flag indicating if text should be encrypted.
            - export_key (str): The file path to export the key.
            - export_file (str): The output file name for encryption results.
    """
    
    args = parser.parse_args()
    
    with open(args.file_to_text, 'r') as f:
        text = f.read()
        
    if args.seed:
        seed = args.seed
    elif(args.seed_file_txt):
        with open(args.seed_file_txt, 'r') as f:
            seed = f.read()
    else:
        seed = STANDART_SEED

    if args.key:
        key = args.key
    elif args.pathKey:
        with open(args.pathKey, 'r') as f:
            key = f.read()
    
    export_cihep = parser.parse_args().file_for_export

    if not export_cihep:
        export_cihep = file_to_fail_export
    
    translate = parser.parse_args().translate
    export_key = parser.parse_args().export_key_txt
    
    return {"text": text, "seed": seed, "key": key, "translate" : translate, 
            "export_key": export_key, "export_file": export_cihep}


def main():
    """
    Main function for encrypting text with Enigma using a key.

    The function performs the following steps:
    1. Creates an ArgumentParser object with a description of the program.
    2. Generates command line arguments using the generate_command function.
    3. Parses the command line arguments and retrieves them as a dictionary.
    4. Creates an Enigma machine instance with the specified key and seed.
    5. Encrypts or translates the input text based on the command line arguments.
    6. Optionally exports the key to a file if specified in the command line 
    arguments.
    7. Writes the encrypted or translated text to the specified output file.

    Command line arguments:
        -k, --key (str): Key for Enigma machine
        -s, --seed (str): Seed for key generation
        -t, --translate (bool): Flag indicating if text should be translated 
        instead of encrypted
        -e, --export_key (str): Export key to a file
        -f, --export_file (str): Output file name for the encrypted/translated 
        text

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description='Program for encrypting with Enigma using a key')

    generate_command(parser)

    args = get_args(parser)
    
    en = eni.Enigma.create_enigma_into_key(key=args["key"], seed=args["seed"])

    if args["translate"]:
        cihep = en.translate_update_roters(args["text"])
    else:
        cihep = en.encrypt_update_roters(args["text"])
    
    if args["export_key"]:
        with open(args["export_key"], 'w') as file:
            file.write(args["export_key"])

    with open(args["export_file"], 'w') as file:
        file.write(cihep)


if __name__ == "__main__":
    
    try:
        main()
    except Exception as e:
        print("Error:", e)