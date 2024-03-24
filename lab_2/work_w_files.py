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
