import argparse
import logging

from crypto_system import CriptoSystem
from work_w_files import json_to_dict


if __name__ == '__main__':
    settings = json_to_dict('settings.json')

    parser = argparse.ArgumentParser()
    parser.add_argument('-gen', '--generation', nargs=3,
                        metavar=('path_public_key', 'path_private_key', 'path_symmetric_key'),
                        help='start generation process')
    parser.add_argument('-enc', '--encryption', nargs=4,
                        metavar=('path_text', 'path_private_key', 'path_symmetric_key', 'path_encrypted_text'),
                        help='start encryption process')
    parser.add_argument('-dec', '--decryption', nargs=4,
                        metavar=('encrypted_text', 'symmetric_key', 'private_key', 'decrypted_text'),
                        help='start decryption process')

    args = parser.parse_args()

    try:
        match args:
            case args if args.generation:
                CriptoSystem.generate_keys(CriptoSystem(), *args.generation)
            case args if args.encryption:
                CriptoSystem.encrypt_text(*args.encryption)
            case args if args.decryption:
                CriptoSystem.decrypt_text(*args.decryption)
            case _:
                raise ValueError("Invalid mode")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
