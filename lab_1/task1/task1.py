import json
import logging

from enum import Enum
from for_work_with_file import save_to_file, read_from_file, save_to_json_file

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    
class VigenerMode(Enum):
    """Enumeration class for the modes of Vigenere cipher operations."""
    ENCRYPT = 1
    DECRYPT = 2
    
def vigener_cipher(text, key, mode: VigenerMode):
    """
    Encrypts or decrypts the given text using the Vigenère cipher with the specified key and mode.
    
    Parameters:
    text (str): The text to be encrypted/decrypted.
    key (str): The key to be used in the Vigenère cipher.
    mode (VigenerMode): The mode of operation - ENCRYPT for encryption, DECRYPT for decryption.
    
    Returns:
    str: The resulting encrypted or decrypted text.
    """
    result_text = ""        
    key_length = len(key)
    key_index = 0

    try:
        for char in text:
            if char in alphabet:
                shift = alphabet.index(key[key_index])
                char_index = alphabet.index(char)
                if mode == VigenerMode.ENCRYPT:
                    cipher_char_index = (char_index + shift) % len(alphabet)
                    correct_cipher_char_index = (cipher_char_index + 1) % len(alphabet)
                elif mode == VigenerMode.DECRYPT:
                    cipher_char_index = (char_index - shift) % len(alphabet)
                    correct_cipher_char_index = (cipher_char_index - 1) % len(alphabet)
                result_text += alphabet[correct_cipher_char_index]
                key_index = (key_index + 1) % key_length
            else:
                result_text += char
    except Exception as e:
        logging.error(f"An error occurred during Vigener cipher operation: {str(e)}")
    
    return result_text

def main():
    """
    Main function to demonstrate the Vigenere cipher encryption and decryption process.
    """
    key = 'лист'
    save_to_json_file('lab_1/task1/key.json', key)

    text = read_from_file('lab_1/task1/text.txt')
    encrypted_text = vigener_cipher(text, key, VigenerMode.ENCRYPT)
    save_to_file('lab_1/task1/encrypted_text.txt', encrypted_text)

    encrypted_text = read_from_file('lab_1/task1/encrypted_text.txt')
    decrypted_text = vigener_cipher(encrypted_text, key, VigenerMode.DECRYPT)
    save_to_file('lab_1/task1/decrypted_text.txt', decrypted_text)

if __name__ == '__main__':
    main()
