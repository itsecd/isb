import json
import logging


logging.basicConfig(filename="lab_1/report.log", filemode="a", level=logging.INFO)


def read_file(path: str) -> str:
    """
    Function to read file contents
    
    Args:
        path (str): path to the content file

    Returns:
        str: file contents
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        logging.info("read_file")
    except Exception as e:
        logging.error(f"error in read {e}")
    return text


def write_file(path: str, text: str) -> None:
    """
    Function for recording the result of the Vigenere method
    
    Args:
        path (str): path to the content file
        text (str): str to write to file
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            f.write(text)
        logging.info("write_file")
    except Exception as e:
        logging.error(f"error in write_file {e}")


def formatting_text(path: str) -> None:
    """
    Function for formatting text
    
    Args:
        path (str): path to the content file
    """
    try:
        text = read_file(path)
        words = text.split()
        formatted_text = ' '.join(words)
        upper_text = formatted_text.upper()
        write_file(path, upper_text)
        logging.info("formatting")
    except Exception as e:
        logging.error(f"error in formatting {e}")


def get_dict(dict: dict, path: str) -> None:
    """
    The function writes the dictionary to the json file
    
    Args:
        dict (path): writable dictionary
        path (str): path for the json file
    """
    try:
        with open(path, "w", encoding="utf-8") as json_f:
            json.dump(dict, json_f, ensure_ascii=False)
        logging.info("json created")
    except Exception as e:
        logging.error(f"error in get_dict {e}")
