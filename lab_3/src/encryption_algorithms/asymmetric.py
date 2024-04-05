from typing import Tuple

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey


def generate_private_key(public_exponent: int = 65537,
                         key_size: int = 2048) -> RSAPrivateKey:
    """
    Generates a private key of RSA.

    Args:
        - public_exponent(int): The public exponent for the RSA 
        keys (default: 65537).
        - key_size(int): The size of the RSA keys in bits (default: 2048).

    Returns:
        - A tuple containing the private and public keys.
    """

    try:
        return rsa.generate_private_key(public_exponent=public_exponent, 
                                        key_size=key_size)

    except Exception as e:
        raise ValueError(f"Generate private key error: {e}")


def generate_pair_key(public_exponent: int = 65537,
                      key_size: int = 2048
                      ) -> Tuple[RSAPrivateKey, RSAPublicKey]:
    """
    Generates a pair of RSA public and private keys.

    Args:
        - public_exponent(int): The public exponent for the RSA
        keys (default: 65537).
        - key_size(int): The size of the RSA keys in bits (default: 2048).

    Returns:
        - A tuple containing the private and public keys.
    """

    try:
        private_key = rsa.generate_private_key(
            public_exponent=public_exponent, key_size=key_size)
        return private_key, private_key.public_key()

    except Exception as e:
        raise ValueError(f"Generate pair key error: {e}")


def encrypt_with_private_key(text: bytes,
                             private_key: RSAPrivateKey) -> bytes:
    """
    Encrypts a plaintext string using RSA encryption with OAEP padding.

    Args:
        - text(bytes): The plaintext string to encrypt.
        - private_key(RSAPrivateKey): The RSA public key to use for 
        encryption.

    Returns:
        - The encrypted ciphertext as bytes.
    """
    try:
        return private_key.public_key().encrypt(
                    text, 
                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(), label=None))

    except Exception as e:
        raise ValueError(f"Encrypt text to private key error: {e}")


def encrypt_with_public_key(text: bytes, public_key: RSAPublicKey) -> bytes:
    """
    Encrypts a plaintext string using RSA encryption with OAEP padding.

    Args:
        - text(bytes): The plaintext string to encrypt.
        - public_key(RSAPublicKey): The RSA public key to use for encryption.

    Returns:
        - The encrypted ciphertext as bytes.
    """
    try:
        return public_key.encrypt(
                    text, 
                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(), label=None))

    except Exception as e:
        raise ValueError(f"Encrypt text to public key error: {e}")


def decrypt(ciphertext: bytes, private_key: RSAPrivateKey) -> bytes:
    """
    Decrypts a ciphertext string using RSA decryption with OAEP padding.

    Args:
        - ciphertext(bytes): The ciphertext string to decrypt.
        - private_key(RSAPrivateKey): The RSA private key to use for 
        decryption.

    Returns:
        - The decrypted plaintext as bytes.
    """

    try:
        return private_key.decrypt(
                    ciphertext, 
                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(), label=None))
    except Exception as e:
        raise ValueError(f"Decrypt text to private key error: {e}")
    