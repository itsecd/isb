import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from work_w_files import serialize_private_and_public_keys

keys = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
private_key = keys
public_key = keys.public_key()
print(private_key)
print(type(public_key))
print(public_key)
serialize_private_and_public_keys(private_key,'private.pem',public_key,'public.pem')

def generate_symmetric_key():
    return os.urandom(16)


def seriliaze_key(path:str, key:str)-> None:
    with open(path,'wb') as file:
        file.write(key)


def deseriliaze_key(path:str) -> str:
    with open(path,'rw') as file:
        return file.read()

