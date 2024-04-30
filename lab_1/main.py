from constants import *


def caesar_cipher_16(string: str) -> str:
    """ coding text using caesar cipher with shift 16 """
    result = ""
    for char in string:
        if char.isalpha():
            if char.lower() <= 'п':
                result += chr(ord(char) + 16)
            else:
                result += chr(ord(char) - 16)
        else:
            result += char
    return result