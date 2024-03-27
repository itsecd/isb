import enum
import logging

from cryptography.hazmat.primitives import asymmetric, hashes
from cryptography.hazmat.primitives.asymmetric import rsa

logging.basicConfig(level=logging.INFO)


class Action(enum.Enum):
    ENCRYPT = 1
    DECRYPT = 2


def encrypt_decrypt(
    key: rsa.RSAPublicKey, symmetric_key: bytes, param: Action
) -> bytes:
    """Encrypts or decrypts the symmetric key using the RSA public key.

    parametrs:
        key: The RSA public key.
        symmetric_key: The symmetric key to be encrypted or decrypted.
        param: The action to perform - encrypt or decrypt.

    return:
        bytes: The encrypted or decrypted data.
    """
    match param:
        case Action.ENCRYPT:
            data = key.encrypt(
                symmetric_key,
                asymmetric.padding.OAEP(
                    mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
        case Action.DECRYPT:
            data = key.decrypt(
                symmetric_key,
                asymmetric.padding.OAEP(
                    mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
        case _:
            logging.info(f"The parameter is not specified")
    return data
