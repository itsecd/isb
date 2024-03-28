import os
import json

from work_with_json2 import read_json_file
from constants2 import PATHS2
from collections import Counter, defaultdict


def read_text_file(file_path: str) -> str:
    """
    Read text from a file
    parameters: file_path as str
    return: str
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден.")
        return ""
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return ""


def character_frequency(text: str) -> dict:
    """
    Calculate the frequency of each character in the text, including tabs
    parameters: text as str: input text
    return: dict
    """
    try:
        frequencies = defaultdict(int)
        for char in text:
            frequencies[char] += 1
        return frequencies
    except Exception as e:
        print(f"An error occurred while calculating character frequencies: {e}")
        return {}


def main():
    try:
        json_data = read_json_file(PATHS2)
        if json_data:
            folder_path = json_data.get("folder")
            input_file = json_data.get("input")

            input_file_path = f"{folder_path}/{input_file}"

            text = read_text_file(input_file_path)
            if text:
                frequencies = character_frequency(text)

                total_chars = sum(frequencies.values())

                sorted_frequencies = sorted(
                    frequencies.items(), key=lambda x: x[1], reverse=True
                )

                for char, freq in sorted_frequencies:
                    decimal_freq = freq / total_chars
                    print(f"Символ '{char}': {decimal_freq:.4f}")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()