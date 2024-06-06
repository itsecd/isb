import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Symmetric:
    """
    Class for symmetric encryption operations.
    """
    def __init__(self):
        """
        Initializes the key to None.
        """
        self.key = None
        
    def generate_key(self) -> bytes:
        """
        Generates a random symmetric key.

        Returns:
        bytes: The generated symmetric key.
        """
        self.key = os.urandom(16)
        return self.key

    def __pad_data(self, text: str) -> bytes:
        """
        Pads the input text to match the block size.

        Parameters:
        text (str): The text to pad.

        Returns:
        bytes: The padded text.
        """
        padder = padding.PKCS7(128).padder()
        btext = bytes(text, 'UTF-8')
        padded_text = padder.update(btext) + padder.finalize()
        return padded_text
    
    def __unpad_data(self, decrypted_text: bytes) -> str:
        """
        Removes the padding from decrypted text.

        Parameters:
        decrypted_text (bytes): The decrypted text.

        Returns:
        str: The unpadded text.
        """
        unpadder = padding.PKCS7(128).unpadder()
        unpadded_text = unpadder.update(decrypted_text) + unpadder.finalize()
        return unpadded_text.decode('UTF-8')

    def process_text(self, text: str, key: bytes, mode: str) -> bytes:
        """
        Encrypts or decrypts text using the provided symmetric key.

        Parameters:
        text (str): The text to process.
        key (bytes): The symmetric key.
        mode (str): The operation mode ('encrypt' or 'decrypt').

        Returns:
        bytes: The processed text.
        """
        if mode == 'encrypt':
            iv = os.urandom(16)
            cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            encrypted_text = encryptor.update(self.__pad_data(text)) + encryptor.finalize()
            encrypted_text = iv + encrypted_text
            return encrypted_text
        elif mode == 'decrypt':
            iv = text[:16]
            cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            decrypted_text = decryptor.update(text[16:]) + decryptor.finalize()
            return self.__unpad_data(decrypted_text)
        else:
            raise ValueError("Invalid mode provided. Use 'encrypt' or 'decrypt'.")
