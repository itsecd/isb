import argparse
import logging
import os

from working_with_file import json_to_dict, dict_to_json, read_file, write_file

logging.basicConfig(level=logging.INFO)


def make_stats(text : str) -> dict:
    """
    Finds the frequency of occurrence of a letter in a word.
    Return dict(letter : frequency)

    Args
    ----------
    text(str) - Text for analysis
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
    Return new text(str)

    Args
    ----------
    text(str) - The text in which the replacement occurs
    key(dict) - Dictionary-key
    """
    try:
        for old, new in key.items():
            text = text.replace(old, new)
        return text
    except Exception as ex:
        logging.error(f"Incorrect text or dict - {ex}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--setting', type=str, help='Файл с настройками') 
    args = parser.parse_args()

    if args.setting:
        setting = json_to_dict(args.setting)

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

    keyDict = dict(zip(setting['oldSymbols'], setting['newSymbols']))
    resultTxt = decryption(text, keyDict)
    
    dict_to_json(key_path, keyDict)
    write_file(decrypted_path, resultTxt)