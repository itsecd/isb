import logging

from typing import Tuple

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from .encryption_algorithms import asymmetric
from .encryption_algorithms.TypeArgument import TypeArgument
from .encryption_algorithms.SymmetricTripleDES import SymmetricTripleDES

from .consts import DEFAULT_KEY_SIZE_ASYMMETRIC

logger = logging.getLogger(__name__)


def generate_hybrid_tripleDes(
    len_rsa_private_key: int = DEFAULT_KEY_SIZE_ASYMMETRIC,
    len_key_symmetrical: int = None,
    type_len_symmetrical: TypeArgument = TypeArgument.BYTE
    ) -> Tuple[SymmetricTripleDES, RSAPrivateKey]:
    """
    Generate a hybrid encryption key pair using TripleDES and RSA.

    The generated key pair consists of a TripleDES key encrypted with an RSA 
    private key.

    The RSA private key is used to decrypt the TripleDES key, which is then 
    used to encrypt and decrypt data.

    Args:
        - len_rsa_private_key: The length of the RSA private key in bits.
        - len_key_symmetrical: The length of the TripleDES key in bytes.
        - type_len_symmetrical: The type of the length of the TripleDES key.

    Returns:
        - A tuple containing the TripleDES key and the RSA private key.
    """

    try:
        
        if not len_key_symmetrical and type_len_symmetrical == TypeArgument.BIT:
            raise Exception("For default len key symmetrical use type " \
                            "argument BYTE")
        
        if len_key_symmetrical:
            key = SymmetricTripleDES.generate_key(len_key_symmetrical, 
                                                  type_len_symmetrical) 
        else:
            key = SymmetricTripleDES.generate_key()

        private_key = asymmetric.generate_private_key(
            key_size=len_rsa_private_key)
        encrypt_key = asymmetric.encrypt_with_public_key(
            key, private_key.public_key())

        logger.info("Generate hybrid tripleDes successful")
        return (SymmetricTripleDES(
                    stored_key=encrypt_key, 
                    init_vector=SymmetricTripleDES.generate_init_vector()),
                private_key)

    except Exception as e:
        logger.error(f"Generate hybrid tripleDes error: {e}")


def encrypt_text(text: bytes,
                 symmetric_encrypt_key: SymmetricTripleDES,
                 asymetric_key: RSAPrivateKey,
                 len_block_padding: int = None,
                 type_len_block_padding: TypeArgument = TypeArgument.BYTE
                 ) -> bytes:
    """
    Encrypt a text using a hybrid encryption key pair.

    The text is encrypted using the TripleDES key, which is decrypted using
    the RSA private key.

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
        if (not len_block_padding and 
            type_len_block_padding == TypeArgument.BIT):
            
            raise Exception("For default len block padding use type " \
                            "argument BYTE")
        
        original_symmetric_key = asymmetric.decrypt(
            symmetric_encrypt_key.stored_key,
            asymetric_key)

        if len_block_padding:
            encrypted_text = symmetric_encrypt_key.encrypt(
                text, original_symmetric_key, len_block_padding
            )
        else:
            encrypted_text = symmetric_encrypt_key.encrypt(
                text, 
                original_symmetric_key, 
                type_len_block_padding=type_len_block_padding
            )
        logger.info("Encrypt text into hybrid tripleDes successful")
        return encrypted_text

    except Exception as e:
        logger.error(f"Encrypt text into hybridTripleDES error: {e}")


def decrypt_cipher(cipher: bytes,
                   symmetric_encrypt_key: SymmetricTripleDES,
                   asymetric_key: RSAPrivateKey,
                   len_block_padding: int = None,
                   type_len_block_padding: TypeArgument = TypeArgument.BYTE
                   ) -> bytes:
    """
    Decrypt a cipher using a hybrid encryption key pair.

    The cipher is decrypted using the TripleDES key, which is decrypted using 
    the RSA private key.

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
        if not len_block_padding and type_len_block_padding == TypeArgument.BIT:
            raise Exception("For default len block padding use type argument BYTE")
        
        original_symmetric_key = asymmetric.decrypt(symmetric_encrypt_key.stored_key,
                                                    asymetric_key)

        if len_block_padding:
            decrypted_text = symmetric_encrypt_key.decrypt(
                cipher, original_symmetric_key, len_block_padding)
        else:
            decrypted_text = symmetric_encrypt_key.decrypt(
                cipher, 
                original_symmetric_key, 
                type_len_block_padding=type_len_block_padding)

        logger.info("Decrypt text into hybrid tripleDes successful")
        return decrypted_text

    except Exception as e:
        logger.error(f"Decrypt text for hybridTripleDES error: {e}")
        