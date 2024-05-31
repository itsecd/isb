import sys
import argparse
import logging

sys.path.append("algoritms")

from algoritms.asymmetric_cipher import Asymmetric
from algoritms.symmetric_cipher import Symmetric
from algoritms.serialization import Serialization
from algoritms.functional import Functional

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-mode", type=str, help="key_generation OR encryption OR decryption"
    )
    args = parser.parse_args()

    settings = Functional.read_json("settings.json")

    def hybrid_system_keys_generation():
        symmetric_key = Symmetric.key_generation(settings["key_length"])
        Serialization.symmetric_key_serialization(
            settings["symmetric_key"], symmetric_key
        )

        public_key, private_key = Asymmetric.key_generation()
        Serialization.public_key_serialization(settings["public_key"], public_key)
        Serialization.private_key_serialization(settings["private_key"], private_key)

        logging.info("keys was generated")

    def hybrid_system_encryption():
        encrypted_text = Symmetric.encryption(
            settings["initial_file"],
            settings["symmetric_key"],
            settings["encrypted_file"],
        )

        Asymmetric.encryption(
            settings["public_key"],
            settings["symmetric_key"],
            settings["encrypted_symmetric_key"],
        )

        logging.info("text was encrypted")

    def hybrid_system_decryption():
        Asymmetric.decryption(
            settings["private_key"],
            settings["encrypted_symmetric_key"],
            settings["decrypted_symmetric_key"],
        )

        decrypted_text = Symmetric.decryption(
            settings["symmetric_key"],
            settings["encrypted_file"],
            settings["decrypted_file"],
        )
        logging.info(f"Decrypted text: {decrypted_text}")

    task = {
        "key_generation": hybrid_system_keys_generation,
        "encryption": hybrid_system_encryption,
        "decryption": hybrid_system_decryption,
    }
    task[f"{args.mode}"]()


if __name__ == "__main__":
    main()
