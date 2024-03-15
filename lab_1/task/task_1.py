import os

from working_with_a_file import *


alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def atbash_cipher(text_path: str, path: str) -> None:
    """
    implements the atbash cipher and writes data to a file

    Parameters
        text_path: the path to the file where the message is located
        path: the path where the cipher will be written
    """
    reversed_alphabet = alphabet[::-1]
    result = ''
    text = read_file(text_path)
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            result += reversed_alphabet[index]
        else:
            result += char

    write_file(path, result)


def key_json(path: str) -> None:
    """
    Сreate the key to the atbash cipher and writes it to a json file in the form of a dictionary

    Parameters
        path: the path where the key will be written
    """
    reversed_alphabet = alphabet[::-1]
    key = dict()
    for i, char in enumerate(alphabet):
        key[char] = reversed_alphabet[i]
    write_json(key, path)


def decryption(path_encryption: str, path_key: str, path_decryption: str) -> None:
    """
    Decrypts the text by the key

    Parameters
        path_encryption: the path to the encrypted text file
        path_key: the path to the key file
        path_decryption: the path to the file where the decrypted text will be written
    """
    key = read_json(path_key)
    decrypted_text = ''
    text = read_file(path_encryption)
    for char in text:
        if char in key:
            decrypted_text += key[char]
        else:
            decrypted_text += char
    write_file(path_decryption, decrypted_text)


if __name__ == "__main__":
    atbash_cipher(os.path.join('text', 'first_task', 'text.txt'),
                  os.path.join('text', 'first_task', 'encryption.txt'))

    key_json(os.path.join('text', 'first_task', 'key.json'))

    decryption(os.path.join('text', 'first_task', 'encryption.txt'),
               os.path.join('text', 'first_task', 'key.json'),
               os.path.join('text', 'first_task', 'decryption.txt'))


