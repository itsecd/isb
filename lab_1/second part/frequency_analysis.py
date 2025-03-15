import json


RUSSIAN_FREQ = {
    ' ': 0.128675, 'о': 0.096456, 'и': 0.075312, 'е': 0.072292, 'а': 0.064841,
    'н': 0.061820, 'т': 0.061619, 'с': 0.051953, 'р': 0.040677, 'в': 0.039267,
    'м': 0.029803, 'л': 0.029400, 'д': 0.026983, 'я': 0.026379, 'к': 0.025977,
    'п': 0.024768, 'з': 0.015908, 'ы': 0.015707, 'ь': 0.015103, 'у': 0.013290,
    'ч': 0.011679, 'ж': 0.010673, 'г': 0.009867, 'х': 0.008659, 'ф': 0.007249,
    'й': 0.006847, 'ю': 0.006847, 'б': 0.006645, 'ц': 0.005034, 'ш': 0.004229,
    'щ': 0.003625, 'э': 0.002416, 'ъ': 0.000000
}



def save_freq_to_json(filename: str, d: dict) -> None:
    """
    Saves a frequency dictionary to a JSON file.

    :param filename: The name of the file to save the data.
    :param d: The dictionary containing character frequencies.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(d, file, ensure_ascii=False)


def load_freq_from_json(filename: str) -> dict:
    """
    Loads a frequency dictionary from a JSON file.

    :param filename: The name of the file to load data from.
    :return: The dictionary containing character frequencies.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def calculate_freq(text: str) -> dict:
    """
    Compute character frequencies in text.

    :param text: The input text.
    :return: A dictionary mapping characters to their frequency in the text.
    """

    sym_counts = {}

    for sym in text:

        if sym in sym_counts:

            sym_counts[sym] += 1

        else:

            sym_counts[sym] = 1

    total_symbs_count = sum(sym_counts.values())

    sym_freq = {}

    for char, count in sym_counts.items():

        freq = round(count / total_symbs_count, 6)

        sym_freq[char] = freq

    sorted_freq_list = sorted(sym_freq.items(), key=lambda item: item[1], reverse=True)

    sorted_freq = dict(sorted_freq_list)

    return sorted_freq


def create_encrypt_rus_dict(encrypt_freq: dict, rus_freq: dict) -> dict:
    """
    Matches ciphertext characters with Russian ones by frequency.

    :param encrypt_freq: A dictionary with character frequencies from the encrypted text.
    :param rus_freq: A dictionary with expected character frequencies in Russian.
    :return: A dictionary mapping encrypted characters to Russian characters.
    """

    encrypt_rus_dict = {}

    encrypt_freq_list = list(encrypt_freq.items())
    rus_freq_list = list(rus_freq.items())

    for i in range(min(len(rus_freq), len(encrypt_freq))):

        encrypt_rus_dict[encrypt_freq_list[i][0]] = rus_freq_list[i][0]

    return encrypt_rus_dict


def decrypt_text(encrypted_text: str, d: dict) -> str:
    """
    Decrypt text using a character mapping.

    :param encrypted_text: encrypted_text
    :param d: A dictionary mapping encrypted characters to decrypted characters.
    :return: The decrypted text.
    """

    decrypted_text = []

    for symb in encrypted_text:

        if symb in d:

            decrypted_text.append(d[symb])

        else:

            decrypted_text.append(symb)

    return ''.join(decrypted_text)