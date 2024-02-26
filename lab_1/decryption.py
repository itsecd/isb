import argparse
import json
import logging
import os

from read_write import read_file, write_to_file


logging.basicConfig(level=logging.INFO)


def get_dict(path: str, new_path: str) -> None:
    """
    Creates a dictionary with the relative frequencies of characters in the given text file
    and saves the sorted dictionary in JSON format.

    Args:
        path (str): The path to the input text file.
        new_path (str): The path to the output JSON file.

    Raises:
        IOError: If there is an issue reading the input file or writing to the output file.
    """
    try:
        data = read_file(path)
        my_dict = {}
        
        for char in data:
            my_dict[char] = my_dict.get(char, 0) + 1
        
        total_chars = len(data)
        relative_freq_dict = {char: count / total_chars for char, count in my_dict.items()}
        
        sorted_dict = dict(sorted(relative_freq_dict.items(), key=lambda x: x[1], reverse=True))
        
        with open(new_path, "w", encoding="utf-8") as json_file:
            json.dump(sorted_dict, json_file, ensure_ascii=False, indent=1)
    
    except Exception as ex:
        logging.error(f"Error during creating and saving the dictionary: {ex}\n")


def decrypt_text(encrypted_text: str, key_path: str, decrypted_text: str) -> None:
    """
    Decrypts the text using a given key and saves the result.

    Args:
        encrypted_text (str): Path to the file containing the encrypted text.
        key_path (str): Path to the JSON file containing the decryption key.
        decrypted_text (str): Path to the file where the decrypted text will be saved.

    Raises:
        IOError: If there is an issue reading the encrypted text file, the key file, or writing to the decrypted text file.
    """
    try:
        data = read_file(encrypted_text)
        
        with open(key_path, "r", encoding="utf-8") as key_file:
            dict = json.load(key_file)
        
        for key, value in dict.items():
            data = data.replace(key, value)
        
        write_to_file(decrypted_text, data)
    
    except Exception as ex:
        logging.error(f"Error during text decryption: {ex}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decryption of text encrypted with monoalphabetic substitution")
    parser.add_argument(
        "--input_file",
        type=str,
        default=os.path.join("lab_1","task_2","cod1.txt"),
        help="Path to the input file containing the text to be encrypted."
    )

    parser.add_argument(
        "--freq_dict",
        type=str,
        default=os.path.join("lab_1","task_2","freq.json"),
        help="Path to the file where the frequency dictionary will be saved."
    )
    
    parser.add_argument(
        "--key_dict",
        type=str,
        default=os.path.join("lab_1","task_2","key.json"),
        help="Path to the file that contains the key dictionary."
    )
    
    parser.add_argument(
        "--output_file",
        type=str,
        default=os.path.join("lab_1","task_2","decrypted_text.txt"),
        help="Path to the output file where the encrypted text will be saved."
    )

    args = parser.parse_args()

    try:
        get_dict(args.input_file,args.freq_dict)
        decrypt_text(args.input_file,args.key_dict,args.output_file)
        logging.info(f"Text successfully decrypted and saved to {args.output_file}")
    except Exception as ex:
        logging.error(f"Error during decryption: {ex}")