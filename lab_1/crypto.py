RUSSIAN_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_cipher(text: str, key: int, alphabet_is_english: bool) -> str:
    """Caesar's Cipher
    Args:
      text: message
      key: alphabet shift
      alphabet_is_english: flag to check that the alphabet is English
    Returns:
      encrypted message
    """
    if alphabet_is_english:
        alphabet = ENGLISH_ALPHABET
    else:
        alphabet = RUSSIAN_ALPHABET
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            index = (alphabet.index(letter) + key) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += letter
    return encrypted_text


def frequency_analysis(text: str) -> dict:
    """Frequency analysis of the message
    Args:
      text: message
    Returns:
      A dictionary where the keys are the symbols of the message and their meanings are the frequency of occurrence
    """
    frequency = {}
    for letter in text:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    for key in frequency:
        frequency[key] = frequency[key] / len(text)
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))


def decryption_by_key(code: str, key: dict) -> str:
    """The function for decryption by key helps to get rid of a large number of replace
    Args:
      code: encrypted message
      key: encryption key
    Returns:
      the decrypted message
    """
    for letter in key:
        code = code.replace(letter, key[letter])
    return code
