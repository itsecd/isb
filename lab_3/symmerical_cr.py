import logging
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricCryptography:
    @staticmethod
    def generate_symmetric_key(size_of_key=16) -> bytes:
        return os.urandom(size_of_key)

    @staticmethod
    def serialize_sym_key(path: str, key: bytes) -> None:
        """
        serialize symmetric key
        """
        try:
            with open(path, 'wb') as file:
                file.write(key)
        except BaseException as ex:
            logging.error(f'error in serialize_sym_key - {ex}')

    @staticmethod
    def deserialize_sym_key(path: str) -> bytes:
        """
        deserialize symmetric key
        """
        try:
            with open(path, 'rb') as file:
                return file.read()
        except BaseException as ex:
            logging.error(f'error in deserialize_sym_key - {ex}')

    def encrypt(self, symmetric_key: bytes, text: bytes, size_of_key=16) -> tuple:
        """
        encrypt the text using symmetric key.
        returns a tuple containing the key and the ciphertext.
        """
        try:
            key = self.generate_symmetric_key()
            cipher = Cipher(algorithms.IDEA(symmetric_key), modes.CBC(key))
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(size_of_key*8).padder()
            padded_text = padder.update(text) + padder.finalize()
            ciphertext = encryptor.update(padded_text) + encryptor.finalize()
            return key, ciphertext
        except Exception as e:
            logging.error(f"Error occurred while encrypting data: {e}")
