import logging

from SymmetricCryptography import SymmetricCryptography
from AsymmetricCryptography import AsymmetricCryptography
from CryptoUtility import CryptoUtility

logging.basicConfig(level=logging.INFO)

class HybridEncryption:
    """
    A class for hybrid encryption using both symmetric and asymmetric keys.
    """
    def __init__(self, text_path: str, symmetric_key_path: str,
                 encrypted_text_path: str, decrypted_text_path: str,
                 symmetric_crypto: SymmetricCryptography, asymmetric_crypto: AsymmetricCryptography) -> None:
        """
        Initialize HybridEncryption object with necessary paths and key length.

        :param text_path: Path to the text file.
        :param symmetric_key_path: Path to the symmetric key file.
        :param encrypted_text_path: Path to store the encrypted text.
        :param decrypted_text_path: Path to store the decrypted text.
        :param symmetric_crypto: An instance of a class for working with symmetric cryptography.
        :param asymmetric_crypto: An instance of a class for working with asymmetric cryptography.
        """
        self.text_path = text_path
        self.symmetric_key_path = symmetric_key_path
        self.encrypted_text_path = encrypted_text_path
        self.decrypted_text_path = decrypted_text_path
        self.symmetric_crypto = symmetric_crypto
        self.asymmetric_crypto = asymmetric_crypto


    def generate_keys(self) -> None:
        """
        Generate asymmetric and symmetric keys and write them to files.
        """
        try:
            symmetric_key = self.symmetric_crypto.generate_key()
            private_key, public_key = self.asymmetric_crypto.generate_key_pair(2048)

            self.asymmetric_crypto.serialize_private_key(private_key)
            self.asymmetric_crypto.serialize_public_key(public_key)

            encrypted_symmetric_key = self.asymmetric_crypto.encrypt_with_public_key(public_key, symmetric_key)
            CryptoUtility.serialize_key(encrypted_symmetric_key, f"{self.symmetric_key_path[:-4]}_{self.symmetric_crypto.key_len}.txt")

            logging.info("Keys successfully generated and written to files.")
        except Exception as ex:
            logging.error(f"An error occurred while generating the keys: {ex}")


    def encrypt_text(self) -> None:
        """
        Encrypt the text using the generated symmetric key and write it to a file.
        """
        try:
            symmetric_key = CryptoUtility.deserialize_key(f"{self.symmetric_key_path[:-4]}_{self.symmetric_crypto.key_len}.txt")
            symmetric_key = self.asymmetric_crypto.decrypt_with_private_key(self.asymmetric_crypto.deserialize_private_key(),symmetric_key)
            plaintext = bytes(CryptoUtility.read_text_file(self.text_path,"r","UTF-8"),"UTF-8")
            encrypted_text = self.symmetric_crypto.encrypt_text(symmetric_key, plaintext)
            CryptoUtility.write_text_file(encrypted_text, self.encrypted_text_path)
            logging.info("Text successfully encrypted and written to file.")
        except Exception as ex:
            logging.error(f"An error occurred while encrypting the text: {ex}")


    def decrypt_text(self) -> None:
        """
        Decrypt the text using the generated symmetric key and write it to a file.
        """
        try:
            symmetric_key = CryptoUtility.deserialize_key(f"{self.symmetric_key_path[:-4]}_{self.symmetric_crypto.key_len}.txt")
            symmetric_key = self.asymmetric_crypto.decrypt_with_private_key(self.asymmetric_crypto.deserialize_private_key(),symmetric_key)
            encrypted_text = bytes(CryptoUtility.read_text_file(self.encrypted_text_path,"rb"))
            decrypted_text = self.symmetric_crypto.decrypt_text(symmetric_key, encrypted_text)
            CryptoUtility.write_text_file(decrypted_text, self.decrypted_text_path)
            logging.info("Text successfully decrypted and written to file.")
        except Exception as ex:
            logging.error(f"An error occurred while decrypting the text: {ex}")