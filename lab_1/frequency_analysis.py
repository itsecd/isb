from work_with_files import read_txt_file, save_json_file
from typing import Dict

def frequency_analysis(path: str, probabilities: str) -> None:
    """
    Perform frequency analysis of symbols in the text file located at the given path
    and save the sorted probabilities to a JSON file.

    :param path: Path to the text file for frequency analysis.
    :param probabilities: Path to the output JSON file for sorted probabilities.
    """
    try:
        frequencies: Dict[str, int] = {}
        text_length: int = 0

        text: str = read_txt_file(path)
        text_length = len(text)

        for symbol in text:
            if symbol != '\n':
                if symbol in frequencies:
                    frequencies[symbol] += 1
                else:
                    frequencies[symbol] = 1

        probabilitie: Dict[str, float] = {symbol: frequency / text_length for symbol, frequency in frequencies.items()}
        sorted_probabilities: Dict[str, float] = {k: v for k, v in sorted(probabilitie.items(), key=lambda item: item[1], reverse=True)}  

        save_json_file(probabilities, sorted_probabilities)

    except Exception as e:
        print(f"An error occurred: {e}")