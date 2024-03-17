import argparse
import json
import logging
import os

from writer_and_reader import read_from_file, write_to_file


logging.basicConfig(level=logging.INFO)


def char_freq_analysis(text: str, json_text:str) -> dict:
    """Perform character frequency analysis of the given text."""
    try:
        data = read_from_file(text)
        my_dict = {}

        for char in data:
            my_dict[char] = my_dict.get(char, 0) + 1

        total_chars = len(data)
        relative_freq_dict = {char: count / total_chars for char, count in my_dict.items()}

        sorted_dict = dict(sorted(relative_freq_dict.items(), key=lambda x: x[1], reverse=True))
        with open(json_text, "w", encoding="utf-8") as json_file:
            json.dump(sorted_dict, json_file, ensure_ascii=False, indent=1)
    except Exception as ex:
        logging.error(f"Can't do analysis: {ex}\n")


def decrypt_text(encrypted_text: str, key_path: str, decrypted_text: str) -> None:
    """Decrypt the given encrypted text using the key from the JSON file
    and save the result in a text file"""
    try:
        data = read_from_file(encrypted_text)

        with open(key_path, "r", encoding="utf-8") as key_file:
            dict = json.load(key_file)
        for key, value in dict.items():
            data = data.replace(key, value)
        write_to_file(decrypted_text, data)
    except Exception as ex:
        logging.error(f"Can't do analysis: {ex}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform character frequency analysis.")
    parser.add_argument("--input_file",
                        type=str,
                        default=os.path.join('isb','lab_1','task2','cod1.txt'),
                        help="Path to the input file.")
    parser.add_argument("--output_file",
                        type=str,
                        default=os.path.join('isb','lab_1','task2','result.json'),
                        help="Path to the output JSON file.")
    parser.add_argument("--key",
                        type=str,
                        default=os.path.join('isb','lab_1','task2','key.json'),
                        help="Path to the key JSON file.")
    parser.add_argument("--decrypted_file",
                        type=str,
                        default=os.path.join('isb','lab_1','task2','decrypted_text.txt'),
                        help="Path to the decrypted text file.")
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        logging.error(f"File '{args.input_file}' does not exist.")
        exit(1)
    try:
        char_freq_analysis(args.input_file, args.output_file)
        decrypt_text(args.input_file, args.key, args.decrypted_file)
        logging.info(f"Text successfully decrypted and saved to {args.decrypted_file}")
    except Exception as ex:
        logging.error(f"Error during decryption: {ex}")