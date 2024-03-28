import constants_text
import key_for_task2 as key
import logging


def frequency_analysis(text: str) -> list:
    """
    Функция возращает список пар - буква и её частота появления в тексте. Список отсортирован в убывающем порядке.
    :param text:
    :return list:
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


if __name__ == "__main__":
    message = constants_text.text
    dictonary1 = frequency_analysis(message)
    print(dictonary1)

    for letter in key.dictonary_letter_value:
        message = message.replace(key.dictonary_letter_value[letter], letter)

    print(message)