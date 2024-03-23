import json
import logging
import os
import re

from enum import Enum
from files import read_file, write_file, formatting_text, get_dict


logging.basicConfig(filename="lab_1/report.log", filemode="a", level=logging.INFO)


class Mode(Enum):
    """
    The class contains modes for encryption and decryption

    Modes:
        True - encryption
        False - decryption
    """
    ENCRYPTION = 1
    DECRYPTION = 0


def get_key(keyword: str, alphabet: str, path: str) -> dict:
    """
    The function receives a word, each letter
    of which is replaced by the corresponding
    number in the table

    Args:
        keyword (str): accepts a keyword
        alphabet (str): alphabet for creating a key
        path (str): path to store the dictionary

    Returns:
        dict: the dictionary representing the generated key
    """
    try:
        key = {}
        for i, char in enumerate(keyword):
            key[i] = alphabet.index(char)
        get_dict(key, path)
        logging.info("func get_key work")
    except Exception as e:
        logging.error(f"key problems {e}")
    return key


def vigenere_chipher(
    path: str, new_path: str, alphabet: str, key: dict, mode: Mode
) -> str:
    """
    Encryption and decryption function using Vigenere method

    Args:
        path (str): reading a file along the path
        new_path (str): path for the result file
        alphabet (str): alphabet for encryption and decryption
        key (dict): dictionary with key for encryption and decryption
        mode (Mode): shows the operating mode of the function

    Returns:
        str: The encrypted or decrypted text
    """
    text = read_file(path)
    chipher = ""
    try:
        for i, char in enumerate(text):
            if char in alphabet:
                char_idx = alphabet.index(char)
                keyword_idx = i % len(key)
                shift = key[keyword_idx]
                match mode:
                    case Mode.ENCRYPTION:
                        chipher_idx = (char_idx + shift) % len(alphabet)
                    case Mode.DECRYPTION:
                        chipher_idx = (char_idx - shift) % len(alphabet)
                    case _:
                        logging.error("mode not selected")
                chipher_char = alphabet[chipher_idx]
                chipher += chipher_char
            else:
                chipher += char
        logging.info(f"func vigenere_chipher work mode:{mode}")
    except Exception as e:
        logging.error(f"error in enc/decr {e}")
    write_file(new_path, chipher)
    return chipher


if __name__ == "__main__":
    with open(os.path.join("lab_1", "settings.json"), "r", encoding="utf-8") as json_f:
        settings = json.load(json_f)
    key = get_key(
        settings["keyword"],
        settings["alphabet"],
        os.path.join(settings["dir"], settings["keyword_dict"]),
    )
    vigenere_chipher(
        (os.path.join(settings["dir"], settings["txt"])),
        os.path.join(settings["dir"], settings["encryption"]),
        settings["alphabet"],
        key,
        Mode.ENCRYPTION,
    )
    vigenere_chipher(
        (os.path.join(settings["dir"], settings["encryption"])),
        os.path.join(settings["dir"], settings["decryption"]),
        settings["alphabet"],
        key,
        Mode.DECRYPTION,
    )
