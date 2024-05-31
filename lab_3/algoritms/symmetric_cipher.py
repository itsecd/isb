import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

from serialization import Serialization
from functional import Functional


class Symmetric:
    @staticmethod
    def key_generation(bytes_num: int) -> bytes:
        """generate symmetric key

        Args:
            bytes_num (int):key_len

        Returns:
            bytes: symmetric key
        """
        return os.urandom(bytes_num)

    @staticmethod
    def encryption(
            text_file_path: str,
            path_to_symmetric: str,
            encrypted_text_file_path: str,
    ) -> bytes:
        """encryption by symmetric key

        Args:
            text_file_path (str): path to origin text
            path_to_symmetric (str): path to symmetric key
            encrypted_text_file_path (str): file path for encrypted text

        Returns:
            str: encrypted text
        """
        origin_text = Functional.read_file(text_file_path)
        symmetric_key = Serialization.symmetric_key_deserialization(path_to_symmetric)
        iv = os.urandom(8)
        cipher = Cipher(algorithms.TripleDES(symmetric_key), modes.CBC(iv))
        padder = padding.PKCS7(256).padder()
        text_to_bytes = bytes(origin_text, "UTF-8")
        padded_text = padder.update(text_to_bytes) + padder.finalize()
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        Functional.write_file_bytes(encrypted_text_file_path, encrypted_text)
        return encrypted_text

    @staticmethod
    def decryption(
            path_to_symmetric: str,
            path_to_encrypted_text: str,
            path_to_decrypted_text: str,
    ) -> str:
        """decryption by symmetric key

        Args:
            path_to_symmetric (str): path to key
            path_to_encrypted_text (str): path to ebcrypted file
            path_to_decrypted_text (str): path to decrypted file

        Returns:
            str: decrypted text
        """
        encrypted_text = Functional.read_file_bytes(path_to_encrypted_text)
        symmetric_key = Serialization.symmetric_key_deserialization(path_to_symmetric)
        iv = os.urandom(8)
        cipher = Cipher(algorithms.TripleDES(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(256).unpadder()
        unpadded_dc_text = unpadder.update(decrypted_text) + unpadder.finalize()

        dec_unpad_text = unpadded_dc_text.decode()
        Functional.write_file(path_to_decrypted_text, dec_unpad_text)
        return dec_unpad_text
