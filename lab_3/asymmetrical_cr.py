import logging

from cryptography.hazmat.primitives import serialization, hashes, asymmetric
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


class AsymmetricalCryptograpy:
    """class provides the ability to work with symmetric cryptography"""
    @staticmethod
    def generate_asymmetric_keys() -> tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        """generates asymmetric keys"""
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        return keys, keys.public_key()

    @staticmethod
    def serialize_private_and_public_keys(
            private: RSAPrivateKey,
            path_private: str,
            public: RSAPublicKey,
            path_public: str) -> None:
        """
        serialize private and public keys

        params:
            private: private key
            path_private: path to file for private key
            public: public key
            path_public: path to file with public key
        """
        try:
            with open(path_public, 'wb') as file:
                file.write(
                    public.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except BaseException as ex:
            logging.error(f'error in serialize_public_key - {ex}')
        try:
            with open(path_private, 'wb') as file:
                file.write(
                    private.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption()))
        except BaseException as ex:
            logging.error(f'error in serialize_private_key - {ex}')

    @staticmethod
    def deserialize_private_key(
            path_private: str) -> RSAPrivateKey:
        """deserialize private key"""
        try:
            with open(path_private, 'rb') as file:
                return load_pem_private_key(file.read(), password=None, )
        except BaseException as ex:
            logging.error(f'error in deserialize_private_key - {ex}')

    @staticmethod
    def deserialize_public_key(
            path_public: str) -> RSAPublicKey:
        """deserialize public key"""
        try:
            with open(path_public, 'rb') as file:
                return load_pem_public_key(file.read())
        except BaseException as ex:
            logging.error(f'error in deserialize_public_key - {ex}')

    @staticmethod
    def encrypt_with_public_key(public_key: RSAPublicKey, text: bytes) -> bytes:
        """encrypt text using the public key."""
        try:
            return public_key.encrypt(
                text,
                asymmetric.padding.OAEP(
                    mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            logging.error(f"error in encrypting data with public key: {e}")

    @staticmethod
    def decrypt_with_private_key(private_key: RSAPrivateKey, encrypted_text: bytes) -> bytes:
        """decrypt data using the private key."""
        try:
            return private_key.decrypt(
                encrypted_text,
                asymmetric.padding.OAEP(
                    mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            logging.error(f"error in decrypt with private key: {e}")

