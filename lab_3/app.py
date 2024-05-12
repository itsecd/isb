import argparse
import logging

from crypto_system import CriptoSystem
from work_w_files import json_to_dict


if __name__ == '__main__':
    settings = json_to_dict('settings.json')

    #3parser = argparse.ArgumentParser()
    #group = parser.add_mutually_exclusive_group(required=True)
    #group.add_argument('-gen', '--generation', help='start generation keys')
    #group.add_argument('-enc', '--encryption', help='start encryption')
    #group.add_argument('-dec', '--decryption', help='start decryption')

    #args = parser.parse_args()
    parser = argparse.ArgumentParser()
    #group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
    #group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
    #group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')

    args = parser.parse_args()
    if args.generation is not None:
        CriptoSystem.generate_keys(CriptoSystem(),
                                   settings['public_key'],
                                   settings['private_key'],
                                   settings['symmetric_key'])
    elif args.encryption is not None:
        pass
    else:
        pass
    # дешифруем
    '''try:
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

