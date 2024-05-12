from asymmetrical_cr import AsymmetricalCryptograpy
from symmerical_cr import SymmetricCryptography


class CriptoSystem:
    def __init__(self):
        self.private_key, self.public_key = AsymmetricalCryptograpy.generate_asymmetric_keys()
        self.symmetric_key = SymmetricCryptography.generate_symmetric_key()

    def generate_keys(self, path_public_key: str, path_private_key: str, path_symmetric_key: str) -> None:
        AsymmetricalCryptograpy.serialize_private_and_public_keys(self.private_key,
                                                                  path_private_key,
                                                                  self.public_key,
                                                                  path_public_key)
        SymmetricCryptography.serialize_sym_key(path_symmetric_key,
                                                AsymmetricalCryptograpy.encrypt_with_public_key(
                                                    self.public_key,
                                                    self.symmetric_key)
                                                )
