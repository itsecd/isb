def make_dict_upper(data: dict[str, str]) -> dict[str, str]:
    """
    The function changes the case of the key and value
    :param data: dictionary to make changes to
    :return: dictionary with keys and values in uppercase
    """
    result = dict()
    for key, value in data.items():
        result[key.upper()] = value.upper()

    return result


def text_encryption(data: str, key: dict[str, str]) -> str:
    """
    The function encrypts the text with the specified key
    :param data: The text that needs to be encrypted
    :param key: The specified key
    :return: Encrypted text
    """
    result = ""

    key = make_dict_upper(key)
    for symbol in data.upper():
        new_symbol = key.get(symbol)

        if new_symbol is not None:
            result += new_symbol
        else:
            result += symbol

    return result
