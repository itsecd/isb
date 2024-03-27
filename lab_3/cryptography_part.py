import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from open_save_part import write_data, read_file
from symmetric import encrypt_decrypt, Action


class Cryptograthy:
    """Class of hybrid cryptosystem. Symmetric Triple Des encryption algorithm, Asymmetric RSA.
    Methods:
        1.key_generation(self)->None
        2.encryption(self, text_file_path:str, encryption_file_path:str) -> None
        3.decryption(self, encryption_file_path:str, decryption_file_path:str)->None:
    """

    def __init__(
        self, symmetric_key: str, private_key: str, public_key: str, key_size: int
    ) -> None:
        """parameters:
        symmetric_key: the path by which to serialize the encrypted symmetric key;
        public_key: the path by which to serialize the public key;
        private_key: the path to serialize the private key;
        key_size: the key size is at the user's choice (8, 16 or 24 bytes)"""
        self.symmetric_key = symmetric_key
        self.private_key = private_key
        self.public_key = public_key
        self.key_size = key_size

    def key_generation(self) -> None:
        """The function which:
        1.1. Generate a key for the symmetric algorithm.
        1.2. Generate keys for the asymmetric algorithm.
        1.3. Serialize asymmetric keys.
        1.4. Encrypt the symmetric encryption key with a public key and save it in the specified path.
        """
        symmetric_key = os.urandom(self.key_size)
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        write_data(
            self.public_key,
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            ),
        )
        write_data(
            self.private_key,
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            ),
        )
        encrypted_symmetric_key = encrypt_decrypt(
            public_key, symmetric_key, Action.ENCRYPT
        )
        write_data(self.symmetric_key, encrypted_symmetric_key)

    def encryption(self, text_file_path: str, encryption_file_path: str) -> None:
        """parameters:
        text_file_path:the path to the encrypted text file;
        encryption_file_path: the path to save the encrypted text file;
        the function which:
            2.1. Decrypt the symmetric key.
            2.2. Encrypt the text using a symmetric algorithm and save it along the specified path.
        """
        sym_key = read_file(self.symmetric_key)
        pr_key = read_file(self.private_key)
        private_key = load_pem_private_key(pr_key, password=None)
        symmetric_key = encrypt_decrypt(private_key, sym_key, Action.DECRYPT)
        data = read_file(text_file_path)
        padder = padding.PKCS7(self.key_size * 8).padder()
        padded_text = padder.update(data) + padder.finalize()
        iv = os.urandom(self.key_size)
        cipher = Cipher(algorithms.TripleDES(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_text) + encryptor.finalize()
        encrypted_data = iv + encrypted_data
        write_data(encryption_file_path, encrypted_data)

    def decryption(self, encryption_file_path: str, decryption_file_path: str) -> None:
        """parameters:
            encryption_file_path: the path to the encrypted text file;
            decryption_file_path: the path to save the decrypted text file.
        the function which:
            3.1. Decrypt the symmetric key.
            3.2. Decrypt the text using a symmetric algorithm and save it along the specified path.
        """
        sym_key = read_file(self.symmetric_key)
        pr_key = read_file(self.private_key)
        private_key = load_pem_private_key(pr_key, password=None)
        symmetric_key = encrypt_decrypt(private_key, sym_key, Action.DECRYPT)
        encrypted_data = read_file(encryption_file_path)
        iv = encrypted_data[: self.key_size]
        encrypted_data = encrypted_data[self.key_size :]
        cipher = Cipher(algorithms.TripleDES(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = padding.PKCS7(self.key_size * 8).unpadder()
        data = unpadder.update(data) + unpadder.finalize()
        write_data(decryption_file_path, data)
