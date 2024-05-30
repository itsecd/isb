import os
import logging

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


logging.basicConfig(level=logging.INFO)


class SymmetricCryptography:
    """
    Class that contains methods for generating key,
    encryption and decryption by symmetrical method.
    Methods:
    generate_key(self, size: int) -> bytes,
    encrypt(self, data: bytes, key: bytes) -> bytes,
    decrypt(self, data: bytes, key: bytes) -> bytes.
    """

    def __init__(self, key_path: str) -> None:
        """Initialises SymmetricCryptography class object.
        :param key_path: path for saving key.
        :return: None.
        """
        self.key_path = key_path

    def generate_key(self, size: int) -> bytes:
        """Generates key for symmetrical method.
        :param size: size of key in bits.
        :return: key as bytes object.
        """
        try:
            key = os.urandom(size)
            return key
        except Exception as exc:
            logging.error(f"Generating symmetrical key error: {exc}\n")

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        """Does symmetrical encryption of data using key.
        :param data: bytes object that is needed to encrypt.
        :param key: bytes object key for encryption.
        :return: bytes of encrypted data.
        """
        try:
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(256).padder()
            padded_text = padder.update(data) + padder.finalize()
            c_text = iv + encryptor.update(padded_text) + encryptor.finalize()
            return c_text
        except Exception as exc:
            logging.error(f"Symmetrical encryption error: {exc}\n")

    def decrypt(self, data: bytes, key: bytes) -> bytes:
        """Does symmetrical decryption of encrypted data using key.
        :param data: bytes object that is needed to decrypt.
        :param key: bytes object key for decryption.
        :return: bytes of decrypted data.
        """
        try:
            iv = data[:16]
            data = data[16:]
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            dc_data = decryptor.update(data) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            unpadded_dc_data = unpadder.update(dc_data) + unpadder.finalize()
            return unpadded_dc_data
        except Exception as exc:
            logging.error(f"Symmetrical decryption error: {exc}\n")
 