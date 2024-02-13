import json
import logging
import os

from open_save_part import open_file, write_data, dict_save


logging.basicConfig(level=logging.INFO)


def get_dict(path: str, new_path: str) -> None:
    """Function for doing frequency analysis in the text.
    parameters:
        path: path to read the text
        new_path: path for saving dictionary"""
    data = open_file(path)
    my_dict = dict()
    for i in data:
        my_dict[i] = data.count(i) / len(data)
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    dict_save(sorted_dict, new_path)


def decryption(old: str, new: str, data: str, path_for_dict: str, dict: dict) -> str:
    """Function replaces the specified letters in the text and fixes it in the dictionary.
    parameters:
        old: letter to replace
        new: new letter
        data: text
        path_for_dict:path for save dict
    returned value:
        data (str): decoded text
    """
    data = data.replace(old, new)
    dict[old] = new
    dict_save(dict, path_for_dict)
    return data


def utility(base_path: str, key_path: str, decoded_path: str) -> None:
    """Function parses the json file and replaces all key values
    in the text with values. Saves the received text to a file.
    parameters:
        base_path: path to read the encrypted text
        key_path: path to file to the dictionary with key
        decoded_path: path to write the decrypted text
    """
    try:
        data = open_file(base_path)
        with open(
            key_path,
            "r",
            encoding="utf-8",
        ) as file:
            dictionary = json.load(file)
        for key, value in dictionary.items():
            data = data.replace(key, value)
        write_data(decoded_path, data)
    except Exception as ex:
        logging.error(f"Failed to open dictionary: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":

    with open(os.path.join("lab_1", "settings.json"), "r") as file:
        settings = json.load(file)

    utility(
        os.path.join(
            settings["directory"], settings["folder2"], settings["original_text"]
        ),
        os.path.join(settings["directory"], settings["folder2"], settings["key_file"]),
        os.path.join(
            settings["directory"], settings["folder2"], settings["decryption"]
        ),
    )
