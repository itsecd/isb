import os
import fetch_data as wr
from base64 import b64encode, b64decode
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)




class HybridCryptosystem():
    """
    A hybrid cryptosystem that uses RSA to encrypt a symmetric key and Camellia to encrypt the data.
    """
    def __init__(self, key_size=256):
        """Initializes the hybrid cryptosystem.
        Args:
            key_size (int): The size of the Camellia key in bits (defaults to 256).
        """
        self.__symmetric_key = os.urandom((key_size + 8 - 1) // 8)
        self.__private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.__cipher = Cipher(algorithms.Camellia(self.__symmetric_key),
                               mode=modes.CBC(os.urandom(16)))
        self.__public_key = self.__private_key.public_key()

    def serialize_public_key(self, path: str) -> None:
        """Serializes the public key to a PEM file.
        Args:
            path (str): The path to the file to save the public key.
        """
        pem = self.__public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        wr.write(path, pem)

    def serialize_private_key(self, path: str) -> None:
        """Serializes the private key to a PEM file.
        Args:
            path (str): The path to the file to save the private key.
        """
        pem = self.__private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption())
        wr.write(path, pem)

    def serialize_symmetric_key(self, path: str) -> None:
        """Encrypts the symmetric key with the public key and serializes to a file.
        Args:
            path (str): The path to the file to save the encrypted symmetric key.
        """
        key = self.__symmetric_key
        key = self.__public_key.encrypt(key, 
                                        rsa_padding.OAEP(mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                                                     algorithm=hashes.SHA256(),
                                                     label=None))
        wr.write(path, key)  

    def deserialize_symmetric_key(self, path: str) -> None:
        """Decrypts the symmetric key with the private key and deserializes from a file.
        Args:
            path (str): The path to the file containing the encrypted symmetric key.
        """
        key = wr.read(path)
        key = self.__private_key.decrypt(key,
                                        rsa_padding.OAEP(mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                                                     algorithm=hashes.SHA256(),
                                                     label=None))
        self.__symmetric_key = key
        self.__cipher = Cipher(algorithms.Camellia(self.__symmetric_key),
                               mode=modes.CBC(key))

    def deserialize_public_key(self, path: str) -> None:
        """Deserializes the public key from a PEM file.
        Args:
            path (str): The path to the file containing the public key in PEM format.
        """
        public_bytes = wr.read(path)
        self.__public_key = load_pem_public_key(public_bytes)

    def deserialize_private_key(self, path: str) -> None:
        """Deserializes the private key from a PEM file.
        Args:
            path (str): The path to the file containing the private key in PEM format.
        """
        private_bytes = wr.read(path)
        self.__private_key = load_pem_private_key(private_bytes,password=None,)

    def encrypt(self, plaintext: str) -> bytes:
        """Encrypts data using the Camellia symmetric key.
        Args:
            plaintext (str): The data to encrypt.
        Returns:
            bytes: The encrypted data.
        """
        padder = padding.ANSIX923(64).padder()
        text = bytes(plaintext,'UTF-8')
        padded_text = padder.update(text) + padder.finalize()
        encryptor = self.__cipher.encryptor()
        ciphertext = encryptor.update(padded_text) + encryptor.finalize()
        return ciphertext

    def decrypt(self, plaintext: bytes) -> str:
        """Decrypts data using the Camellia symmetric key.
        Args:
            plaintext (bytes): The encrypted data.
        Returns:
            str: The decrypted data.
        """
        decryptor = self.__cipher.decryptor()
        dc_text = decryptor.update(plaintext) + decryptor.finalize()

        unpadder = padding.ANSIX923(64).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()
        return dc_text.decode('UTF-8')
