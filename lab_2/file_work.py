import json
import logging

logging.basicConfig(level=logging.INFO)


def json_reader(path: str) -> dict:
    """
    Reading json file with paths and returning dict
    :param path: (str) input path of json file
    :return:
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            paths = json.load(f)
        return paths
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def txt_writer(path: str, result: str) -> None:
    """
    Write a txt file with paths
    :param path: (str) The path to the txt file.
    :param result: (str) The result to write txt file.
    :return:None

    """
    try:
        with open(path, 'w', encoding="utf-8") as f:
            f.write(result)
    except Exception as ex:
        logging.error(f"Failed to write txt file: {ex}")
