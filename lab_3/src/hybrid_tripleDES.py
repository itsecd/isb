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
    
    try:
        original_symmetric_key = asymmetric.decrypt(symmetric_encrypt_key.stored_key, asymetric_key)
    
        logger.info("Decrypt text into hybrid tripleDes successful")
        return symmetric_encrypt_key.decrypt(cipher, original_symmetric_key, len_block_padding, type_len_block_padding)
    
    except Exception as e:
        logger.error(f"Decrypt text for hybridTripleDES error: {e}")