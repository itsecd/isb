import os
import sys
 
from supportive import json_reader, file_writer, file_reader
from constants_for_encrypt import PATHS, ALPHABET


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

    cipher_dict = dict(zip(ALPHABET, key))
    
    for char in text:
        if char.lower() in cipher_dict:
            encrypted_text += cipher_dict[char.lower()]
        else:
            encrypted_text += char
    
    return encrypted_text


if __name__ == "__main__":
    paths = json_reader(PATHS)
    encrypted_text = encrypt(os.path.join(paths["key"]))
    file_writer(os.path.join(paths["folder"], paths["encrypted"]), encrypted_text, 'w')