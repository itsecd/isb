
from collections import Counter

def calculate_frequencies(text):
    """
    Calculate frequency of all symbols

    :param text: text
    :return: frequency
    """
    freq = Counter(text)

    total_chars = sum(freq.values())
    relative_freq = {char: count / total_chars for char, count in freq.items()}

    return relative_freq

def create_key(russian_freq, my_freq):
    """
        Compare our frequency and table frequency

        :param russian_freq: table frequency
        :param my_freq: our frequency
        :return: key to decode
        """
    sorted_russian_freq = sorted(russian_freq.items(), key=lambda item: item[1], reverse=True)
    sorted_my_freq = sorted(my_freq.items(), key=lambda item: item[1], reverse=True)

    encryption_key = {}
    for (russian_char, _), (my_char, _) in zip(sorted_russian_freq, sorted_my_freq):
        encryption_key[my_char] = russian_char

    return encryption_key

def decode_text(text, encryption_key):
    """
    Replace symbols according to the key

    :param text: text to decode
    :param encryption_key: key
    :return: text
    """
    encrypted_text = []

    for char in text:
        if char in encryption_key:
            encrypted_text.append(encryption_key[char])
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)
