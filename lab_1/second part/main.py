from frequency_analysis import *


def write_encrypted_text(filename: str, text: str) -> None:
    """
    Function to write text to file.

    """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


def read_file(filename: str) -> str:
    """
    Text reading function.

    :return: The input text.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def main():

    save_freq_to_json('frequencies/russian_freq.json', RUSSIAN_FREQ)

    encrypted_text = read_file('texts_and_key/encrypted_text.txt')

    text_freq = calculate_freq(encrypted_text)

    save_freq_to_json("frequencies/encrypted_freq.json", text_freq)

    rus_dict = load_freq_from_json('frequencies/russian_freq.json')
    encrypt_dict = load_freq_from_json('frequencies/encrypted_freq.json')

    encrypt_rus_dict = create_encrypt_rus_dict(encrypt_dict, rus_dict)

    key = load_freq_from_json('texts_and_key/key.json')

    decrypted_text = decrypt_text(encrypted_text, key)

    write_encrypted_text('texts_and_key/decrypted_text.txt', decrypted_text)


if __name__ == '__main__':
    main()