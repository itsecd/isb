import logging
import os

from collections import Counter
from constants_for_decrypt import PATHS, ASSUMED_PURITY
from supportive import json_reader, file_reader, json_writer, file_writer

logging.basicConfig(level=logging.INFO)


def frequency(enc_text: str) -> list[list[str]]:
    """
    Calculates the frequency variations in the encrypted text.

    Args:
    enc_text (str): The encrypted text for frequency analysis.

    Returns:
    list[list[str]]: A list of variations in the frequencies of characters in the text.
    Each inner list contains the characters with the same frequency.
    """
    counter = Counter(enc_text)
    dict_pairs = counter.most_common()
    freq_variations = []
    
    for i in range(1, len(dict_pairs)):
        if dict_pairs[i - 1][1] == dict_pairs[i][1]:
            freq_variations.append([tup[0] for tup in dict_pairs])
            dict_pairs[i - 1], dict_pairs[i] = dict_pairs[i], dict_pairs[i - 1]
            freq_variations.append([tup[0] for tup in dict_pairs])

    return freq_variations


def decrypt_text(text_for_decrypt: str, arr_decrypt_letters: list[str]) -> str:
    """
    Decrypts a given text using a dictionary mapping of decryption letters.

    Parameters:
    - text_for_decrypt (str): The text to be decrypted.
    - arr_decrypt_letters (list[str]): A list of decryption letters.

    Returns:
    - str: The decrypted text.
    """
    arr_encrypt_text = []

    dictionary = dict(zip(arr_decrypt_letters, ASSUMED_PURITY))
    for symb in text_for_decrypt:
        arr_encrypt_text.append(dictionary[symb])
    text_for_decrypt = ''.join(arr_encrypt_text)
    return text_for_decrypt


def write_result(path_decrypt: str, path_key: str, path_input: str) -> None:
    """
    Writes the result of decrypting a text, the decryption key, and the key values to files.

    Parameters:
    - path_decrypt (str): The file path to write the decrypted text.
    - path_key (str): The file path to write the decryption key.
    - path_input (str): The file path of the input text to decrypt.

    Returns:
    - None
    """
    file_writer(path_decrypt,f'{decrypt_text(file_reader(path_input), frequency(file_reader(path_input))[-1])}\n', 'w')

    keys = dict(zip(list(frequency(file_reader(path_input))[-1]), ASSUMED_PURITY))

    dict_result = {"code": ','.join(keys.keys()), "key": ','.join(keys.values())}
    
    json_writer(path_key, dict_result)


if __name__ == "__main__":
    paths = json_reader(PATHS)
    try:
        write_result(os.path.join(paths["folder"], paths["decrypt"]),
                     os.path.join(paths["folder"], paths["key"]), os.path.join(paths["folder"], paths["input"]))
        logging.info(f"Text successfully decrypted and saved to file")
    except Exception as ex:
        logging.error(f"Error in decryption or file can't be open or was not found: {ex}\n")
