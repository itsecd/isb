import logging

from typing import Tuple

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from .consts import DEFAULT_KEY_SIZE_ASYMMETRIC

from .encryption_algorithms import asymmetric
from .encryption_algorithms.TypeArgument import TypeArgument
from .encryption_algorithms.SymmetricTripleDES import SymmetricTripleDES

from .encryption_algorithms.consts import DEFAULT_KEY_BYTES_FOR_TRIPLEDES, DEFAULT_LEN_BYTES_PADDING_BLOCK_FOR_TRIPLEDES

logger = logging.getLogger(__name__)

def generate_hybrid_tripleDes(len_rsa_private_key: int = DEFAULT_KEY_SIZE_ASYMMETRIC,
                              len_key_symmetrical: int = DEFAULT_KEY_BYTES_FOR_TRIPLEDES, 
                              type_len_symmetrical: TypeArgument = TypeArgument.BYTE
                              ) -> Tuple[SymmetricTripleDES, RSAPrivateKey]:
    
    """
    Generate a hybrid encryption key pair using TripleDES and RSA.

    The generated key pair consists of a TripleDES key encrypted with an RSA private key.
    The RSA private key is used to decrypt the TripleDES key, which is then used to encrypt and decrypt data.

    Args:
        - len_rsa_private_key: The length of the RSA private key in bits.
        - len_key_symmetrical: The length of the TripleDES key in bytes.
        - type_len_symmetrical: The type of the length of the TripleDES key.

    Returns:
        - A tuple containing the TripleDES key and the RSA private key.
    """
    
    try:
        key = SymmetricTripleDES.generate_key(len_key_symmetrical, type_len_symmetrical)
        private_key = asymmetric.generate_private_key(key_size=len_rsa_private_key)
        encrypt_key = asymmetric.encrypt(key, private_key.public_key())

        logger.info("Generate hybrid tripleDes successful")
        return (SymmetricTripleDES(stored_key=encrypt_key, init_vector=SymmetricTripleDES.generate_init_vector()), private_key)
    
    except Exception as e:
        logger.error(f"Generate hybrid tripleDes error: {e}")

def encrypt_text(text: bytes, 
                 symmetric_encrypt_key: SymmetricTripleDES, 
                 asymetric_key: RSAPrivateKey, 
                 len_block_padding: int = DEFAULT_LEN_BYTES_PADDING_BLOCK_FOR_TRIPLEDES, 
                 type_len_block_padding: TypeArgument = TypeArgument.BYTE
                 ) -> bytes:
    
    """
    Encrypt a text using a hybrid encryption key pair.

    The text is encrypted using the TripleDES key, which is decrypted using the RSA private key.

    Args:
        - text: The text to encrypt.
        - symmetric_encrypt_key: The TripleDES key.
        - asymetric_key: The RSA private key.
        - len_block_padding: The length of the padding block in bytes.
        - type_len_block_padding: The type of the length of the padding block.

    Returns:
        - The encrypted text.
    """
    
    try:
        original_symmetric_key = asymmetric.decrypt(symmetric_encrypt_key.stored_key, asymetric_key)
    
        logger.info("Encrypt text into hybrid tripleDes successful")
        return symmetric_encrypt_key.encrypt(text, original_symmetric_key, len_block_padding, type_len_block_padding)
    
    except Exception as e:
        logger.error(f"Encrypt text into hybridTripleDES error: {e}")


def decrypt_cipher(cipher: bytes, 
                   symmetric_encrypt_key: SymmetricTripleDES, 
                   asymetric_key: RSAPrivateKey, 
                   len_block_padding: int = DEFAULT_LEN_BYTES_PADDING_BLOCK_FOR_TRIPLEDES, 
                   type_len_block_padding: TypeArgument = TypeArgument.BYTE
                   ) -> bytes:
    
    """
    Decrypt a cipher using a hybrid encryption key pair.

    The cipher is decrypted using the TripleDES key, which is decrypted using the RSA private key.

    Args:
        - cipher: The cipher to decrypt.
        - symmetric_encrypt_key: The TripleDES key.
        - asymetric_key: The RSA private key.
        - len_block_padding: The length of the padding block in bytes.
        - type_len_block_padding: The type of the length of the padding block.

    Returns:
        - The decrypted text.
    """
    
    try:
        original_symmetric_key = asymmetric.decrypt(symmetric_encrypt_key.stored_key, asymetric_key)
    
        logger.info("Decrypt text into hybrid tripleDes successful")
        return symmetric_encrypt_key.decrypt(cipher, original_symmetric_key, len_block_padding, type_len_block_padding)
    
    except Exception as e:
        logger.error(f"Decrypt text for hybridTripleDES error: {e}")