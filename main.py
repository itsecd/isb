import argparse
import json

def create_parser()->tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("key",type=str,help="key")
    parser.add_argument("input_text",type=str,help="path to the original text")
    parser.add_argument("encrypted_text", type=str, help="path where result will be saved")
    args=parser.parse_args()
    return args.key, args.input_text, args.encrypted_text


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(data)

def tritemius_cipher(text,key):
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

def main():
    key = read_file(create_parser()[0])
    text = read_file(create_parser()[1])
    result = create_parser()[2]

    encrypted_text = tritemius_cipher(text, key)
    write_file(result, encrypted_text)

if __name__ == "__main__":
    main()