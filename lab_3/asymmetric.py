import logging

from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


logging.basicConfig(level=logging.INFO)


class AsymmetricCryptography:
    """
    Class that contains methods for generating key,
    encryption and decryption by asymmetrical method.
    Methods:
    generate_key(self, size: int) -> tuple,
    serialize_key(self, key: tuple) -> None,
    deserialize_key(self) -> tuple,
    encrypt(self, data: bytes, key: bytes) -> bytes,
    decrypt(self, data: bytes, key: bytes) -> bytes.
    """

    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        """Initializes AsymmetricCryptography class object.
        :param private_key_path: path for saving private key.
        :param public_key_path: path for saving public key.
        :return: None.
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path

    def generate_key(self, size: int) -> tuple:
        """Generates key for asymmetrical method.
        :param size: size of keys in bits.
        :return: tuple of private and public keys.
        """
        try:
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            public_key = private_key.public_key()
            return private_key, public_key
        except Exception as exc:
            logging.error(f"Generating asymmetrical keys error: {exc}\n")

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """Does asymmetrical encryption of data using key.
        :param data: bytes object that is needed to encrypt.
        :param key: bytes object key for encryption.
        :return: bytes of encrypted data.
        """
        try:
            c_data = key.encrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            return c_data
        except Exception as exc:
            logging.error(f"Asymmetrical encryption error: {exc}\n")

    def decrypt(self, data: bytes, key: bytes) -> bytes:
        """Does asymmetrical decryption of encrypted data using key.
        :param data: bytes object that is needed to decrypt.
        :param key: bytes object key for decryption.
        :return: bytes of decrypted data.
        """
        try:
            c_data = key.decrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            return c_data
        except Exception as exc:
            logging.error(f"Asymmetrical decryption error: {exc}\n")
 