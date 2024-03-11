import json
import logging

logging.basicConfig(level=logging.INFO)


def read_from_file(file_path: str) -> str:
    """
    Read text data from the specified file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logging.error(
            f"An error occurred while reading the file '{file_path}': {e}")
        return ''


def write_to_file(file_path: str, data: str) -> None:
    """
    Write data to the specified file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)
        logging.info(f"Data written to '{file_path}' successfully.")
    except Exception as e:
        logging.error(
            f"An error occurred while writing to the file '{file_path}': {e}")


def load_json_file(json_file_path: str) -> dict:
    """
    Load encryption key from the specified file.

    Args:
        key_path (str): The path to the file containing the encryption key.

    Returns:
        dict: The encryption key loaded from the file.
    """
    try:
        with open(json_file_path, encoding='utf-8') as f:
            key = json.load(f)
        return key
    except Exception as e:
        logging.error(
            f"An error occurred while loading the key from '{json_file_path}': {e}")
        return {}


def encrypt_text(text_path: str, key_path: str) -> str:
    """
    Encrypts the given text using the provided key.

    Args:
        text_path (str): The path to the text to be encrypted.
        key_path (str): The path to the encryption key where keys are uppercase characters
                    and values are their corresponding encrypted forms.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ''
    try:
        text = read_from_file(text_path)
        key = load_json_file(key_path)
        for char in text:
            if char.upper() in key:
                encrypted_text += key[char.upper()]
            else:
                encrypted_text += char
    except Exception as e:
        logging.error(f"Error occurred during encryption: {e}")
    return encrypted_text


def decrypt_text(text_path: str, key_path: str) -> str:
    """
    Decrypts the given text using the provided key.

    Args:
        text_path (str): The path to the text to be decrypted.
        key_path (str): The path to the encryption key where values are encrypted characters
                    and keys are their corresponding decrypted forms.

    Returns:
        str: The decrypted text.
    """
    decrypted_text = ''
    try:
        text = read_from_file(text_path)
        key = load_json_file(key_path)
        reverse_key = {value: key for key, value in key.items()}
        for char in text:
            if char.upper() in reverse_key:
                decrypted_text += reverse_key[char.upper()]
            else:
                decrypted_text += char
    except Exception as e:
        logging.error(f"Error occurred during decryption: {e}")
    return decrypted_text


if __name__ == "__main__":
    try:
        with open("lab_1/options.json", "r") as options_file:
            options = json.load(options_file)
        encrypted_text = encrypt_text(options['original_text'], options['key'])
        write_to_file(options['encrypted_text'], encrypted_text)

        decrypted_text = decrypt_text(
            options['encrypted_text'], options['key'])
        write_to_file(options['decrypted_text'], decrypted_text)

    except Exception as e:
        logging.error(f"An error occurred: {e}")