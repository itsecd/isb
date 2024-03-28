import os
import json
import logging
from constants import path, signs
import key_for_task1 as key
import read_json


def get_i_j(letter: str) -> tuple:
    """
    Функция возращает индекс строки и столбца буквы из матрицы укв.
    :param letter:
    :return tuple:
    """
    try:
        for i in range(0, len(key.matrix_of_letter)):
            for j in range(0, len(key.matrix_of_letter[0])):
                if (letter == key.matrix_of_letter[i][j]):
                    return i, j
    except Exception as e:
        logging.error(f"Ошибка в функции get_i_j(letter): {e}")


def encryption(message: str) -> str:
    """
    Функция шифрует переданное сообщение согласно "квадрату Полибия".
    :param message:
    :return str:
    """
    message = message.lower()
    result = ""
    try:
        for letter in message:
            if (letter in signs):
                result += letter
            else:
                place_of_letter = get_i_j(letter)
                result += str(place_of_letter)
        return result
    except Exception as e:
        logging.error(f"Ошибка в функции encryption(message): {e}")


def send_encryption_text() -> None:
    """
    Функция считывает сообщение из переданного пользователем файла, шифрует его и записывает в новый файл, заданным пользователем.
    :param :
    :return None:
    """
    try:
        json_data = read_json.read_json_file(path)

        if json_data:
            folder = json_data.get("folder", "")
            path_from = json_data.get("path_from", "")
            path_to = json_data.get("path_to", "")

        if folder and path_from and path_to:
            try:
                with open(f"{path_from}", "r", encoding="utf-8") as file:
                    message = file.read()
                    encrypted_text = encryption(message)

                with open(f"{path_to}", "w", encoding="utf-8") as file:
                    file.write(encrypted_text)

                print("Текст успешно зашифрован и сохранен в файле.")

            except FileNotFoundError:
                print("Один из файлов не найден.")

            except Exception as e:
                print(f"Произошла ошибка в функции send_encryption_text: {e}")

    except Exception as e:
        print(f"Произошла ошибка в функции send_encryption_text: {e}")


if __name__ == "__main__":
    send_encryption_text()
