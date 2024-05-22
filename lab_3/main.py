import argparse
import logging

from hybrid_system import HybridSystemAlgorithm
from symmetric_algorithm import SymmetricAlgorithm
from asymmetric_algorithm import AsymmetricAlgorithm
from serialize_deserialize import SerializeDeserialize
from config import PATHS


def valid_key_length(key_length: int) -> bool:
    """
    Checking that key length is valid for chosen algorithm
    :param key_length: int length of the key
    :return: bool answer valid or not
    """
    return key_length == 128 or key_length == 192 or key_length == 256


def main():
    parser = argparse.ArgumentParser(description="Entry point of the program")
    paths_default = SerializeDeserialize(PATHS)
    paths_dict = paths_default.read_json_file()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-key', '--keys',
                       action='store_true',
                       help='Run key generation mode.')
    group.add_argument('-enc', '--encryption',
                       action='store_true',
                       help='Run encryption mode.')
    group.add_argument('-dec', '--decryption',
                       action='store_true',
                       help='Run decryption mode.')

    parser.add_argument('-kl', '--key_length',
                        type=int,
                        default=128,
                        help='Length of the symmetric key in bits (default: 448).')

    parser.add_argument('-text', '--input_text_file',
                        type=str,
                        default=paths_dict["text_file"],
                        help='Path of the input txt file with text(default: paths_dict["text_file"]')

    parser.add_argument('-public_key', '--public_key_path',
                        type=str,
                        default=paths_dict["public_key"],
                        help='Path of the public pem file with key(default: paths_dict["public_key"]')

    parser.add_argument('-private_key', '--private_key_path',
                        type=str,
                        default=paths_dict["private_key"],
                        help='Path of the private pem file with key(default: paths_dict["private_key"]')

    parser.add_argument('-sym_key', '--symmetric_key_path',
                        type=str,
                        default=paths_dict["symmetric_key_file"],
                        help='Path of the symmetric txt file with key(default: paths_dict["symmetric_key_file"]')

    parser.add_argument('-enc_path', '--encrypted_text_path',
                        type=str,
                        default=paths_dict["encrypted_text_file"],
                        help='Path of the txt file with encrypted text(default: paths_dict["encrypted_text_file"]')

    parser.add_argument('-dec_path', '--decrypted_text_path',
                        type=str,
                        default=paths_dict["decrypted_text_file"],
                        help='Path of the txt file with decrypted text(default: paths_dict["decrypted_text_file"]')

    try:
        args = parser.parse_args()
        if not valid_key_length(args.key_length):
            raise argparse.ArgumentTypeError
        symmetric = SymmetricAlgorithm(args.key_length)
        asymmetric = AsymmetricAlgorithm(args.private_key_path, args.public_key_path)
        hybrid_system = HybridSystemAlgorithm(args.input_text_file,
                                              args.symmetric_key_path, args.encrypted_text_path,
                                              args.decrypted_text_path, symmetric, asymmetric)
        match args:
            case args if args.keys:
                hybrid_system.generate_keys()

            case args if args.encryption:
                hybrid_system.encrypt_text()

            case args if args.decryption:
                hybrid_system.decrypt_text()

    except argparse.ArgumentTypeError:
        logging.error(f"Error in arguments, key_length must be in 128, 192, 256 bits")


if __name__ == "__main__":
    main()
