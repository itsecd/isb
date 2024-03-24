from task1 import cipher
from works_files import *


def frequency_analysis(text_p: str, path: str) -> None:
    """
    Performs a frequency analysis of the text and writes it to the dictionary in another file

    Parameters
        text_path: the path to the file with the text to analyze
        path: the path to the file where the frequency analysis will be recorded
    """
    text = read_files(text_p)
    frequencies = {}
    total = len(text)
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    for char, count in frequencies.items():
        frequencies[char] = count / total
    sort = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
    write_json(sort, path)


def key_json(freq_p: str, path: str, data_p: str) -> None:
    """
    Create a key to the text based on statistical analysis of
    the text and data on frequently encountered characters and write
    it to a json file in the form of a dictionary

    Parameters
        freq_path: the path from which text statistical analysis data is taken
        paths: the path where the key will be written
        data_path: the path from which character data is taken
    """
    key = read_json(freq_p)
    result = {}
    alf = read_json(data_p)

    for key_char, value_char in zip(key.keys(), alf.values()):
        result[key_char] = value_char
        found_key = None
        for k, v in alf.items():
            if v == value_char:
                found_key = k
                break
        result[key_char] = found_key
    write_json(result, path)


if __name__ == "__main__":
    try:
        config = read_json("config.json")
        text_path = config["text_path_task2"]
        freq_path = config["key_freq_path_task2"]
        key_path = config["key_path_task2"]
        data_path = config["data_path_task2"]
        decryption_key_path = config["text_key_path_task2"]
        decryption_path = config["decryption_path_task2"]
        text_decryption_path = config["text_decryption_path_task2"]

        frequency_analysis(text_path, freq_path)
        key_json(freq_path, key_path, data_path)
        cipher(Mode.ENCRYPT, key_path, text_path, decryption_path)
        cipher(Mode.ENCRYPT, decryption_key_path, text_path, text_decryption_path)
    except Exception as e:
        print(f"An error occurred: {e}")
