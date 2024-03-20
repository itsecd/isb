import json
import logging
import os

from enum import Enum
from working_with_a_file import open_file, write_text, saving_values


logging.basicConfig(level=logging.INFO)

RUS = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class Action(Enum):
    """Класс для выбора опции работы с текстом"""
    ENCRYPTION = 0
    DECRYPTION = 1


def cipher_key(path: str, key_my: str) -> dict:
    """Осуществляет сохранение ключа от зашифрованного текста;
    path - файлу, в который пойдет запись 
    key_my - слово, которое используется в качестве ключа
    """
    try:
        key = dict()
        for i in range(len(key_my)):
            place = RUS.find(key_my[i])
            key[i] = place
        saving_values(key, path)
    except Exception as ex:
        logging.error(f"Data is not recognized: {ex.message}\n{ex.args}\n")
    return key


def encryption(path: str, new_path: str, key_my: dict, action: Action) -> None:
    """Осуществляет шифрование и дешифрование текста; 
    path - файлу с исходным текстом
    new_patth - путь к новому файлу, в который пойдет запись
    key_my - директорию, содержащую сдвиги, в соответвии с выбранным словом
    action - выбранная опция работы с текстом
    """
    try:
        data = open_file(path)
        cipher_str = ""
        for i in range(len(data)):
            if data[i] == " ":
                cipher_str += " " 
                continue
            match action:
                case Action.ENCRYPTION:
                    place = (RUS.find(data[i]) + key_my[i % len(key_my)]) % len(RUS)
                case Action.DECRYPTION:
                    place = (RUS.find(data[i]) - key_my[i % len(key_my)] + len(RUS)) % len(RUS)
                case _:
                    logging.error(
                        f"An invalid operation was entered: {ex.message}\n{ex.args}\n")
            cipher_str += RUS[place]
        write_text(new_path, cipher_str)
    except Exception as ex:
        logging.error(
            f"Data could not be encrypted: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":
    with open(os.path.join("lab_1", "settings.json"), "r", encoding="utf-8") as file:
        settings = json.load(file)
    with open(os.path.join("lab_1", "key.json"), "r", encoding="utf-8") as f:
        key = json.load(f)
    cipher_key = cipher_key(
        os.path.join(settings["directory"], settings["folder_1"], settings["cipher_key"]),
        key["key"],
    ) 
    encryption(
        os.path.join(settings["directory"], settings["folder_1"], settings["initial_text"]),
        os.path.join(settings["directory"], settings["folder_1"], settings["my_encrypted"]),
        cipher_key, Action.ENCRYPTION
    )
    encryption(
        os.path.join(settings["directory"], settings["folder_1"], settings["my_encrypted"]),
        os.path.join(settings["directory"], settings["folder_1"], settings["decrypted"]),
        cipher_key, Action.DECRYPTION
    )
