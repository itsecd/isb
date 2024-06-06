import argparse

from asymmetric import Asymmetric
from symmetric import Symmetric
from for_work_with_file import Support


def clean_text_files(file_paths: list):
    """
        Clean files.

        Parameters:
        path (str): The path to files.

        Returns:
        None
        """
    for file_path in file_paths:
        try:
            with open(file_path, 'w') as file:
                file.write('')
            print(f"File '{file_path}' cleaning successfull.")
        except FileNotFoundError:
            print(f"Error: the file could not be found: '{file_path}'")
        except IOError:
            print(f"Error: the file could not be open: '{file_path}'")


def actions_for_generating_keys(symmetric: Symmetric, asymmetric: Asymmetric, settings: dict)->None:
    symmetric.generate_key()
    symmetric.serialize_sym_key(settings['sym_key'])
    asymmetric.generate_key_pair()
    asymmetric.serialize_asym_key(settings['private_key'],'private')
    asymmetric.serialize_asym_key(settings['public_key'],'public')
    print(f'Key generare and serialize successfull')


def actions_to_encrypt_symmetric_key(symmetric: Symmetric, asymmetric: Asymmetric, settings: dict)->None:
    sym_key = symmetric.deserialize_sym_key(settings['sym_key'])
    if sym_key is None:
        print("Error: sym_key do not download")
        return
    to_write = asymmetric.process_symmetric_key(sym_key, settings['public_key'],'encrypt')
    Support.write_bytes_to_txt(to_write,settings['encrypted_sym'])            
    print(f'The symmetric key has been successfully encrypted')


def actions_to_decrypt_symmetric_key(asymmetric: Asymmetric, settings: dict)->None:
    asym_key = Support.read_bytes(settings['encrypted_sym'])
    sym_key = asymmetric.process_symmetric_key(asym_key, settings['private_key'],'decrypt')            
    Support.write_bytes_to_txt(sym_key, settings['decrypted_sym'])
    print(f'The symmetric key has been successfully decrypted')


def actions_for_encrypting_text(symmetric: Symmetric, settings: dict)->None:
    sym_key = symmetric.deserialize_sym_key(settings['sym_key'])
    text = Support.read_from_file(settings['original_text'])
    e_text = symmetric.process_text(text, sym_key, 'encrypt')
    Support.write_bytes_to_txt(e_text, settings['encrypted_text'])

    print(f'The text has been successfully encrypted')


def actions_for_decrypting_text(symmetric: Symmetric, settings: dict)->None:
    dec_sym_key = symmetric.deserialize_sym_key(settings['decrypted_sym'])
    text = Support.read_bytes(settings['encrypted_text'])
    dec_text = symmetric.process_text(text, dec_sym_key,'decrypt')
    Support.save_to_file(settings['decrypted_text'], dec_text)
    print(f'The text has been successfully decrypted')


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Generate keys', action='store_true')
    group.add_argument('-encr_k', '--encryption_key', help='Encrypted of sym key', action='store_true')
    group.add_argument('-decr_k', '--decription_key', help='Decrypted of sym key', action='store_true')
    group.add_argument('-encr', '--encryption', help='Encrypted of text', action='store_true')
    group.add_argument('-decr', '--decryption', help='Decrypted of text', action='store_true')
    group.add_argument('-clear', '--clear', help='Clear all files without original text file', action='store_true')
    parser.add_argument('settings', type=str, help='Settings', nargs='?', default='settings.json')
    args = parser.parse_args()
    symmetric = Symmetric()
    asymmetric = Asymmetric()
    settings = Support.read_from_json_file('settings.json')
    match args:
        case args if args.generation:
            actions_for_generating_keys(symmetric, asymmetric, settings)
        case args if args.encryption:
           actions_for_encrypting_text(symmetric, settings)
        case args if args.encryption_key:
            actions_to_encrypt_symmetric_key(symmetric, asymmetric, settings)  
        case args if args.decription_key:
            actions_to_decrypt_symmetric_key(asymmetric, settings)
        case args if args.decryption:
            actions_for_decrypting_text(symmetric, settings)
        case args if args.clear:
            clean_text_files([settings['decrypted_sym'], settings['decrypted_text'], settings['encrypted_text'], settings['private_key'], settings['public_key'], settings['sym_key']])
            print("All file cleaning successfull.")
        case _:
            print("Choose work-mode")
    

if __name__ == '__main__':
    main()
    