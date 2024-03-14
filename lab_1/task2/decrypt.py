import logging
import os

from collections import Counter
from constants import arr_encrypt_letters, PATHS
from lab_1.task1.json_read import json_reader

logging.basicConfig(level=logging.INFO)


def input_text(path_input: str) -> str:
    """
    Read encrypted text from txt file
    :param path_input:
    :return:
    """
    try:
        with open(path_input, 'r', encoding='utf-8') as f_input:
            return f_input.read()
    except Exception as ex:
        logging.error(f"File can't be open or was not found: {ex}\n")


def frequency(enc_text: str) -> list[list[str]]:
    """
    Returns list of different variations counts of letters in descending order

    :param enc_text:
    :return:
    """
    c = Counter(enc_text)
    dict_pairs = c.most_common()
    freq_variations = []
    for i in range(1, len(dict_pairs)):
        if dict_pairs[i - 1][1] == dict_pairs[i][1]:
            freq_variations.append([tup[0] for tup in dict_pairs])
            tmp = dict_pairs[i - 1]
            dict_pairs[i - 1] = dict_pairs[i]
            dict_pairs[i] = tmp
            freq_variations.append([tup[0] for tup in dict_pairs])

    return freq_variations


def decrypt_text(text_for_decrypt: str, arr_decrypt_letters: list[str]) -> str:
    """
    Decrypt text using frequency analysis algorithm

    :param text_for_decrypt:
    :param arr_decrypt_letters:
    :return:
    """
    arr_encrypt_text = []

    dictionary = dict(zip(arr_decrypt_letters, arr_encrypt_letters))
    for symb in text_for_decrypt:
        arr_encrypt_text.append(dictionary[symb])
    text_for_decrypt = ''.join(arr_encrypt_text)
    return text_for_decrypt


def write_result(path_decrypt: str, path_key: str, path_input: str) -> None:
    """
    Write decrypted text and keys in file
    :param path_input:
    :param path_key:
    :param path_decrypt:
    :return:
    """
    try:
        with open(path_decrypt, 'w', encoding='utf-8') as f_decrypt:
            f_decrypt.write(f'{decrypt_text(input_text(path_input), frequency(input_text(path_input))[-1])}\n')

        with open(path_key, 'w', encoding='utf-8') as f_key:
            keys = dict(zip(list(frequency(input_text(path_input))[-1]), arr_encrypt_letters))
            f_key.write(f"code: {' '.join(keys.keys())}\n")
            f_key.write(f" key: {' '.join(keys.values())}")
    except Exception as ex:
        logging.error(f"Error in decryption or file can't be open or was not found: {ex}\n")


if __name__ == "__main__":
    paths = json_reader(PATHS)
    try:
        write_result(os.path.join(paths["folder"], paths["decrypt"]),
                     os.path.join(paths["folder"], paths["key"]), os.path.join(paths["folder"], paths["input"]))
        logging.info(f"Text successfully decrypted and saved to file")
    except Exception as ex:
        logging.error(f"Error in decryption or file can't be open or was not found: {ex}\n")
