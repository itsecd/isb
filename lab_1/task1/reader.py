import json
import logging

logging.basicConfig(level=logging.INFO)


def json_reader(path: str) -> dict:
    """Reads json file into dict.
    :param path: path to json file
    :return: dict which contains keys and values from file
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            paths = json.load(file)
        return paths
    except Exception as exc:
        logging.error(f'Cannot find the path: {exc}\n')

def txt_reader(path: str) -> str:
    """Reads txt file into str.
    :param path: path to txt file
    :return: str of text from file
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read().replace(' ', '').replace('\n', '')
        return text
    except Exception as exc:
        logging.error(f'Cannot find the path: {exc}\n')