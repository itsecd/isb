import argparse
import logging

from crypto_system import CriptoSystem
from work_w_files import json_to_dict


if __name__ == '__main__':
    settings = json_to_dict('settings.json')

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='start generation process')
    group.add_argument('-enc', '--encryption', help='start encryption process')
    group.add_argument('-dec', '--decryption', help='start decryption process')

    args = parser.parse_args()

    try:
        match args:
            case args if args.generation:
                CriptoSystem.generate_keys(CriptoSystem(),
                                           settings['public_key'],
                                           settings['private_key'],
                                           settings['symmetric_key'])
            case args if args.encryption:
                CriptoSystem.encrypt_text(settings['text'],
                                          settings['private_key'],
                                          settings['symmetric_key'],
                                          settings['encrypted_text'])
            case args if args.decryption:
                CriptoSystem.decrypt_text(settings['encrypted_text'],
                                          settings['symmetric_key'],
                                          settings['private_key'],
                                          settings['decrypted_text'])
            case _:
                raise ValueError(f"invalid mode")

    except Exception as e:
        logging.error(f"error occurred: {e}")
