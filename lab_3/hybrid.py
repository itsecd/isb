import logging

from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding

from functions import FileReadWrite
from symmetric import SymmetricCryptography
from asymmetric import AsymmetricCryptography


logging.basicConfig(level=logging.INFO)


class HybridCryptography:
    """Class that contains methods for generating key,
    encryption and decryption by hybrid method(symmetrical and asymmetrical).
    Methods:
    generate_key(self, size: int) -> bytes,
    encrypt(self, text_path: str, encrypted_text_path: str) -> None,
    decrypt(self, text_path: str, decrypted_text_path: str) -> None.
    """

    def __init__(
        self, symmetric_key_path: str, private_key_path: str, public_key_path: str
    ) -> None:
        """Initializes HybridCryprography class object.
        :param symmetric_key_path: path for saving symmetrical key.
        :param private_key_path: path for saving private key.
        :param public_key_path: path for saving public key.
        :return: None.
        """
        self.symmetric = SymmetricCryptography(symmetric_key_path)
        self.asymmetric = AsymmetricCryptography(private_key_path, public_key_path)

    def set_paths(
        self, symmetric_key_path: str, private_key_path: str, public_key_path: str
    ) -> None:
        """Sets new paths to keys.
        :param symmetric_key_path: path for saving symmetrical key.
        :param private_key_path: path for saving private key.
        :param public_key_path: path for saving public key.
        :return: None.
        """
        self.asymmetric.private_key_path = private_key_path
        self.asymmetric.public_key_path = public_key_path
        self.symmetric.key_path = symmetric_key_path

    def generate_keys(self, size: int) -> None:
        """Generates key for hybrid method.
        :param size: size of keys in bits.
        :return: tuple of private and public keys.
        """
        try:
            if size != 16 and size != 24 and size != 32:
                raise ValueError("Size of keys must be 128, 192 or 256")
            symmetric_key = self.symmetric.generate_key(size)
            asymmetric_key = self.asymmetric.generate_key(size)
            private_key, public_key = asymmetric_key
            FileReadWrite.serialize_private_key(self.asymmetric.private_key_path, private_key)
            FileReadWrite.serialize_public_key(self.asymmetric.public_key_path, public_key)
            FileReadWrite.write_bytes(
                self.symmetric.key_path,
                public_key.encrypt(
                    symmetric_key,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None,
                    ),
                ),
            )
        except Exception as exc:
            logging.error(f"Genereting keys for HybridCryptography error: {exc}\n")

    def encrypt(self, text_path: str, encrypted_text_path: str) -> None:
        """Does hybrid encryption of data.
        :param text_path: path to file with data that is needed to encrypt.
        :param encrypted_text_path: path to file for saving encrypted data.
        :return: None.
        """
        try:
            text = bytes(FileReadWrite.read_txt(text_path), "UTF-8")
            key = FileReadWrite.deserialize_private_key(self.asymmetric.private_key_path)
            symmetric_key = self.asymmetric.decrypt(
                FileReadWrite.read_bytes(self.symmetric.key_path), key
            )
            c_text = self.symmetric.encrypt(text, symmetric_key)
            FileReadWrite.write_bytes(encrypted_text_path, c_text)
        except Exception as exc:
            logging.error(f"Hybrid encryption error: {exc}\n")

    def decrypt(self, text_path: str, decrypted_text_path: str) -> None:
        """Does hybrid dencryption of data.
        :param text_path: path to file with data that is needed to decrypt.
        :param decrypted_text_path: path to file for saving decrypted data.
        :return: None.
        """
        try:
            c_data = FileReadWrite.read_bytes(text_path)
            key = FileReadWrite.deserialize_private_key(self.asymmetric.private_key_path)
            symmetric_key = self.asymmetric.decrypt(
                FileReadWrite.read_bytes(self.symmetric.key_path), key
            )
            dc_data = self.symmetric.decrypt(c_data, symmetric_key)
            FileReadWrite.write_bytes(decrypted_text_path, dc_data)
        except Exception as exc:
            logging.error(f"Hybrid decryption error: {exc}\n")
 