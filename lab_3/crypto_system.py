from asymmetrical_cr import AsymmetricalCryptograpy
from symmerical_cr import SymmetricCryptography
from work_w_files import write_bytes, write_file, read_bytes


class CriptoSystem:
    """class provides the ability to work with hybrid crypto system"""
    def __init__(self):
        self.private_key, self.public_key = AsymmetricalCryptograpy.generate_asymmetric_keys()
        self.symmetric_key = SymmetricCryptography.generate_symmetric_key()

    def generate_keys(self, path_public_key: str, path_private_key: str, path_symmetric_key: str) -> None:
        """generates the private, public keys and symmetric keys and serializes them"""
        AsymmetricalCryptograpy.serialize_private_and_public_keys(self.private_key,
                                                                  path_private_key,
                                                                  self.public_key,
                                                                  path_public_key)
        SymmetricCryptography.serialize_sym_key(path_symmetric_key,
                                                AsymmetricalCryptograpy.encrypt_with_public_key(
                                                    self.public_key,
                                                    self.symmetric_key)
                                                )

    @staticmethod
    def encrypt_text(path_text: str, path_private_key: str,
                     path_symmetric_key: str, path_encrypted_text: str) -> None:
        """decrypts symmetric key and encrypts text"""
        private_key = AsymmetricalCryptograpy.deserialize_private_key(path_private_key)
        encrypted_symmetric_key = SymmetricCryptography.deserialize_sym_key(path_symmetric_key)
        symmetric_key = AsymmetricalCryptograpy.decrypt_with_private_key(private_key, encrypted_symmetric_key)
        encrypted_text = SymmetricCryptography.encrypt(symmetric_key,
                                                       read_bytes(path_text))
        write_bytes(path_encrypted_text, encrypted_text)

    @staticmethod
    def decrypt_text(path_encrypted_text: str, path_symmetric_key: str,
                     path_private_key: str, path_decrypted_text: str) -> None:
        """decrypts symmetric key and decrypts text"""
        private_key = AsymmetricalCryptograpy.deserialize_private_key(path_private_key)
        encrypted_symmetric_key = SymmetricCryptography.deserialize_sym_key(path_symmetric_key)
        symmetric_key = AsymmetricalCryptograpy.decrypt_with_private_key(private_key, encrypted_symmetric_key)
        decrypted_text = SymmetricCryptography.decrypt(symmetric_key, path_encrypted_text)
        write_file(path_decrypted_text, decrypted_text)
