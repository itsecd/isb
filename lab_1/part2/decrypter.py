import os
import json
import logging


logging.basicConfig(level=logging.INFO)


def replace_letters(input_file:str, output_file:str, key_file_path:str) -> None:
    """
    Replace encoded letters in the input file using a provided key mapping.

    Parameters:
    - input_file (str): The path to the input file containing the text with encoded letters.
    - output_file (str): The path to the output file where the decoded text will be saved.
    - key_file_path (str): The path to the JSON file containing the key mapping for letter replacement.

    Returns:
    - None
    """
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        with open(key_file_path, 'r', encoding='utf-8') as key_file:
            key_mapping = json.load(key_file)

        for key, value in key_mapping.items():
            text = text.replace(value, key)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)

    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON in key file: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during file processing: {e}")


if __name__ == '__main__':
    with open(os.path.join("lab_1","part2","params2.json"), 'r', encoding='utf-8') as json_file:
        params = json.load(json_file)
    replace_letters(params["input_file"],params["output_file"],params["key"])