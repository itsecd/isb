import logging
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from util import json_reader, txt_reader, txt_writer
logging.basicConfig(level=logging.INFO)

def create_dict(source_alphabet: str) -> dict:
    """
    Create a dictionary from the provided alphabet.
    :param source_alphabet: A string containing the source alphabet.
    :return: A dict mapping each letter to its index in the alphabet.
    """
    dict_alphabet = {}
    i = 0
    for letter in source_alphabet:
        dict_alphabet[letter] = i
        i += 1
    return dict_alphabet
def create_vigenere_table(source_alphabet: str) -> dict:
    """
    Create a Vigenère cipher table.
    :param source_alphabet: A string containing the alphabet.
    :return: A dict where each key is an index and each value is a list representing
             a shifted version of the alphabet starting from that index.
    """
    list_letter = list(source_alphabet)
    list_line = {}
    for i in range(32):
        list_line[i] = list_letter[i : i + 32 : 1] + list_letter[0:i]
    for i in range(len(source_alphabet)):
        list_line[i] = list_letter[i: i + len(source_alphabet): 1] + list_letter[0:i]
    return list_line

def encryption(source_alphabet: str, path_source_text: str, path_key: str, path_enc_text: str) -> None:
    """
    Encrypt a text file using the Vigenère cipher.
    :param path_source_text: Path to the file containing the source text to be encrypted.
    :param source_alphabet: A string containing the alphabet.
    :param path_key: Path to the file containing the encryption key.
    :param path_enc_text: Path to the file where the encrypted text will be saved.
    :return: None
    """
    text = txt_reader(path_source_text)
    key = txt_reader(path_key)
    text = "".join(text.split())
    key = (key * (len(text) // len(key) + 1))[: len(text)]
    dict_alphabet = create_dict(source_alphabet)
    table = create_vigenere_table(source_alphabet)
    new_text = ""
    for k, t in zip(key, text):
        new_text += table[dict_alphabet[k]][dict_alphabet[t]]
    txt_writer(path_enc_text, new_text)


def is_valid_decryption(source_alphabet: str, path_enc_text: str, path_source_text: str, path_key: str) -> bool:
    """
    Decrypt text and compare with input text
    :param path_key: Path to the file containing the encryption key.
    :param path_source_text: Path to the file containing the source text to be encrypted.
    :param source_alphabet: A string containing the alphabet.
    :param path_enc_text: Path to the file where the encrypted text saved.
    :return:
    """
    enc_text = list(txt_reader(path_enc_text))
    key = txt_reader(path_key)
    key = (key * (len(enc_text) // len(key) + 1))[: len(enc_text)]
    source_text = txt_reader(path_source_text)
    table = create_vigenere_table(source_alphabet)
    dict_alphabet = create_dict(source_alphabet)
    decrypted_text = ""
    for k, t in zip(key, enc_text):
        for symb in source_alphabet:
            if table[dict_alphabet[k]][dict_alphabet[symb]] == t:
                decrypted_text += symb

    return decrypted_text == source_text.replace(' ', '')


def main() -> None:
    alphabet: str = json_reader("constants.json")["alphabet"]
    paths: dict = json_reader(json_reader("constants.json")["paths"])

    encryption(alphabet,
               paths["input"], paths["key"], paths["encrypt"]
               )

    if is_valid_decryption(alphabet, paths["encrypt"], paths["input"], paths["key"]):
        logging.info('Text encrypted correctly')


if __name__ == "__main__":
    main()