import os
import logging

from lab_1 import read_json
from key_for_task1 import KEY
from constant import PATH, SIGNS


def get_i_j(letter: str) -> tuple:
    """
    Функция возращает индекс строки и столбца буквы параметра letter.
    Параметр letter сравнивается с буквами из матрицы букв.
    Возвращает неизменяемый список(tuple) вида (i, j), где i - индекс строки, а j - индекс столбца.
    :param letter: буква (str)
    :return tuple:
    """
    try:
        for i in range(0, len(KEY)):
            if letter in KEY[i]:
                j = KEY[i].index(letter)
                if (letter == KEY[i][j]):
                    return i, j
    except Exception as e:
        logging.error(f"Ошибка в функции get_i_j(letter): {e}")
        raise


def encryption(message: str) -> str:
    """
    Функция шифрует переданное сообщение message согласно "квадрату Полибия".
    message переводится в нижний регистр, а затем каждая буква из message штфруется согласно "квадрату Полибия".
    Возвращает результат в виде строки(str).
    :param message: переданное сообщение (str)
    :return str:
    """
    message = message.lower()
    result = ""
    try:
        for letter in message:
            if (letter in SIGNS):
                result += letter
            else:
                place_of_letter = get_i_j(letter)
                if place_of_letter != None:
                    result += str(place_of_letter)
        return result
    except Exception as e:
        logging.error(f"Ошибка в функции encryption(message): {e}")


def message_encryption(file_name: str) -> str:
    """
    Функция  считывает сообщение из файла с именем file_name, затем шифрует его
    и возращает результат в виде строки(str).
    file_name нужен, чтобы открыть файл с сообщением, считать и зашифровать его.
    :param file_name: имя файла (str)
    :return str:
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            message = file.read()
            encrypted_text = encryption(message)
            return encrypted_text
    except FileNotFoundError:
        print("Файл не найден.")


def save_message(file_name: str, message) -> None:
    """
    Функция сохраняет сообщение(message) в указанный файл с именем file_name с перезаписыванием содержимого.
    Создает файл с именем file_name, если такого нет.
    file_name нужен, чтобы открыть файл для записи сообщения.
    Функция ничего не возвращает.
    :param file_name: имя файла (str)
    :param message: переданное сообщение (str)
    :return None:
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(message)
    except Exception as e:
        logging.error(f"Ошибка в функции get_i_j(letter): {e}")
        raise


def main() -> None:
    """
    Функция считывает сообщение из файла, шифрует его и записывает в новый файл, заданным пользователем.
    Функция ничего не возвращает.
    :param :
    :return None:
    """
    absolute_path = os.path.abspath(os.getcwd())
    json_data = read_json.read_json_file(absolute_path + PATH)
    if json_data:
        folder = json_data.get("folder", "")
        path_from = json_data.get("path_from", "")
        path_to = json_data.get("path_to", "")
    if folder and path_from and path_to:
        try:
            encrypted_text = message_encryption(absolute_path + folder + path_from)
            save_message(absolute_path + folder + path_to, encrypted_text)
            print("Текст успешно зашифрован и сохранен в файле.")
        except Exception as e:
            print(f"Произошла ошибка в функции send_encryption_text: {e}")


if __name__ == "__main__":
    main()