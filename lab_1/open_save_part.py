import json
import logging
import re


logging.basicConfig(level=logging.INFO)


def open_file(path: str) -> str:
    """
    Function for open .txt-files and making str.
    parameters:
        path: path to the file to open
    """
    try:
        with open(path, "r+", encoding="utf-8") as file:
            data = file.read()
        return data
    except Exception as ex:
        logging.error(f"Failed to open file or file was not found: {ex.message}\n{ex.args}\n")


def write_data(path: str, data: str) -> None:
    """
    Function for write str-dats in .txt-file.
    parameters:
        path: path to file to write data 
        data: data to write to a file
    """
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as ex:
        logging.error(f"Failed to write data or file was not found: {ex.message}\n{ex.args}\n")


def formatting(path: str) -> None:
    """Function for formatting text:
    removes punctuation marks and results in uppercase.
    parameters:
        path: path to the file to open and formatting
    """
    try:
        data = open_file(path)
        new_text = str.upper(data)
        clean_string = re.sub("\W+", " ", new_text)
        write_data(path, clean_string)
    except Exception as ex:
                    logging.error(f"Failed to formatting data: {ex.message}\n{ex.args}\n")


def dict_save(dictionary: dict, path: str) -> None:
    """Saving a dictionary to a json-file. 
    parameters:
        dictionary: dictionary for saving
        path: path to file to write dictoinary
    """
    try:
        with open(path, "w", encoding="utf-8") as fp:
            json.dump(dictionary, fp, ensure_ascii=False, indent=1)
    except Exception as ex:
        logging.error(f"Failed to saving dictionary: {ex.message}\n{ex.args}\n")
