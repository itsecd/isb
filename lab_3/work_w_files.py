import logging
import json


def json_to_dict(path: str) -> dict:
    """
    make json to dict
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except BaseException as ex:
        logging.error(f'error in json_to_dict - {ex}')


def write_bytes(path: str, text: bytes) -> None:
    """write binary file"""
    try:
        with open(path, 'wb') as file:
            file.write(text)
    except BaseException as ex:
        logging.error(f'error in write_file - {ex}')


def read_bytes(path: str) -> bytes:
    """read binary file"""
    try:
        with open(path, 'rb') as file:
            return file.read()
    except BaseException as ex:
        logging.error(f'error in read_file - {ex}')


def write_file(path: str, data: str) -> None:
    """writing data to a file"""
    try:
        with open(path, "a", encoding='UTF-8') as file:
            file.write(data)
    except Exception as e:
        print(f"error in writing the file: {str(e)}")
