import pickle
import logging

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

from .encryption_algorithms.SymmetricTripleDES import SymmetricTripleDES

logger = logging.getLogger(__name__)

def read_symmetricTripleDES(path_file: str) -> SymmetricTripleDES:

    """
    Reads a serialized SymmetricTripleDES object from a file.

    Args:
        - path_file (str): The path to the file containing the serialized SymmetricTripleDES object.

    Returns:
        - SymmetricTripleDES: The deserialized SymmetricTripleDES object.
    """
    try:
        with open(path_file, 'rb') as f:
            symmetricTripleDES: SymmetricTripleDES = pickle.load(f)
        
        logger.info(f"Read[{path_file}] SymmetricTripleDES successful")
        return symmetricTripleDES
    
    except Exception as e:
        logger.error(f"Read[{path_file}] SymmetricTripleDES error: {e}")
        
def safe_symmetricTripleDES(path_file: str, symmetricTripleDES: SymmetricTripleDES) -> None:

    """
    Safely serializes a SymmetricTripleDES object to a file.

    Args:
        - path_file (str): The path to the file to which the SymmetricTripleDES object should be serialized.
        - symmetricTripleDES (SymmetricTripleDES): The SymmetricTripleDES object to serialize.
    """
    try:
        with open(path_file, 'wb') as f:
            f.write(pickle.dumps(symmetricTripleDES))

        logger.info(f"Safe[{path_file}] SymmetricTripleDES successful")
    
    except Exception as e:
        logger.error(f"Safe[{path_file}] SymmetricTripleDES error: {e}")


def read_bytes(path_file: str) -> bytes:

    """
    Reads the contents of a file as bytes.

    Args:
        - path_file(str): The path to the file to read.

    Returns:
        - The contents of the file as bytes.
    """

    try:
        with open(path_file, mode='rb') as key_file:
            content = key_file.read()
        
        logger.info(f"Read[{path_file}] bytes successful")
        return content

    except Exception as e:
        logger.error(f"Read[{path_file}] bytes error: {e}")

def safe_bytes(path_file_safe: str, key: bytes) -> None:

    """
    Safely writes bytes to a file.

    Args:
        - path_file_safe(str): The path to the file to write to.
        - key(bytes): The bytes to write to the file.
    """

    try:
        with open(path_file_safe, 'wb') as key_file:
            key_file.write(key)
        
        logger.info(f"Safe[{path_file_safe}] bytes successful")
        
    except Exception as e:
        logger.error(f"Safe[{path_file_safe}] bytes error: {e}")

def safe_public_key(path_to_file_key: str, public_key: RSAPublicKey) -> None:

    """
    Safely writes a public key to a file.

    Args:
        - path_to_file_key(str): The path to the file to write to.
        - public_key(RSAPublicKey): The public key to write to the file.
    """

    try:
        with open(path_to_file_key, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                             format=serialization.PublicFormat.SubjectPublicKeyInfo))
        
        logger.info(f"Safe[{path_to_file_key}] RSA public key successful")
        
    except Exception as e:
        logger.error(f"Safe[{path_to_file_key}] RSA public key error: {e}")

def safe_private_key(path_to_file_key: str, private_key: RSAPrivateKey) -> None:

    """
    Safely writes a private key to a file.

    Args:
        - path_to_file_key(str): The path to the file to write to.
        - private_key(RSAPrivateKey): The private key to write to the file.
    """

    try:
        with open(path_to_file_key, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                              format=serialization.PrivateFormat.TraditionalOpenSSL,
                              encryption_algorithm=serialization.NoEncryption()))
          
        logger.info(f"Safe[{path_to_file_key}] RSA private key successful")    
            
    except Exception as e:
        logger.error(f"Safe[{path_to_file_key}] RSA private key error: {e}")

def read_public_key(path_to_file_key: str) -> RSAPublicKey:

    """
    Reads a public key from a file.

    Args:
        - path_to_file_key(str): The path to the file to read from.

    Returns:
        - The public key read from the file.
    """

    try:
        with open(path_to_file_key, 'rb') as public_key_file:
            public_bytes = public_key_file.read()
        
        logger.info(f"Read[{path_to_file_key}] RSA public key successful")           
        return load_pem_public_key(public_bytes)

    except Exception as e:
        logger.error(f"Read[{path_to_file_key}] RSA public key error: {e}")
        


def read_private_key(path_to_file_key: str) -> RSAPrivateKey:

    """
    Reads a private key from a file.

    Args:
        - path_to_file_key(str): The path to the file to read from.

    Returns:
        - The private key read from the file.
    """

    try: 
        with open(path_to_file_key, 'rb') as private_key_file:
            private_bytes = private_key_file.read()

        logger.info(f"Read[{path_to_file_key}] RSA private key successful")   
        return load_pem_private_key(private_bytes,password=None)

    except Exception as e:
        logger.error(f"Read[{path_to_file_key}] RSA private key error: {e}")