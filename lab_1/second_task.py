import logging
import os

from working_with_file import json_to_dict, dict_to_json, read_file, write_file

logging.basicConfig(level=logging.INFO)

SETTING_PATH = "lab_1\\settings2.json"
RIGHT_ALPHABET = " оиеантсрвмлдякпзыьучжгхфйюбцщэъ"


def make_stats(text : str) -> dict:
    """
    Finds the frequency of occurrence of a letter in a word.
    Return dict(letter : frequency)

    parameters
    ----------
    text : str,
        Text for analysis
    """
    try:
        length = len(text)
        stats = dict()
        for letter in text:
            if letter not in stats:
                count = text.count(letter)
                stats[letter] = count / length
        stats = dict(sorted(stats.items(), key=lambda item:item[1], reverse=True))
        return stats
    except Exception as ex:
        logging.error(f"Incorrect path - {ex}")


def decryption(text : str, key : dict) -> str:
    """
    Replaces old characters with new ones in the text using a dictionary. 
    Return new text

    parameters
    ----------
    text : str,
        The text in which the replacement occurs
    key : dict,
        Dictionary-key
    """
    try:
        for old, new in key.items():
            text = text.replace(old, new)
        return text
    except Exception as ex:
        logging.error(f"Incorrect text or dict - {ex}")


if __name__ == "__main__":
    setting = json_to_dict(SETTING_PATH)
    text = read_file(os.path.join(
        setting['fold_lab'],
        setting['fold_task'],
        setting['cipherTxt']
    ))
    stats_path = os.path.join(
        setting['fold_lab'],
        setting['fold_task'],
        setting['statsJson']
    )
    key_path = os.path.join(
        setting['fold_lab'],
        setting['fold_task'],
        setting['keyJson']
    )
    decrypted_path = os.path.join(
        setting['fold_lab'],
        setting['fold_task'],
        setting['decryptedTxt']
    )

    freq = make_stats(text)
    dict_to_json(stats_path, freq)

    # letter_list = list(freq.keys())
    # key = dict(zip(letter_list, RIGHT_ALPHABET))
    # dict_to_json(key_path, key)

    keyDict = dict(zip(setting['oldSymbols'], setting['newSymbols']))
    resultTxt = decryption(text, keyDict)
    
    dict_to_json(key_path, keyDict)
    write_file(decrypted_path, resultTxt)