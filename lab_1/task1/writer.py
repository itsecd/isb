import logging

from caesar import caesar_encrypt
from route import route_transposition
from reader import txt_reader

logging.basicConfig(level=logging.INFO)


def write_caesar(path : str, key : int, path_encrypt: str, path_key: str) -> None:
    """Encrypts by Caesar method and writes str and key into files.
    :param path: path to txt file that is needed to encrypt
    :param key: key for Caesar method
    :param path_encrypt: path for writing encrypted text
    :param path_key: path for writing keyword for encrypted text
    :return:
    """
    try:
        encrypted_text = caesar_encrypt(txt_reader(path), key)
        with open(path_encrypt, 'w', encoding='utf-8') as encrypt_file:
            encrypt_file.write(encrypted_text)
        with open(path_key, 'w', encoding='utf-8') as key_file:
            key_file.write(f'KEY: {key}')
        logging.info(f"Successfully encrypted and saved")
    except Exception as exc:
        logging.error(f'Saving error: {exc}\n')

def write_route(path : str, keyword : str, path_encrypt: str, path_key: str) -> None:
    """Encrypts by route transposition method and writes str and key into files.
    :param path: path to txt file that is needed to encrypt
    :param keyword: keyword for route transposition method
    :param path_encrypt: path for writing encrypted text
    :param path_key: path for writing keyword for encrypted text
    :return:
    """
    try:
        encrypted_text = route_transposition(txt_reader(path), keyword)
        with open(path_encrypt, 'w', encoding='utf-8') as encrypt_file:
            encrypt_file.write(encrypted_text)
        with open(path_key, 'w', encoding='utf-8') as key_file:
            key_file.write(f'KEY: {keyword}')
        logging.info(f"Successfully encrypted and saved")
    except Exception as exc:
        logging.error(f'Saving error: {exc}\n')