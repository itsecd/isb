import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class SymmetricCryptography:
    """
    A class for symmetric cryptography operations.

    This class provides methods for generating symmetric keys,
    encrypting and decrypting data using symmetric encryption algorithms.

    Attributes:
        None
    """
    def __init__(self, key_len: int) -> None:
        """
        Initialize SymmetricCryptography object with key length.

        :param key_len: Length of the key.
        """
        self.key_len = key_len
    
    
    def generate_key(self) -> bytes:
        """
        Generate and return symmetric key.
        
        :param key_len: Length of the key.
        """
        return os.urandom(self.key_len//8)


    def encrypt_text(self, symmetric_key: bytes, text: bytes) -> bytes:
        """
        Encrypts the text using the provided symmetric key.
        
        :param symmetric_key: Symmetric key.
        :param text: Text to encrypt.
        
        :return: Encrypted text.
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_text = padder.update(text) + padder.finalize()
        return iv + encryptor.update(padded_text) + encryptor.finalize()


    def decrypt_text(self, symmetric_key: bytes, encrypted_text: bytes) -> bytes:
        """
        Decrypts the text using the provided symmetric key.
        
        :param symmetric_key: Symmetric key.
        :param encrypted_text: Encrypted text.
        
        :return: Decrypted text.
        """
        iv = encrypted_text[:16]
        encrypted_text = encrypted_text[16:]
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(decrypted_text) + unpadder.finalize()