import logging
import os
import sys


from constants import ALPHABET, PATHS

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from util import json_reader, txt_reader, txt_writer

logging.basicConfig(level=logging.INFO)



def create_dict(sourse_alphabet: str) -> dict:
    """
    Create a dictionary from the provided alphabet.

    :param source_alphabet: A string containing the source alphabet.
    :return: A dict mapping each letter to its index in the alphabet.
    """
    dict_alphabet = {}
    i = 0
    for letter in sourse_alphabet:
        dict_alphabet[letter] = i
        i += 1
    return dict_alphabet


def create_vigenere_table(sourse_alphabet: str) -> dict:
    """
    Create a Vigenère cipher table.

    :param source_alphabet: A string containing the alphabet.
    :return: A dict where each key is an index and each value is a list representing
             a shifted version of the alphabet starting from that index.
    """
    list_letter = list(sourse_alphabet)
    list_line = {}
    for i in range(32):
        list_line[i] = list_letter[i : i + 32 : 1] + list_letter[0:i]
    return list_line


def encryption(path_sourse_text: str, path_key: str, path_enc_text: str) -> None:
    """
    Encrypt a text file using the Vigenère cipher.

    :param path_source_text: Path to the file containing the source text to be encrypted.
    :param path_key: Path to the file containing the encryption key.
    :param path_encrypted_text: Path to the file where the encrypted text will be saved.
    :return: None
    """
    text = txt_reader(path_sourse_text)
    key = txt_reader(path_key)
    text = "".join(text.split())
    key = (key * (len(text) // len(key) + 1))[: len(text)]
    dict_alphabet = create_dict(ALPHABET)
    table = create_vigenere_table(ALPHABET)
    new_text = ""
    for k, t in zip(key, text):
        new_text += table[dict_alphabet[k]][dict_alphabet[t]]
    txt_writer(path_enc_text, new_text)


def main() -> None:
    paths = json_reader(PATHS)
    encryption(
        paths["input"], paths["key"], paths["encrypt"]
    )


if __name__ == "__main__":
    main()

