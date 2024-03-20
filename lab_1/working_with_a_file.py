import json
import logging


logging.basicConfig(level=logging.INFO)


def open_file(path: str) -> str:
    """Осуществляет открытие файла 
    path - путь к файлу, необходимый для открытия
    """
    try:
        with open(path, "r+", encoding="utf-8") as file:   
            main = file.read()
        return main
    except Exception as ex:
        logging.error(f"Error opening the file: {ex.message}\n{ex.args}\n")


def write_text(path: str, data: str) -> None:
    """Осуществляет запись данных в файл 
    path - путь к файлу, в который пойдет запись
    data - данные для записи
    """
    try:
        with open(path, "w", encoding="utf-8") as file: 
            file.write(data)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n")


def saving_values(dict: dict, path: str) -> None:
    """Осуществляет сохранение данных в json-файл
    path - путь к файлу, в который пойдет запись
    dict - данные для записи
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(dict, ensure_ascii=False, indent=4))
    except Exception as ex:
        logging.error(f"An error occurred while saving: {ex.message}\n{ex.args}\n")
