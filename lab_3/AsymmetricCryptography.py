from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

class AsymmetricCryptography:
    """
    A class for asymmetric cryptography operations.

    This class provides methods for generating key pairs,
    encrypting and decrypting data using asymmetric encryption algorithms.

    Attributes:
        None
    """
    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        """
        Initialize AsymmetricCryptography object with public and private key paths.

        :param private_key_path: Path to the private key file.
        :param public_key_path: Path to the public key file.
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path
        
        
    def generate_key_pair(self, key_size: int) -> tuple:
        """
        Generate an RSA key pair.

        :param key_size: The size of the RSA key in bits.

        :return: A tuple containing the private and public keys.
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key = private_key.public_key()
        return private_key, public_key


    def serialize_private_key(self, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serialize the private key and save it to a file.

        :param private_key: The private key.
        """
        with open(self.private_key_path, 'wb') as key_file:
            key_file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                     encryption_algorithm=serialization.NoEncryption()))


    def serialize_public_key(self, public_key: rsa.RSAPublicKey) -> None:
        """
        Serialize the public key and save it to a file.

        :param public_key: The public key.
        """
        with open(self.public_key_path, 'wb') as key_file:
            key_file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                    format=serialization.PublicFormat.SubjectPublicKeyInfo))


    def deserialize_private_key(self) -> rsa.RSAPrivateKey:
        """
        Deserialize the private key and return it.
        
        :return: The deserialized private key.
        """
        with open(self.private_key_path, 'rb') as key_file:
            return serialization.load_pem_private_key(key_file.read(), password=None)


    def deserialize_public_key(self) -> rsa.RSAPublicKey:
        """
        Deserialize the public key and return it.
        
        :return: The deserialized public key.
        """
        with open(self.public_key_path, 'rb') as key_file:
            return serialization.load_pem_public_key(key_file.read())


    def encrypt_with_public_key(self, public_key: rsa.RSAPublicKey, text: bytes) -> bytes:
        """
        Encrypts ntext using the provided public key.

        :param public_key: The RSA public key used for encryption.
        :param text: The text to be encrypted.

        :return: The ciphertext produced by the encryption process.
        """
        return public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                          algorithm=hashes.SHA256(), label=None))


    def decrypt_with_private_key(self, private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
        """
        Decrypts ciphertext using the provided private key.

        :param private_key: The RSA private key used for decryption.
        :param ciphertext: The ciphertext to be decrypted.

        :return: The text produced by the decryption process.
        """
        return private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                            algorithm=hashes.SHA256(), label=None))