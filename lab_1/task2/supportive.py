import json
import logging

logging.basicConfig(level=logging.INFO)

def json_reader(path: str) -> dict:
    """
    Reading json file with paths and returning dict
    :param path:
    :return:
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            paths = json.load(f)
        return paths
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def file_reader(path_input: str) -> str:
    """
    Reads the contents of a text file specified by the input path.

    Args:
    path_input (str): The path to the text file to be read.

    Returns:
    str: The contents of the text file as a string.
    """
    try:
        with open(path_input, 'r', encoding='utf-8') as f_input:
            return f_input.read()
    except Exception as ex:
        logging.error(f"File can't be open or was not found: {ex}\n")


def file_writer(path: str, content: str, type: str) -> None:
    """
    Writes the specified content to a file at the given path.

    Args:
    path (str): The path to the file where the content will be written.
    content (str): The content to be written to the file.

    Returns:
    None
    """
    try:
        with open(path, type , encoding='utf-8') as file:
            file.write(content)
    except Exception as ex:
        logging.error(f"File can't be open or was not found: {ex}\n")