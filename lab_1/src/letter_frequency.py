def calculate_frequency(message: str, skip_break: bool = True) -> list:
    """Calculates the frequency of occurrence of letters in a given text.

    Args:
        message (str): Input Text.
        skip_break (bool, optional): Skips break lines. Defaults to True.

    Returns:
        list: A list containing letters and frequencies.
    """
    result = []
    if not message:
        return result

    message_len = len(message)

    for char in set(message):
        if skip_break and char == "\n":
            continue

        frequency = round(message.count(char) / message_len, 6)
        result.append([char, frequency])

    result.sort(key=lambda _: _[1], reverse=True)

    return result


def replace_by_freq(text: str, cip_freq: dict, real_freq: dict) -> str:
    """Replaces letters in the ciphertext based on the calculated frequencies
    and frequencies of the real letters.

    It is worth noting that the text needs further manual processing.

    Args:
        text (str): Input ciphertext.
        cip_freq (dict): Cipher-letter frequencies.
        real_freq (dict): Frequencies of real letters.

    Returns:
        str: Output text.
    """
    replace_dict = {}

    for cip, real in zip(cip_freq, real_freq):
        replace_dict[cip[0]] = real[0]
        print(f"'{cip[0]}' => '{real[0]}'")

    replaced_text = "".join(replace_dict.get(char, char) for char in text)

    return replaced_text
