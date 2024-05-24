import logging
import os

from lab_1 import read_json
from key_for_task2 import KEY
from constants import PATH


def frequency_analysis(text: str) -> list:
    """
    Функция считает частоту появления буквы в тексте(text).
    text - это сообщение, в котором мы считаем частоту встречаемости символов.
    Возвращает список, отсортированный по частоте в убывающем порядке.
    :param text: передаваемый тект (str)
    :return list:
    """
    dictonary_of_frequency = {}
    len_text = len(text)
    try:
        for letter in text:
            if (letter not in dictonary_of_frequency.keys()):
                frequency = text.count(letter) / len_text
                dictonary_of_frequency[letter] = frequency
            else:
                continue
        result = sorted(dictonary_of_frequency.items(), key=lambda x: x[1], reverse=True)
    except Exception as e:
        logging.error(f"Ошибка в функции frequency_analysis(text): не удалось вернуть список")
        raise
    else:
        return result


def read_file() -> str:
    """
    Функция считывает закодированное сообщение из файла.
    Возращает сообщение в виде строки(str).
    :return str:
    """
    absolute_path = os.path.abspath(os.getcwd())
    json_data = read_json.read_json_file(absolute_path + PATH)
    if json_data:
        folder = json_data.get("folder", "")
        path_from = json_data.get("path_from", "")
    if folder and path_from:
        try:
            path_to_file = absolute_path + folder + path_from
            with open(path_to_file, "r", encoding="utf-8") as file:
                message = file.read()
                lines = message.splitlines()
                result = ""
                for item in lines:
                    result += item
        except FileNotFoundError:
            print("Файл не найден.")
        else:
            return result


if __name__ == "__main__":
    message = read_file()
    print(message)
    dictonary1 = frequency_analysis(message)
    print(dictonary1)

    for letter in KEY:
        message = message.replace(KEY[letter], letter)

    print(message)