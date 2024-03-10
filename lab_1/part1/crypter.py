import os
import json
import logging


logging.basicConfig(level=logging.INFO)


def encoder(input_file:str, output_file:str,shift:int, key_file:str) -> None:
    """
    Encode the contents of the input file using a Caesar cipher with a specified shift value.
    
    Parameters:
    - input_file (str): The path to the input file containing the text to be encoded.
    - output_file (str): The path to the output file where the encoded text will be saved.
    - shift (int): The number of positions to shift each alphabetic character in the text.
    - key_file (str): The path to the output file where the encoding key will be saved in JSON format.

    Returns:
    - None
    """
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        encoder_text = ""
        encoding_dict = {}

        for char in text:
            if char.isalpha():
                base_char = 'а' if char.islower() else 'А'
                encoded_char = chr((ord(char) - ord(base_char) + shift) % 32 + ord(base_char))
                encoder_text += encoded_char
                encoding_dict[char] = encoded_char
            else:
                encoder_text += char

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(encoder_text)

        with open(key_file, 'w', encoding='utf-8') as json_file:
            json.dump(encoding_dict, json_file, ensure_ascii=False)

    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    with open(os.path.join("lab_1","part1","params1.json"), 'r', encoding='utf-8') as json_file:
            params = json.load(json_file)
    encoder(params["input_file"],params["output_file"],params["shift"],params["key_file"])
