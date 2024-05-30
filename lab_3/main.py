import argparse
import crypto
import fetch_data as wr

if __name__ == "__main__":
    path = wr.json_read("settings.json")
    parser = argparse.ArgumentParser()
    parser.add_argument("-kl", "--key_length", help="Длина ключа", required=False)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-gen",
        "--generation",
        help="Запускает режим генерации ключей",
        action="store_true",
    )
    group.add_argument(
        "-enc",
        "--encryption",
        help="Запускает режим шифрования",
        action="store_true",
    )
    group.add_argument(
        "-dec",
        "--decryption",
        help="Запускает режим дешифрования",
        action="store_true",
    )
    parser.add_argument(
        "-sp",
        "--symmetric_key_path",
        help="путь к симметричному ключу",
        required=False,
        default=path["symmetric_key"]
    )
    parser.add_argument(
        "-pk", "--public_key_path", 
        help="путь к открытому ключу", 
        required=False,
        default=path["public_key"]
    )
    parser.add_argument(
        "-sk", "--secret_key_path",
        help="путь к закрытому ключу",
        required=False,
        default=path["secret_key"]
    )
    parser.add_argument(
        "-if", "--initial_file_path",
        help="путь к исходному файлу (для шифрования)",
        required=False,
        default=path["initial_file"]
    )
    parser.add_argument(
        "-ef", "--encrypted_file_path",
        help="путь к зашифрованному файлу (для дешифрования)",
        required=False,
        default=path["encrypted_file"]
    )
    parser.add_argument(
        "-df", "--decrypted_file_path",
        help="путь к расшифрованному файлу",
        required=False,
        default=path["decrypted_file"]
    )
    args = parser.parse_args()
    system = crypto.HybridCryptosystem(key_size= int(args.key_length))
    match args.action:
        case "generation":
            system.serialize_symmetric_key(args.symmetric_key_path)
            system.serialize_public_key(args.public_key_path)
            system.serialize_private_key(args.secret_key_path)
        case "encryption":
            text = wr.read_txt(args.initial_file_path)
            system.deserialize_private_key(args.secret_key_path)
            system.deserialize_symmetric_key(args.symmetric_key_path)
            encrypt_text = system.encrypt(text)
            wr.write(args.encrypted_file_path, encrypt_text)
        case "decryption":
            text = wr.read(args.encrypted_file_path)
            system.deserialize_private_key(args.secret_key_path)
            system.deserialize_symmetric_key(args.symmetric_key_path)
            decrypt_text = system.decrypt(text)
            wr.write_txt(args.decrypted_file_path, decrypt_text)