import argparse
from collections import Counter
import json

def create_parser()->tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("key",type=str,help="key")
    parser.add_argument("input_text",type=str,help="path to the original text")
    parser.add_argument("encrypted_text", type=str, help="path where result for task1 will be saved")
    parser.add_argument("task2_key", type=str, help="path to the key for task2")
    parser.add_argument("task2_encrypted", type=str, help="path to encrypted text for task2")
    parser.add_argument("task2_result", type=str, help="path where result for task2 will be saved")
    args=parser.parse_args()
    return args.key, args.input_text, args.encrypted_text, args.task2_key, args.task2_encrypted, args.task2_result


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

def get_frequency(filename):
    char_count = Counter(filename)
    total_chars = len(filename)
    char_frequency = {char: count/total_chars for char, count in char_count.items() }
    sorted_char_frequency = dict(sorted(char_frequency.items(), key=lambda item: item[1], reverse=True))
    with open("frequency_analysis.json", 'w', encoding='utf-8') as file:
        json.dump(sorted_char_frequency, file, ensure_ascii=False, indent=4)

def get_key(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        key=json.load(file)
    reverse_key = {char: k for k, char in key.items()}
    return reverse_key

def get_decryption(encrypted_text, key):
    decrypted_text = ''.join([key.get(char,char) for char in encrypted_text])
    return decrypted_text

def main():
    key = read_file(create_parser()[0])
    text = read_file(create_parser()[1])
    result = create_parser()[2]

    encrypted_text = tritemius_cipher(text, key)
    write_file(result, encrypted_text)

    task2_key = create_parser()[3]
    original_text_task2 = read_file(create_parser()[4])
    get_frequency(original_text_task2)

    task2_decrypted = create_parser()[5]

    task2_res = get_decryption(original_text_task2, get_key(task2_key))
    write_file(task2_decrypted, task2_res)



if __name__ == "__main__":
    main()