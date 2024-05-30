import logging
import json

def read_txt(file_path: str) -> str:
    """Reads a text file and returns its content as a string.
    Args:
        file_path (str): The path to the text file.
    Returns:
        str: The content of the text file.
    """
    try:
        with open(file_path, "r",encoding='utf-8') as f:
            data = f.read()
            return data
    except Exception as e:
        logging.error(f"file reading error: {e}")

def write_txt(file_path: str, data: str) -> None:
    """Writes a string to a text file.
    Args:
        file_path (str): The path to the text file.
        data (str): The data to write to the file.
    """
    try:
        with open(file_path, "w",encoding="utf-8") as f:
            f.write(data)
            return data
    except Exception as e:
        logging.error(f"file writing error: {e}")

def read(file_path: str) -> str:
    """Reads a binary file and returns its content as a byte string.
    Args:
        file_path (str): The path to the binary file.
    Returns:
        bytes: The content of the binary file.
    """
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            return data
    except Exception as e:
        logging.error(f"binary file reading error: {e}")

def json_read(file_path: str) -> dict:
    """Reads a JSON file and returns its content as a dictionary.
    Args:
        file_path (str): The path to the JSON file.
    Returns:
        dict: The content of the JSON file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load( f)
    except Exception as e:
        logging.error(f"JSON file reading error: {e}")

def write(file_path: str, data) -> None:
    """Writes data to a binary file.
    Args:
        file_path (str): The path to the binary file.
        data (bytes): The data to write to the file.
    """
    try:
        with open(file_path, "wb") as f:
            f.write(data)
    except Exception as e:
        logging.error(f"JSON file writing error: {e}")