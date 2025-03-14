from audioop import reverse
from collections import Counter
import json

def read_file(filename: str)->str:
    """
    Opens a file in read mode
    :param filename: directory of the file
    :return: content of the file as a string
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filename: str, data:str)->int:
    """
    Opens a file in write mode
    :param filename: directory of the file
    :param data: text that will be added to the file
    :return: number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(data)

def tritemius_cipher(text: str, key: str)->str:
    """
    Gets encrypted text using Trithemius Cipher
    :param text: directory to original text
    :param key: word that will be using for encryption
    :return: encrypted text as a string
    """
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"
    char_to_num = {char: i + 1 for i, char in enumerate(alphabet)}
    num_to_char = {i + 1: char for i, char in enumerate(alphabet)}

    text = text.upper()
    key = key.upper()

    encrypted_text = []
    key_id = 0

    for i, char in enumerate(text):
        if char in char_to_num:
            text_num = char_to_num[char]
            key_char = key[key_id % len(key)]
            key_num = char_to_num[key_char]

            encrypted_num = text_num + key_num
            if encrypted_num > len(alphabet):
                encrypted_num -= len(alphabet)
            encrypted_text.append(num_to_char[encrypted_num])

            key_id+=1
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def get_frequency(filename: str)->None:
    """
    Gets a frequency for every character in the text
    :param filename: directory to the text file
    """
    char_count = Counter(filename)
    total_chars = len(filename)
    char_frequency = {char: count/total_chars for char, count in char_count.items() }
    sorted_char_frequency = dict(sorted(char_frequency.items(), key=lambda item: item[1], reverse=True))
    with open("frequency_analysis.json", 'w', encoding='utf-8') as file:
        json.dump(sorted_char_frequency, file, ensure_ascii=False, indent=4)

def get_key(filename: str)->dict:
    """
    Gets a key for decryption the text
    :param filename: directory of the key file
    :return: key for decryption
    """
    with open(filename, 'r', encoding='utf-8') as file:
        key=json.load(file)
    return key

def get_decryption(encrypted_text: str, key: dict)->str:
    """
    Gets decrypted text
    :param encrypted_text: directory to encrypted text
    :param key: key for decryption
    :return: decrypted text as a string
    """
    decrypted_text = ''.join([key.get(char,char) for char in encrypted_text])
    return decrypted_text