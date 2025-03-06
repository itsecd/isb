import json


def read_key(key_path)->dict[str:str]:
    """
    A function for reading the json encryption key.
    :param key_path:path to the file with the encryption key
    :return:dictionary from the key data
    """
    try:
        with open(key_path,"r",encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error: {e}")


def read_txt_file(file_path: str) -> str:
    """
    A function for reading a text file.
    :param file_path: path to the text file
    :return:text file as a string
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error: {e}")


def write_txt_file(data: str,file_path: str)->None:
    """
    A function for writing text to a file
    :param data: data to enter into the file
    :param file_path: the path to the file to save the data
    :return: None
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(data))
    except Exception as e:
        print(f"Error: {e}")


def encryption(data: str, key: dict[str, str]) -> str:
    """
    A function for encrypting text
    :param data: data for encryption
    :param key: encryption key
    :return: encrypted text
    """
    if data is None or key is None:
        return "There is no text or encryption key!"
    result = ""
    for lit in data:
        if lit in key:
            result += key[lit]
        else:
            result += lit
    return result


def frequency(data: str) -> dict:
    """
    A function for calculating the frequency of occurrence of characters in the text
    :param data:encrypted data
    :return:frequency of occurrence of symbols
    """
    dic = dict()
    for i in data:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for k in dic:
        dic[k] = dic[k] / len(data)
    return dic


def save_frequency(file_path: str, text: str) -> None:
    """
    A function to save the frequency of occurrence
    :param file_path:the path to the file to save the frequency
    :param text:text for frequency analysis
    :return:None
    """
    with open(file_path, 'w', encoding = "utf-8") as file:
        json.dump(frequency(text), file,ensure_ascii=False)