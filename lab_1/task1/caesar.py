import logging

from constants import ALPHABET

logging.basicConfig(level=logging.INFO)


def caesar_encrypt(text : str, shift : int) -> str:
    """Encrypts text from file using Caesar method.
    :param text: str of text that is needed to encrypt
    "param shift: shift for caesar method
    :return: str of encrypted text
    """
    try:
        new_alphabet = {((value - shift) % 32): key for key, value in ALPHABET.items()}
        encrypted_text = ""
        for char in text:
            if char.lower() in ALPHABET:
                encrypted_text += new_alphabet[ALPHABET[char.lower()]]
            else:
                encrypted_text += char
        return encrypted_text
    except Exception as exc:
        logging.error(f'Encrypting error: {exc}\n')

