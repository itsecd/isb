import logging

from reader import txt_reader

logging.basicConfig(level=logging.INFO)


def char_frequency(text : str) -> dict:
    """Does frequency analysis of text.
    :param text: str of text that is needed to analyse 
    :return: dict of symbol : frequency
    """
    try:
        frequency = {}
        for char in text:
            frequency[char] = text.count(char)
        frequency = {key : float(value) / len(text) for key, value in frequency.items()}
        frequency = sorted(frequency.items(), key=lambda item : item[1], reverse=True)
        return frequency
    except Exception as exc:
        logging.error(f"Frequency analisys error: {exc}")