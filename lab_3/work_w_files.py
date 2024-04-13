from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
import logging
import json


def json_to_dict(path: str) -> dict:
    """
    make json to dict
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except BaseException as ex:
        logging.error(f'error in json_to_dict - {ex}')


def serialize_sym_key(path: str, key: str) -> None:
    """
    serialize symmetric key
    """
    try:
        with open(path, 'wb') as file:
            file.write(key)
    except BaseException as ex:
        logging.error(f'error in serialize_sym_key - {ex}')


def deserialize_sym_key(path: str) -> str:
    """
    deserialize symmetric key
    """
    try:
        with open(path, 'rb') as file:
            return file.read()
    except BaseException as ex:
        logging.error(f'error in deserialize_sym_key - {ex}')  


def serialize_private_and_public_keys(private: str, path_private: str, public: str, path_public: str) -> None:
    """
    serialize private and public keys

    params:
        private: private key 
        path_private: path to file for private key 
        public: public key 
        path_public: path to file with public key
    """
    try:
        with open(path_public, 'wb') as file:
            file.write(public.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except BaseException as ex:
        logging.error(f'error in serialize_public_key - {ex}')
    try:
        with open(path_private, 'wb') as file:
            file.write(private.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()))
    except BaseException as ex:
        logging.error(f'error in serialize_pivate_key - {ex}')


def deserialize_private_key(path_private: str) -> str:
    try:
        with open(path_private, 'rb') as file:
            return load_pem_private_key(file.read(),password=None,)
    except BaseException as ex:
        logging.error(f'error in deserialize_pivate_key - {ex}')


def deserialize_public_key(path_public: str) -> str:
    try:
        with open(path_public, 'rb') as file:
            return load_pem_public_key(file.read())
    except BaseException as ex:
        logging.error(f'error in deserialize_public_key - {ex}')
