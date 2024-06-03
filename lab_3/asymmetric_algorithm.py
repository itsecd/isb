import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

logging.basicConfig(level=logging.INFO)


class AsymmetricAlgorithm:
    """
    A class for asymmetric cryptography operations.

    This class provides methods for generating key pairs,
    encrypting and decrypting data using asymmetric encryption algorithms.

    """

    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        """
        Initialize AsymmetricCryptography object with public and private key paths.

        :param private_key_path: Path to the private key file.
        :param public_key_path: Path to the public key file.
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path

    @staticmethod
    def generate_key_pair(key_size: int) -> tuple:
        """
        Generate an RSA key pair.

        :param key_size: The size of the RSA key in bits.

        :return: A tuple containing the private and public keys.
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def encrypt_with_public_key(public_key: rsa.RSAPublicKey, text: bytes) -> bytes:
        """
        Encrypts ntext using the provided public key.

        :param public_key: The RSA public key used for encryption.
        :param text: The text to be encrypted.

        :return: The ciphertext produced by the encryption process.
        """
        return public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                     algorithm=hashes.SHA256(), label=None))

    @staticmethod
    def decrypt_with_private_key(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
        """
        Decrypts ciphertext using the provided private key.

        :param private_key: The RSA private key used for decryption.
        :param ciphertext: The ciphertext to be decrypted.

        :return: The text produced by the decryption process.
        """
        return private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                            algorithm=hashes.SHA256(), label=None))
