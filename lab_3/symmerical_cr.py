import logging
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from work_w_files import write_file, read_file


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
            write_file(path, key)
        except BaseException as ex:
            logging.error(f'error in serialize_sym_key - {ex}')

    @staticmethod
    def deserialize_sym_key(path: str) -> bytes:
        """
        deserialize symmetric key
        """
        try:
            return read_file(path)
        except BaseException as ex:
            logging.error(f'error in deserialize_sym_key - {ex}')

    def encrypt(self, symmetric_key: bytes, text: bytes) -> bytes:
        """
        encrypt the text using symmetric key.
        returns a tuple containing the key and the ciphertext.
        """
        try:
            #key = self.generate_symmetric_key()
            key = os.urandom(16)
            cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(key))
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(128).padder()
            padded_text = padder.update(text) + padder.finalize()
            return encryptor.update(padded_text) + encryptor.finalize()
        except Exception as e:
            logging.error(f"Error occurred while encrypting data: {e}")
