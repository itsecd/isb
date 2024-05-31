from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

from algoritms.serialization import Serialization
from algoritms.functional import Functional


class Asymmetric:
    @staticmethod
    def key_generation() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """generate asymmetric key

        Returns:
            tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]: public and private keys
        """
        key_pair = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        return key_pair.public_key(), key_pair

    @staticmethod
    def encryption(
            path_to_public: str,
            path_to_symmetric_origin: str,
            path_to_symmetric_encripted: str,
    ) -> None:
        """Symmetric key encription by asymmetric key

        Args:
            path_to_public (str): path to file with public asymmetric key
            path_to_symmetric_origin (str): path to file with original symmetric key
            path_to_symmetric_encripted (str): path to save encripted symmetric key
        """
        symmetric_key = Serialization.symmetric_key_deserialization(
            path_to_symmetric_origin
        )
        public_key = Serialization.public_key_deserialization(path_to_public)
        encripted_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        Functional.write_file_bytes(path_to_symmetric_encripted, encripted_key)

    @staticmethod
    def decryption(
            path_to_private: str,
            path_to_symmetric_encripted: str,
            path_to_symmetric_decripted: str,
    ) -> bytes:
        """Symmetric key decription by asymmetric key

        Args:
            path_to_private (str): path to private key
            path_to_symmetric_encripted (str): path to file with encrypted symmetric key
            path_to_symmetric_decripted (str): path to file with decrypted symmetric key

        Returns:
            bytes: decrypted key
        """
        symmetric_encripted = Serialization.symmetric_key_deserialization(
            path_to_symmetric_encripted
        )
        private_key = Serialization.private_key_deserialization(path_to_private)
        decripted_key = private_key.decrypt(
            symmetric_encripted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        Serialization.symmetric_key_serialization(
            path_to_symmetric_decripted, decripted_key
        )
        return decripted_key
