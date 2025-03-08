def text_encryption(data: str, key: dict[str, str]) -> str:
    """
    The function encrypts the text with the specified key
    :param data: The text that needs to be encrypted
    :param key: The specified key
    :return: Encrypted text
    """
    result = ""

    for symbol in data.upper():
        result += str(key.get(symbol, None))

    return result
