import json
import logging
import os

from working_with_a_file import open_file, write_text, saving_values


logging.basicConfig(level=logging.INFO)


def text_analysis(path: str, new_path: str) -> None:
    """Осуществляет анализ зашифрованного текста;
    path - файлу с исходным текстом
    new_patth - путь к новому файлу, в который пойдет запись
    """
    try:
        text = open_file(path)
        dict_my = {}
        for i in text:
            dict_my[i] = dict_my.get(i, 0) + 1
        dict_my = {k: (v/len(text)) for k, v in dict_my.items()}
        sort = dict(sorted(dict_my.items(), key=lambda x: x[1], reverse=True))
        saving_values(sort, new_path)
    except Exception as ex:
        logging.error(f"The directory could not be opened: {ex.message}\n{ex.args}\n")


def decryption(path: str, new_path: str, key: str) -> None:
    """Осуществляет расшифровку исходного текста; 
    path - файлу с исходным текстом
    new_patth - путь к новому файлу, в который пойдет запись
    key - путь к файлу, в котором хранится ключ шифрования
    """
    try:
        text = open_file(path)
        with open(key, "r", encoding="utf-8") as file:
            dict_my = json.load(file)
        result = "".join(dict_my.get(letter, letter) for letter in text) 
        write_text(new_path, result)
    except Exception as ex:
        logging.error(f"The directory could not be opened: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":
    with open(os.path.join("lab_1", "settings.json"), "r") as file:
        settings = json.load(file)
    text_analysis(
        os.path.join(settings["directory"], settings["folder_2"], settings["code_text"]),
        os.path.join(settings["directory"], settings["folder_2"], settings["text_analysis"]),
    )
    decryption(
        os.path.join(settings["directory"], settings["folder_2"], settings["code_text"]),
        os.path.join(settings["directory"], settings["folder_2"], settings["decrypted"]),
        os.path.join(settings["directory"], settings["folder_2"], settings["cipher_key"]),
    ) 