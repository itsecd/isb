import os
import sys

sys.path.append(r'C:\Users\koten\OneDrive\Рабочий стол\oib\isb\lab_1\task2')  
from supportive import file_reader, file_writer, json_reader
from constants import PATHS, alphabet


def encrypt(key: str) -> str:
    """
    Encrypts the text using a substitution cipher.

    Parameters:
    key (str): The key to be used for encryption.

    Returns:
    str: The encrypted text.
    """

    encrypted_text = ''
     
    text = file_reader(os.path.join(paths["folder"], paths["input"]))

    cipher_dict = dict(zip(alphabet, key))
    
    for char in text:
        if char.lower() in cipher_dict:
            encrypted_text += cipher_dict[char.lower()]
        else:
            encrypted_text += char
    
    return encrypted_text

if __name__ == "__main__":
    paths = json_reader(PATHS)
    key = 'вгдежзийклмнопрстуфхцчшщъыьэюяаб'
    encrypted_text = encrypt(key)
    file_writer(os.path.join(paths["folder"], paths["encrypted"]), encrypted_text, 'w')