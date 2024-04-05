import os
import logging
import tabulate
import argparse

import src.serialization as ser
import src.hybrid_tripleDES as hybrid

from src.encryption_algorithms.TypeArgument import TypeArgument

from src.consts import DEFAULT_KEY_SIZE_ASYMMETRIC
from src.encryption_algorithms.consts import (
    DEFAULT_KEY_BYTES_FOR_TRIPLEDES, 
    KEY_COUNT_BITS_FOR_TRIPLEDES
)


def generate_args() -> argparse.ArgumentParser:
    """
    Generate argument parser.

    This function generates an argument parser for the program. The argument
    parser is used to parse the command line arguments and set the
    appropriate options.
    """

    parser = argparse.ArgumentParser(
        description="Single entry point for key generation, encryption, and" \
                    " decryption.")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-gen', '--generate_keys',
                       action='store_true',
                       help='Run key generation mode.')

    group.add_argument('-enc', '--encrypt',
                       action='store_true',
                       help='Run encryption mode.')

    group.add_argument('-dec', '--decryption',
                       action='store_true',
                       help='Run decryption mode.')

    parser.add_argument('-fpk', '--file_private_key',
                        type=str,
                        default=os.path.join("private_key.pem"),
                        help=f'Path to file private key hybrid default:' \
                        f'({os.path.join("private_key.pem")})')

    parser.add_argument('-fsk', '--file_encrypted_symmetric_key',
                        type=str,
                        default=os.path.join("encrypted_symmectrical.pkl"),
                        help=f'Path to file encrypted symmetrical key' \
                             f'hybrid default:(' \
                             f'{os.path.join("encrypted_symmectrical.pkl")})')

    parser.add_argument('-x', '--file_input',
                        type=str,
                        default=None,
                        help=f'Path to read decode file.txt no default.')

    parser.add_argument('-o', '--path_object_output',
                        type=str,
                        default=os.path.join("output.out"),
                        help=f'Path to save output hybrid' \
                             f'default:({os.path.join("output.out")})')

    parser.add_argument('-lrsa', '--len_rsa_key',
                        type=int,
                        default=DEFAULT_KEY_SIZE_ASYMMETRIC,
                        help=f'Size key rsa for generate ' \
                             f'default:({DEFAULT_KEY_SIZE_ASYMMETRIC}).')

    parser.add_argument('-lsym', '--len_symmetrical_key',
                        type=int,
                        default=DEFAULT_KEY_BYTES_FOR_TRIPLEDES,
                        help=f'Size key symmetrical in byte for generate ' \
                             f'using:[{KEY_COUNT_BITS_FOR_TRIPLEDES}] bits ' \
                             f'default:{DEFAULT_KEY_BYTES_FOR_TRIPLEDES} ' \
                             'byte.')

    parser.add_argument('-tl', '--type_len_symmetrical',
                        type=TypeArgument,
                        default=TypeArgument.BYTE,
                        help=f'Size key symmetrical in byte for generate ' \
                             f'using:[{TypeArgument.BIT} = bit, ' \
                             f'{TypeArgument.BYTE} = byte] bits ' \
                             f'default:{TypeArgument.BYTE} byte.')

    parser.add_argument('-l', '--save_logs',
                        type=str,
                        default=None,
                        help=f'Path to the file save logs default(None).')

    parser.add_argument('-lp', '--logs_pretty',
                        type=bool,
                        default=False,
                        help=f'Path to the file save pretty logs ' \
                             f'default(False).')
    return parser


def main():
    """
    Main function.

    This function is the entry point for the program. It handles the command
    line arguments and calls the appropriate functions to generate keys,
    encrypt, or decrypt data.
    """

    try:

        parser = generate_args()
        args = parser.parse_args()

        if args.save_logs:
            logging.basicConfig(
                filename=args.save_logs,
                filemode='w',
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(name)s:%(lineno)d' \
                       ' - %(message)s')
            logger = logging.getLogger(__name__)

        if args.generate_keys:

            """
            Generate hybrid encryption key pair.

            This function generates a hybrid encryption key pair using TripleD
            ES and RSA. The generated key pair consists of a TripleDES key
            encrypted with an RSA private key. The RSA private key is used
            to decrypt the TripleDES key, which is then used to encrypt
            and decrypt data.
            """

            symmetrical_encrypted, private_key = \
                hybrid.generate_hybrid_tripleDes(args.len_rsa_key,
                                                 args.len_symmetrical_key,
                                                 args.type_len_symmetrical)
            ser.save_private_key(args.file_private_key,
                                 private_key)
            ser.save_symmetricTripleDES(args.file_encrypted_symmetric_key,
                                        symmetrical_encrypted)

        elif args.encrypt:

            """
            Encrypt data using hybrid encryption key pair.

            This function encrypts data using a hybrid encryption key pair.
            The data is encrypted using the TripleDES key, which is decrypted
            using the RSA private key.
            """

            private_key = ser.read_private_key(args.file_private_key)
            symmetrical_encrypted = ser.read_symmetricTripleDES(args.file_encrypted_symmetric_key)
            text = ser.read_bytes(args.file_input)

            cipher = hybrid.encrypt_text(text,
                                         symmetrical_encrypted,
                                         private_key)
            ser.save_bytes(args.path_object_output, cipher)

        elif args.decryption:

            """
            Decrypt data using hybrid encryption key pair.

            This function decrypts data using a hybrid encryption key pair.
            The data is decrypted using the TripleDES key, which is decrypted
            using the RSA private key.
            """

            private_key = ser.read_private_key(args.file_private_key)
            symmetrical_encrypted = ser.read_symmetricTripleDES(args.file_encrypted_symmetric_key)
            cipher = ser.read_bytes(args.file_input)

            transalte = hybrid.decrypt_cipher(cipher,
                                              symmetrical_encrypted,
                                              private_key)
            ser.save_bytes(args.path_object_output, transalte)

    except Exception as e:

        if logger:
            logger.error(f"ERROR: {e}")
        else:
            raise RuntimeError("Very bad, cloun", e)

    finally:

        if args.save_logs and args.logs_pretty:
            with open(args.save_logs, 'r') as f:
                logs = f.readlines()

            table = tabulate.tabulate(
                [log.split(' - ') for log in logs],
                headers=['Time', 'Level', 'File', 'Message'],
                tablefmt='fancy_grid')

            with open(args.save_logs, 'w') as f:
                f.write(table)


if __name__ == "__main__":

    try:

        main()

    except Exception as e:

        print(e)
