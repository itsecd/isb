import argparse
import logging
import os

from working_with_file import write_file, read_file, json_to_dict

logging.basicConfig(level=logging.INFO)

ALEPHBET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
DIGITAL = "0123456789"


def encryption(text : str, key : dict) -> str:
    """
    Encrypts the received text using the received key. Returns(str) the ciphertext

    Args
    ----------
    text(str) - Original text
    key(dict) - Encryption key
    """
    try:    
        i = 0
        resultText = ""
        for letter in text.upper():
            if (letter not in ALEPHBET) and (letter not in DIGITAL):
                resultText += letter
                i += 1
                continue
            resultKey = key[letter]
            if text[i].isupper(): resultText += resultKey
            else: resultText += resultKey.lower()
            i += 1
        return resultText
    except Exception as ex:
        logging.error(f"Wrong dictionary - {ex}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--setting', type=str, help='Файл с настройками') 
    args = parser.parse_args()

    if args.setting:
        setting = json_to_dict(args.setting)

    original_path = os.path.join(setting["fold_lab"], 
                                 setting["fold_task"], 
                                 setting["originalTxt"])
    key_path = os.path.join(setting["fold_lab"], 
                            setting["fold_task"], 
                            setting["keyJson"])
    result_path = os.path.join(setting["fold_lab"], 
                            setting["fold_task"], 
                            setting["resultTxt"])
    
    text = encryption(read_file(original_path), 
                      json_to_dict(key_path))
    write_file(result_path, text)