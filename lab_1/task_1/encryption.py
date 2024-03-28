import os
import json

from work_with_json import read_json_file
from constants import POLYBEL_SQUARE, PUNCTUATION_MARKS, PATHS


def encrypt_text(text: str, polybius_square: list) -> str:
    """
    Text encryption using Polybius square.
    parametrs: text as str, polybius_square as list
    return: str
    """
    encrypted_text = ""
    try:
        for char in text:
            if char.lower() in PUNCTUATION_MARKS:
                encrypted_text += char
            else:
                char_found = False
                for i in range(len(polybius_square)):
                    for j in range(len(polybius_square[i])):
                        if char.lower() == polybius_square[i][j]:
                            encrypted_text += f"({i + 1}{j + 1})"
                            char_found = True
                            break
                    if char_found:
                        break
                else:
                    raise ValueError(
                        f"Character '{char}' not found in the Polybius square."
                    )
    except Exception as e:
        print("An error occurred:", e)
        return ""
    return encrypted_text


def main() -> None:
    """
    a function for working with file paths.
    parametrs: none
    return: none
    """
    paths_data = read_json_file(PATHS)
    if paths_data:
        folder = paths_data.get("folder", "")
        incoming_text = paths_data.get("incoming_text", "")
        outgoing_text = paths_data.get("outgoing_text", "")

        if folder and incoming_text and outgoing_text:
            try:
                with open(f"{folder}/{incoming_text}", "r", encoding="utf-8") as file:
                    text = file.read()
                    encrypted_text = encrypt_text(text, POLYBEL_SQUARE)

                with open(f"{folder}/{outgoing_text}", "w", encoding="utf-8") as file:
                    file.write(encrypted_text)

                print("Текст успешно зашифрован и сохранен в файле.")
            except FileNotFoundError:
                print("Один из файлов не найден.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        else:
            print("Не удалось получить пути к файлам из JSON-данных.")
    else:
        print("Не удалось прочитать данные из JSON-файла.")


if __name__ == "__main__":
    main()