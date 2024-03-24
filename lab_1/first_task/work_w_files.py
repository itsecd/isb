import logging
import json


def read_file(path: str) -> str:
    """
    reads data from a file and returns an array of strings
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except BaseException as ex:
        logging.error(f'error in read_file - {ex}')


def write_file(path: str, new_text: list[str]) -> None:
    """
    write data to file
    """
    try:
        with open(path, 'w', encoding='utf-8') as file:
            for char in new_text:
                file.write(char)
    except BaseException as ex:
        logging.error(f'error in write_file - {ex}')


def json_to_dict(path: str) -> dict:
    """
    make json to dict
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except BaseException as ex:
        logging.error(f'error in json_to_dict - {ex}')
