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

    if args.generation is not None:
        CriptoSystem.generate_keys(CriptoSystem(),
                                   settings['public_key'],
                                   settings['private_key'],
                                   settings['symmetric_key'])
    elif args.encryption is not None:
        CriptoSystem.encrypt_text(settings["text"],
                                  settings['private_key'],
                                  settings["symmetric_key"],
                                  settings["encrypted_text"])
    else:
        pass
    # дешифруем
    '''
    try:
        match args:
            case args.generation:
                CriptoSystem.generate_keys(settings['public_key'],
                                           settings['private_key'],
                                           settings['symmetric_key'])
            case args.encryption:
                pass
            case args.decryption:
                pass
            case _:
                raise ValueError(f"Invalid mode")

    except Exception as e:
        logging.error(f"An error occurred: {e}")'''
