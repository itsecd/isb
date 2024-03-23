import json
import logging
import os

from files import write_file, read_file, get_dict


logging.basicConfig(filename="lab_1/report.log", filemode="a", level=logging.INFO)


def get_freq(path: str, new_path: str) -> dict:
    """
    The function allows you to write a dictionary 
    using the transmitted path and the new path using 
    the function from task 1
    
    Args:
        path (str): path to the content file
        new_path (str): path to the file to write the dictionary

    Returns:
        dict: dictionary with symbol frequencies
    """
    text = read_file(path)
    freq_dict = dict()
    try:
        for i in text:
            freq_dict[i] = text.count(i) / len(text)
        sorted_freq_dict = dict(
            sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
        get_dict(sorted_freq_dict, new_path)
        logging.info("freq_dict created")
    except Exception as e:
        logging.error(f"Error freq_dict {e}")
    return sorted_freq_dict


def replace_letters(
    text: str, 
    freq_dict: dict, 
    old_letter: str, 
    new_letter: str, 
    path_dict: str
) -> str:
    """
    The function takes from the user the letter 
    we are changing and the replacement letter and 
    updates the dictionary
    
    Args:
        text (str): the text in which the characters are replaced
        freq_dict (dict): dictionary with character frequencies
        old_letter (str): the character that will be replaced
        new_letter (str): the new character to be replaced with
        path_dict (str): path to the file for the dictionary entry

    Returns:
        str: updated text after character replacement  
    """
    try:
        text = text.replace(old_letter, new_letter)
        freq_dict[old_letter] = new_letter
        get_dict(freq_dict, path_dict)
        logging.info("replace_letters work")
    except Exception as e:
        logging.error(f"Error replace_letters {e}")
    return text


def decryption(text_path: str, result_path: str, dict_path: str) -> None:
    """
    The function modifies the ciphertext according to the dictionary
    
    Args:
        text_path (str): path to the ciphertext file
        result_path (str): path to the decryption file
        dict_path (str): path to dictionary 
    """
    try:
        text = read_file(text_path)
        with open(dict_path, "r", encoding="utf-8") as f:
            dict = json.load(f)
        for char, freq in dict.items():
            text = text.replace(char, freq)
        write_file(result_path, text)
    except Exception as e:
        logging.error(f"Error decryption {e}")


if __name__ == "__main__":
    with open(os.path.join("lab_1", "settings.json"), "r", encoding="utf-8") as json_f:
        settings = json.load(json_f)
    text_path = os.path.join(settings["dir"], settings["folder"], settings["text"])
    freq_dict_path = os.path.join(settings["dir"], settings["folder"], settings["dict"])
    decryption(
        text_path, 
        os.path.join(settings["dir"], settings["folder"], settings["result"]),
        freq_dict_path,
    )
