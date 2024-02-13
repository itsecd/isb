import json
import logging
import os

from open_save_part import open_file, write_data, dict_save


logging.basicConfig(level=logging.INFO)

RUS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encryption(path: str, new_path: str, step: int) -> None:
    """Function takes path to the file to be encrypted,
    second path is path for save, and step with which
    the text will be encoded using the caesar cipher.
    parameters:
        path: path where the data file is located
        new_path: path where the encrypted text will be saved
        step: number with which the letters are shifted in alphabet
    """
    try:
        data = open_file(path)
        codding_str = ""
        for i in data:
            if i == " ":
                codding_str += i
                continue
            index = RUS.find(i)
            new_index = (index + step) % len(RUS)
            codding_str += RUS[new_index]
        write_data(new_path, codding_str)
    except Exception as ex:
        logging.error(f"The symbol was not found: {ex.message}\n{ex.args}\n")


def key_dict(path: str, step: int) -> None:
    """Function creates a dictionary-key for the Caesar cipher with a given step.
    parameters:
        path: path to file to write dictoinary
        step: number with which the letters are shifted in alphabet
    """
    try:
        key = dict()
        for i in RUS:
            index = RUS.find(i)
            key[i] = RUS[(index + step) % len(RUS)]
        dict_save(key, path)
    except Exception as ex:
        logging.error(f"The symbol was not found: {ex.message}\n{ex.args}\n")


def decryption(path: str, new_path: str, step: int) -> None:
    """Function takes path to the file to be decrypted,
    second path is path for save, and step with which
    the text will be decoded using the caesar cipher.
    parameters:
        path: path where the data file is located
        new_path: path where the decrypted text will be saved
        step: number with which the letters are shifted in alphabet
    """
    try:
        data = open_file(path)
        codding_str = ""
        for i in data:
            if i == " ":
                codding_str += i
                continue
            index = RUS.find(i)
            new_index = (index - step) % len(RUS)
            codding_str += RUS[new_index]
        write_data(new_path, codding_str)
    except Exception as ex:
        logging.error(f"The symbol was not found: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":

    with open(os.path.join("lab_1", "settings.json"), "r") as file:
        settings = json.load(file)

    encryption(
        os.path.join(
            settings["directory"], settings["folder1"], settings["given_text"]
        ),
        os.path.join(settings["directory"], settings["folder1"], settings["encryption"]),
        settings["step"],
    )
    key_dict(
        os.path.join(settings["directory"], settings["folder1"], settings["key_file"]),
        settings["step"],
    )
    decryption(
        os.path.join(settings["directory"], settings["folder1"], settings["encryption"]),
        os.path.join(settings["directory"], settings["folder1"], settings["decryption"]),
        settings["step"],
    )
