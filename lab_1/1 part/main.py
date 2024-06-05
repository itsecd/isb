import json
from path import (
    encryption_key,
    encryption_input,
    encryption_output,
    encryption_decoded)


def read_text_from_file(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file_name}': {e}")
        return None


def read_key_from_file(file_name: str) -> int:
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            data = json.load(file)
            key = data["key"]
        return key
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return None
    except ValueError:
        print(f"Неверный формат ключа в файле '{
              file_name}'. Ключ должен быть целым числом.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file_name}': {e}")
        return None


def write_text_to_file(text: str, file_name: str) -> None:
    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"Произошла ошибка при записи в файл '{file_name}': {e}")


def code_scytale(text: str, key: int) -> str:
    result = [''] * key
    for i, char in enumerate(text):
        index = i % key
        result[index] += char
    return ''.join(result)


def encode_scytale(text: str, key: int) -> str:
    return code_scytale(text, key)


def decode_scytale(text: str, key: int) -> str:
    dekey = (len(text) // key)
    return code_scytale(text, dekey)


if __name__ == "__main__":
    input_text = read_text_from_file(encryption_input)
    substitution = read_key_from_file(encryption_key)
    if input_text is not None and substitution is not None:
        encrypted_text = encode_scytale(input_text, substitution)
        write_text_to_file(encryption_output)
        decoded_text = decode_scytale(encrypted_text, substitution)
        write_text_to_file(encryption_decoded)
