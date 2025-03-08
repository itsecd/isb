def text_encryption(data: str, key: dict[str, str]) -> str:
    """
    The function encrypts the text with the specified key
    :param data: The text that needs to be encrypted
    :param key: The specified key
    :return: Encrypted text
    """
    result = ""

    for symbol in data:
        new_symbol = key.get(symbol.upper())

        if new_symbol is not None:
            if symbol.isupper():
                result += new_symbol
            else:
                result += new_symbol.lower()
        else:
            result += symbol

    return result
