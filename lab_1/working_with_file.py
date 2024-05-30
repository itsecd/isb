import json
import logging

logging.basicConfig(level=logging.INFO)

def read_file(path : str) -> str:
    """
    Read file. Return text from file.

    Args
    ----------
    path(str) - Path to file
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def write_file(path : str, text : str) -> None:
    """
    Write text to file

    Args
    ----------
    path(str) - Path to save text
    text(str) - Text for saving
    """
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def json_to_dict(path : str) -> dict:
    """
    Read json to dict

    Args
    ----------
    path(str) - Path to json file
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            key = json.load(f)
        return key
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def dict_to_json(path : str, dict : dict) -> None:
    """
    Write dict to json file

    Args
    ----------
    path(str) - Path to json file
    dict(dict) - dict for saving
    """
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(dict, file)
    except Exception as ex:
        logging.error(f"Incorrect dict - {ex}")