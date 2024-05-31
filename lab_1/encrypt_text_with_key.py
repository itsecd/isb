from work_with_files import read_txt_file, write_txt_file, load_json_file
from typing import Dict

def encrypt_text_with_key(text_file_path: str, dict_file_path: str, output_file_path: str) -> None:
    """
    Encrypt the text from the input file using the dictionary file and save the encrypted text to the output file.

    :param text_file_path: Path to the input text file.
    :param dict_file_path: Path to the dictionary JSON file.
    :param output_file_path: Path to the output encrypted text file.
    """
    try:
        text: str = read_txt_file(text_file_path)
        dictionary: Dict[str, str] = load_json_file(dict_file_path)
        encrypted_text: str = ""

        for char in text:
            if char in dictionary:
                encrypted_text += dictionary[char]
            else:
                encrypted_text += char
            
        write_txt_file(output_file_path, encrypted_text)
    
    except Exception as e:
        print(f"An error occurred: {e}")