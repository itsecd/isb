from constants import alphabet
from work_with_files import save_json_file
from typing import Dict

def create_caesar_key(shift: int, path: str) -> None:
    """
    Creates a Caesar cipher key based on the specified shift value and saves it in JSON format.

    :param shift: The number used to shift the alphabet.
    :param path: The file path to save the JSON file.
    :return: None
    """

    caesar_key: Dict[str, str] = {}

    try:
        for i in range(len(alphabet)):
            shifted = alphabet[(i + shift) % 33]
            caesar_key[alphabet[i]] = shifted

        save_json_file(path, caesar_key)

    except Exception as e:
        print(f"An error occurred while creating the encryption key: {e}")