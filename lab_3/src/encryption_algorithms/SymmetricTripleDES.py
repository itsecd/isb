import os

from cryptography.hazmat.primitives import padding

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.ciphers.algorithms import TripleDES

from .TypeArgument import TypeArgument

from .consts import (
    KEY_COUNT_BITS_FOR_TRIPLEDES, 
    INIT_VECTOR_COUNT_BYTE_FOR_TRIPLEDES, 
    BLOCK_LEN_BITS_PADDING_FOR_TRIPLEDES, 
    DEFAULT_KEY_BYTES_FOR_TRIPLEDES, 
    DEFAULT_LEN_BYTES_PADDING_BLOCK_FOR_TRIPLEDES
)


class SymmetricTripleDES:

    """
    This class provides methods for symmetric encryption and decryption 
    using the TripleDES algorithm in CBC mode with ANSIX923 padding.

    Attributes:
        - padder: An object for padding the plaintext before encryption.
        - unpadder: An object for removing the padding from the ciphertext 
        after decryption.
        - encryptor: An object for encrypting the padded plaintext.
        - decryptor: An object for decrypting the ciphertext.
    """

    @staticmethod
    def generate_key(len_key: int = DEFAULT_KEY_BYTES_FOR_TRIPLEDES,
                     type_len: TypeArgument = TypeArgument.BYTE) -> bytes:
        """
        Generates a random encryption key for TripleDES.

        Args:
            - len_key(unsigned int): The length of the key in bits or bytes.
            - type_len(TypeArgument): The type of unit for the length of the 
            key (`BIT` or `BYTE`).

        Returns:
            - The encryption key as bytes.
        """

        try:
            if not len_key * type_len.bits in KEY_COUNT_BITS_FOR_TRIPLEDES:
                raise ValueError(
                    f"Count bits not value, your {len_key * type_len.bits} bits, need to {KEY_COUNT_BITS_FOR_TRIPLEDES}")

            return os.urandom(int(len_key * type_len.bytes))

        except Exception as e:
            raise ValueError(f"Generate key error: {e}")

    @staticmethod
    def generate_init_vector() -> bytes:
        """
        Generates a random initialization vector for TripleDES.

        Returns:
            - The initialization vector as bytes.
        """

        try:
            return os.urandom(INIT_VECTOR_COUNT_BYTE_FOR_TRIPLEDES)
        except Exception as e:
            raise ValueError(f"Generate init_vector error: {e}")

    def __init__(self, stored_key: bytes = None, init_vector: bytes = None):

        try:

            if not stored_key:
                stored_key = SymmetricTripleDES.generate_key()
            if not init_vector:
                init_vector = SymmetricTripleDES.generate_init_vector()

            self.__stored_key = stored_key
            self.__init_vector = init_vector

        except Exception as e:
            raise ValueError(f"Create object SymmetricTripleDES error: {e}")

    @property
    def stored_key(self) -> bytes:
        return self.__stored_key

    @property
    def init_vector(self) -> bytes:
        return self.__init_vector

    def encrypt(self,
                text: bytes,
                symmetrical_key: bytes,
                len_block_padding: int = DEFAULT_LEN_BYTES_PADDING_BLOCK_FOR_TRIPLEDES,
                type_len_block_padding: TypeArgument = TypeArgument.BYTE) -> bytes:
        """
        Encrypts the plaintext using TripleDES in CBC mode.

        Args:
            - text(bytes): The plaintext as bytes.
            - symmetrical_key(bytes): The encryption key as bytes.
            - len_block_padding(unsigned int): The length of the padding block
            in bits or bytes (default: DEFAULT_LEN_BYTES_PADDING_BLOCK_FOR_TRIPLEDES).
            - type_len_block_padding(TypeArgument): The type of unit for the 
            length of the padding block (`BIT` or `BYTE`) 
            (default: TypeArgument.BYTE).

        Returns:
            - The ciphertext as bytes.
        """

        try:
            if not len_block_padding * type_len_block_padding.bits in BLOCK_LEN_BITS_PADDING_FOR_TRIPLEDES:
                raise ValueError(
                    f"Block length is not suitable for this type of encryption, your {len_block_padding * type_len_block_padding.bits} bits, need to {BLOCK_LEN_BITS_PADDING_FOR_TRIPLEDES}")

            padder = padding.ANSIX923(
                int(len_block_padding * type_len_block_padding.bits)).padder()
            padded_text = padder.update(text) + padder.finalize()
            encryptor = Cipher(TripleDES(symmetrical_key),
                               CBC(self.init_vector)).encryptor()

            return encryptor.update(padded_text) + encryptor.finalize()

        except Exception as e:
            raise ValueError(f"Encrypt text symmetrical method error: {e}")

    def decrypt(self,
                cipher: bytes,
                symmetrical_key: bytes,
                len_block_padding: int = DEFAULT_LEN_BYTES_PADDING_BLOCK_FOR_TRIPLEDES,
                type_len_block_padding: TypeArgument = TypeArgument.BYTE) -> bytes:
        """
        Decrypts the ciphertext using TripleDES in CBC mode.

        Args:
            - cipher(bytes): The ciphertext as bytes.
            - symmetrical_key(bytes): The encryption key as bytes.
            - len_block_padding(unsigned int): The length of the padding 
            block in bits or bytes (default: DEFAULT_LEN_BYTES_PADDING_BLOCK_FOR_TRIPLEDES).
            - type_len_block_padding(TypeArgument): The type of unit for 
            the length of the padding block (`BIT` or `BYTE`) (default: TypeArgument.BYTE).

        Returns:
            - The plaintext as bytes.
        """

        try:
            if not len_block_padding * type_len_block_padding.bits in BLOCK_LEN_BITS_PADDING_FOR_TRIPLEDES:
                raise ValueError(
                    f"Block length is not suitable for this type of encryption, your {len_block_padding * type_len_block_padding.bits} bits, need to {BLOCK_LEN_BITS_PADDING_FOR_TRIPLEDES}")

            unpadder = padding.ANSIX923(
                int(len_block_padding * type_len_block_padding.bits)).unpadder()
            decryptor = Cipher(TripleDES(symmetrical_key),
                               CBC(self.init_vector)).decryptor()
            decrypt_text = decryptor.update(cipher) + decryptor.finalize()

            return unpadder.update(decrypt_text) + unpadder.finalize()

        except Exception as e:
            raise ValueError(f"Decrypt cipher symmetrical method error: {e}")
        