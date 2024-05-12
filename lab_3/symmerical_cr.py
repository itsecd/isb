import logging
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from work_w_files import write_bytes, read_bytes


class SymmetricCryptography:
    """class provides the ability to work with symmetric cryptography"""
    @staticmethod
    def generate_symmetric_key(size_of_key=16) -> bytes:
        return os.urandom(size_of_key)

    @staticmethod
    def serialize_sym_key(path: str, key: bytes) -> None:
        """
        serialize symmetric key
        """
        try:
            write_bytes(path, key)
        except BaseException as ex:
            logging.error(f'error in serialize_sym_key - {ex}')

    @staticmethod
    def deserialize_sym_key(path: str) -> bytes:
        """
        deserialize symmetric key
        """
        try:
            return read_bytes(path)
        except BaseException as ex:
            logging.error(f'error in deserialize_sym_key - {ex}')

    @staticmethod
    def encrypt(symmetric_key: bytes, text: bytes) -> bytes:
        """
        encrypt the text using symmetric key.
        returns a ciphertext.
        """
        try:
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(128).padder()
            padded_text = padder.update(text) + padder.finalize()
            return iv + encryptor.update(padded_text) + encryptor.finalize()
        except Exception as e:
            logging.error(f"error in encrypting data: {e}")

    @staticmethod
    def decrypt(symmetric_key: bytes, encrypted_path: str) -> str:
        """decrypts data from a file """
        encrypted_text = read_bytes(encrypted_path)
        iv = encrypted_text[:16]
        cipher_text = encrypted_text[16:]
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
        decrypt = cipher.decryptor()
        unpacker_text = decrypt.update(cipher_text) + decrypt.finalize()
        decrypt_text = unpacker_text.decode('UTF-8')
        return decrypt_text
