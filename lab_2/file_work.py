import json
import logging

logging.basicConfig(level=logging.INFO)


def json_reader(path: str) -> dict:
    """
    Reading json file with paths and returning dict
    :param path: path to json file
    :return: dict with data in json file
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            paths = json.load(f)
        return paths
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def txt_writer(path: str, input_string: str) -> None:
    """
    Writing an input string in txt file
    :param input_string: input string to write in txt file
    :param path: path to txt file
    :return: None
    """
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(input_string)
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")
