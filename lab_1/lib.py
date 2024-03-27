import json

from typing import Optional


def get_key(file_path: str) -> Optional[dict[str, str]]:
    """
        The function reads the key from the json file, and if successful, returns a dict

    Args:
        file_path (str): path to key(json file)

    Returns:
        Optional[dict]: dict contains key
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)  
        return data
    except Exception:
        return None


def get_text(file_path: str) -> Optional[str]:
    """The function reads text from a .txt file, removes \n and returns text without indentation

    Args:
        file_path (str): path to text(.txt file)

    Returns:
        Optional[str]: text from file
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            data = f.read()
            data = data.replace("\n", "")
        return data
    except Exception:
        return None


def print_dict(source: dict[str, str]) -> str:
    """Function for beautiful dictionary printing

    Args:
        source (dict[str, str]): Dict neddy in printing

    Returns:
        str: result of dict printing
    """
    res = ""
    for key, value in source.items():
        res = res + "(" + "{0}: {1}".format(key, value) + ")" + "  "
    return res


def get_freq(source_text: str) -> dict[str, str]:
    """The function counts the frequency of occurrence of symbols in the text

    Args:
        source_text (str): Text to analysis

    Returns:
        dict[str, str]: dictionary, where the key is the symbol and the value is the frequency
    """
    freq = {}
    length = len(source_text)
    for symb in set(source_text):
        freq[symb] = round((source_text.count(symb) / length), 5)
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


def encrypt_by_key(text: str, key: dict[str, str]) -> str:
    """the function uses the cryption key to replace characters in the text using the key

    Args:
        text (str): text to crypt
        key (dict[str, str]): cryption key

    Returns:
        str: result of crypting
    """
    res = ""
    for letter in text:
        if letter in key.keys():
            res += key[letter]
        else:
            res += letter
    return res


def decrypt_by_key(text: str, key: dict[str, str]) -> str:
    """the function uses the cryption key to replace characters in the text using the key

    Args:
        text (str): text to decrypt
        key (dict[str, str]): cryption key

    Returns:
        str: result of decrypting
    """
    new_key = {v: k for k, v in key.items()}
    res = ""
    for letter in text:
        if letter in new_key.keys():
            res += new_key[letter]
        else:
            res += letter
    return res


def write_to_file(text: str, path: str) -> Optional[None]:
    """function to write text to a .txt file

    Args:
        text (str): text to write
        path (str): path to file
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception:
        return None
