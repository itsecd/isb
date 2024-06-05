import json
import logging

def writing_to_json(data: str, path: str)->None:
    """
    Запись данных в формате JSON в файл.

    Params:
    data (str): Данные должны быть записаны в формате JSON.
    path (str): Путь к файлу, в который будут записаны данные.
    """
    try:
        with open(path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        logging.error(f'[writing_to_json]: {e}')


def read_json(path: str)->dict:
    """
    Считывание данные из файла JSON и возвращение их.

    Params:
    path (str): Путь к файлу JSON, который должен быть прочитан.

    Returns:
    str: Данные считываются из файла JSON.

    """
    try:
        with open(path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        logging.error(f'[read_json]: {e}')

    
def write_bytes_to_txt(data: str, path: str)->None:
    """
    Запись данных в текстовый файл.

    Params:
    data (str): Данные, которые будут записаны в файл.
    path (str): Путь к файлу, в который будут записаны данные.
    """
    try:
        with open(path, 'wb') as file:
            file.write(data)
    except Exception as e:
        logging.error(f'[write_to_txt]: {e}')


def read_bytes(path: str)->bytes:
    """
    Считывание байтовых данных из файла.

    Params:
    path (str): Путь к файлу, который будет прочитан.

    Returns:
    bytes: Байтовые данные, считываемые из файла.
    """
    try:
        with open(path, 'rb') as file:
            data = file.read()
        return data
    except Exception as e:
        logging.error(f'[read_bytes]: {e}')


def write_to_txt(text: str, path: str)->None:
    """
    Запись заданного текста в файл по указанному пути.

    Params:
    text (str): Текст, который будет записан в файл.
    path (str): Путь к файлу, в который будет записан текст.    
    """
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        logging.error(f'[write_to_txt]: {e}')


def read_txt(path: str)->str:
    """
    Чтение содержимого файла по указанному пути.

    Params:
    path (str): Путь к файлу, который нужно прочитать.

    Returns:
    str: Содержимое файла.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        logging.error(f'[read_txt]: {e}')