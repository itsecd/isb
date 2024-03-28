import os
import json

from work_with_json2 import read_json_file
from constants2 import PATHS2, KEY
from frequency import read_text_file


def decrypt_text(text: str, cipher: dict) -> str:
    """
    Decrypt the text using the given cipher.
    parameters: text as str, dictionary
    return: str
    """
    try:
        decrypted_text = ""
        for char in text:
            decrypted_text += cipher.get(char, char)
        return decrypted_text
    except Exception as e:
        print(f"An error occurred during text decryption: {e}")
        return ""


def main() -> None:
    """
    a function for working with file paths.
    parametrs: none
    return: none
    """
    try:
        json_data = read_json_file(PATHS2)
        if json_data:
            folder_path = json_data.get("folder", "")
            input_file = json_data.get("input", "")
            output_file = json_data.get("output", "")

            input_file_path = f"{folder_path}/{input_file}"
            output_file_path = f"{folder_path}/{output_file}"

            text = read_text_file(input_file_path)
            if text:
                decrypted_text = decrypt_text(text, KEY)
                if decrypted_text:
                    print(decrypted_text)
                    with open(output_file_path, "w", encoding="utf-8") as file:
                        file.write(decrypted_text)
                        print(f"Decrypted text saved to '{output_file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()