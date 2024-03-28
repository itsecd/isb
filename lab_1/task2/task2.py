import task2_key
import logging

from for_work_with_file import save_to_file, read_from_file, save_to_json_file


def frequency_analysis(text: str) -> list:
    """
    Perform frequency analysis on the given text and return a list of tuples containing each letter and its frequency.
    
    Parameters:
        text (str): The text to analyze.
        
    Returns:
        list: A list of tuples where each tuple contains a letter and its frequency in the text.
    """
    
    dictonary_of_frequency = {}
    len_text = len(text)
    try:
        for letter in text:
            if (letter not in dictonary_of_frequency.keys()):
                frequency = text.count(letter) / len_text
                dictonary_of_frequency[letter] = frequency
            else:
                continue
        result = sorted(dictonary_of_frequency.items(), key=lambda x: x[1], reverse=True)
        return result
    except Exception:
        logging.error(f"Ошибка в функции frequency_analysis(text): не удалось вернуть список")


def main():
    """
    Main function to perform frequency analysis on encrypted text and decrypt it using a predefined key.
    """

    text = read_from_file('lab_1/task2/encrypted_text.txt')
    analis = frequency_analysis(text)
    save_to_json_file('lab_1/task2/analis.json', analis)

    for letter in task2_key.dictonary_letter_value:
        text = text.replace(task2_key.dictonary_letter_value[letter], letter)
    save_to_file('lab_1/task2/decrypted_text.txt', text)

if __name__ == "__main__":
    main()