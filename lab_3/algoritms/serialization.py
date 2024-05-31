import logging

from cryptography.hazmat.primitives.serialization import (
    load_pem_public_key,
    load_pem_private_key,
)
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

logging.basicConfig(level=logging.INFO)


class Serialization:
    @staticmethod
    def symmetric_key_serialization(file_path: str, key: bytes) -> None:
        """Serialization of the symmetric encryption key
        Args:
            file_path: file_path for serialization
            key: symmetric key
        """
        try:
            with open(file_path, "wb") as key_file:
                key_file.write(key)
        except Exception as error:
            logging.error(f"Error in symmetric key serialization - {error}")

    @staticmethod
    def symmetric_key_deserialization(file_path: str) -> bytes:
        """Deserialization of the symmetric encryption key
        Args:
            file_path: file_path for deserialization
        Returns:
            symmetric key
        """
        try:
            with open(file_path, "rb") as key_file:
                return key_file.read()
        except Exception as error:
            logging.error(f"Error in symmetric key deserialization - {error}")

    @staticmethod
    def public_key_serialization(public_pem: str, public_key: rsa.RSAPublicKey) -> None:
        """RSA public key serialization
        Args:
            public_pem: file_path for public RSA key serialization
            public_key: public RSA-key
        """
        try:
            with open(public_pem, "wb") as public_out:
                public_out.write(
                    public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )
        except Exception as error:
            logging.error(f"Error in public key serialization - {error}")

    @staticmethod
    def private_key_serialization(
            private_pem: str, private_key: rsa.RSAPrivateKey
    ) -> None:
        """RSA private key serialization
        Args:
            private_pem: file_path for private RSA key serialization
            private_key: private RSA-key
        """
        try:
            with open(private_pem, "wb") as private_out:
                private_out.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
        except Exception as error:
            logging.error(f"Error in private key serialization - {error}")

    @staticmethod
    def public_key_deserialization(public_pem: str) -> rsa.RSAPublicKey:
        """RSA public key deserialization
        Args:
            public_pem: file_path for public RSA key deserialization
        Returns:
            RSA public Key
        """
        try:
            with open(public_pem, "rb") as pem_in:
                public_bytes = pem_in.read()
            return load_pem_public_key(public_bytes)
        except Exception as error:
            logging.error(f"Error in public key deserialization - {error}")

    @staticmethod
    def private_key_deserialization(private_pem: str) -> rsa.RSAPrivateKey:
        """RSA private key deserialization
        Args:
            private_pem: file_path for private RSA key deserialization
        Returns:
            RSA private Key
        """
        try:
            with open(private_pem, "rb") as pem_in:
                private_bytes = pem_in.read()
            return load_pem_private_key(
                private_bytes,
                password=None,
            )
        except Exception as error:
            logging.error(f"Error in private key deserialization - {error}")
