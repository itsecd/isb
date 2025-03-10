from config.messages import ERRORS


def substitution(
    alphabet1: str,
    alphabet2: str,
    message: str,
    to_upper: bool = False
) -> str:
    """Encrypts the text with a substitution cipher.

    Args:
        alphabet1 (str): Input plaintext alphabet.
        alphabet2 (str): Output ciphertext alphabet.
        message (str): Input plaintext.
        to_upper (bool, optional): Flag that if True, causes alphabets
            and the message to be upper case. Defaults to False.

    Raises:
        ValueError: One of the alphabets is blank.
        ValueError: There are repeated characters
            in the alphabet of the input plaintext.
        ValueError: The ciphertext alphabet
            is smaller than the plaintext alphabet.

    Returns:
        str: Output ciphertext.
    """
    if not alphabet1 or not alphabet2:
        raise ValueError(ERRORS["alphabets_empty"])

    if not message:
        return ""

    if to_upper:
        alphabet1, alphabet2, message = map(
            str.upper,
            (alphabet1, alphabet2, message)
        )

    if len(alphabet1) != len(set(alphabet1)):
        raise ValueError(ERRORS["alphabet1_same_chars"])

    if len(alphabet2) < len(alphabet1):
        raise ValueError(ERRORS["alphabet2_shorter"])

    cipher_text = ""
    char_to_char = {char1: char2 for char1, char2 in zip(alphabet1, alphabet2)}

    for char in message:
        if char not in char_to_char:
            cipher_text += char
            continue

        cipher_text += char_to_char[char]

    return cipher_text


def caesar(
    alphabet: str,
    message: str,
    shift: int = 3,
    to_upper: bool = False
) -> str:
    """Encrypts the text with Caesar's cipher.

    Args:
        alphabet (str): An alphabet of input and output texts.
        message (str): Message to encrypt.
        shift (int, optional): Shift in the cipher. Defaults to 3.
        to_upper (bool, optional): Flag that if True, causes alphabets
            and the message to be upper case. Defaults to False.

    Raises:
        ValueError: The alphabet is empty.
        ValueError: The alphabet contains the same characters.

    Returns:
        str: Output ciphertext.
    """
    if not alphabet:
        raise ValueError(ERRORS["alphabet_empty"])

    if to_upper:
        alphabet, message = map(str.upper, (alphabet, message))

    if len(alphabet) != len(set(alphabet)):
        raise ValueError(ERRORS["alphabet_contains_same_chars"])

    if not message:
        return ""

    cipher_text = ""
    char_to_index = {char: idx for idx, char in enumerate(alphabet)}

    for char in message:
        if char not in char_to_index:
            cipher_text += char
            continue

        new_idx = (char_to_index[char] + shift) % len(alphabet)
        cipher_text += alphabet[new_idx]

    return cipher_text


def vigenere(
    alphabet: str,
    key: str,
    message: str,
    to_upper: bool = False
) -> str:
    """Encrypts the text of Vigenère's ciphers

    Args:
        alphabet (str): An alphabet of input and output texts.
        key (str): Key for encryption.
        message (str): Message to encrypt.
        to_upper (bool, optional): Flag that if True, causes alphabets
            and the message to be upper case. Defaults to False.

    Raises:
        ValueError: The key is empty.
        ValueError: The alphabet is empty.
        ValueError: The alphabet contains the same characters.
        ValueError: The key contains incorrect characters.

    Returns:
        str: Output ciphertext.
    """
    if not key:
        raise ValueError(ERRORS["key_empty"])

    if not alphabet:
        raise ValueError(ERRORS["alphabet_empty"])

    if to_upper:
        alphabet, key, message = map(str.upper, (alphabet, key, message))

    if len(alphabet) != len(set(alphabet)):
        raise ValueError(ERRORS["alphabet_contains_same_chars"])

    if not message:
        return ""

    cipher_text = ""
    alphabet_len = len(alphabet)
    char_to_index = {char: idx for idx, char in enumerate(alphabet)}

    msg_idx = 0
    for msg_char in message:
        key_char = key[msg_idx % len(key)]

        if msg_char not in char_to_index:
            cipher_text += msg_char
            continue

        msg_idx += 1

        shift1 = char_to_index.get(key_char)
        if shift1 is None:
            raise ValueError(ERRORS["key_invalid_char"].format(
                key_char=key_char)
            )

        shift2 = char_to_index.get(msg_char)

        cipher_text += alphabet[(shift1 + shift2) % alphabet_len]

    return cipher_text
