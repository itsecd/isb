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


def txt_reader(path: str) -> str:
    """
    Reading txt file with paths and returning string
    :param path: path to txt file
    :return: string with data in txt file
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            result = f.read()
        return result
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


def json_writer(path: str, result: dict) -> None:
    """
    Write a json file with paths and returns a dictionary
    :param path (str): The path to the json file.
    :param result (str): The result to write json file.
    :return:None

    """
    try:
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
    except Exception as ex:
        logging.error(f"Failed to write json file: {ex}")
        