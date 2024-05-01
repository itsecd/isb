import json

from math import sqrt
from scipy.special import erfc
from scipy.special import gammainc
from constants import BLOCK_SIZE,PATH,PI_VALUES


def read_json_file(file_path: str) -> dict:
    """
    Function to read data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Dictionary containing data from the JSON file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:   
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while reading file '{file_path}': {e}.")
        return {}


def frequency_bit_test(sequency: str) -> float:
    """
    Frequency bit test function.
    
    This function calculates the frequency bit test p-value for a given binary sequency.
    
    Parameters:
        sequency (str): The binary sequency for which the p-value is calculated.
        
    Returns:
        float: The p-value for the frequency bit test.
    """
    try:
        if not sequency:
            raise ValueError("Input sequence is empty")
        if not all(bit in ('0', '1') for bit in sequency):
            raise ValueError("Input sequence contains characters other than '0' and '1'")
        N = len(sequency)
        Sn = sum(1 if bit == "1" else -1 for bit in sequency) / sqrt(N)
        p_value = erfc(abs(Sn) / sqrt(2))
        return p_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

def consecutive_bits_test(sequency: str) -> float:
    """
    Calculates the p-value for the consecutive bit test.
    This test checks the proportion of runs in the sequency. A run is a consecutive
    sequency of identical bits (either '0's or '1's).
    Parameters:
        sequency (str): The binary sequency for which the p-value is calculated.
    Returns:
        float: The p-value for the consecutive bit test.
    """
    try:
        sequency_length = len(sequency)
        proportion_of_ones = sequency.count("1") / sequency_length
        deviation_threshold = 2 / sqrt(sequency_length)
        if abs(proportion_of_ones - 0.5) >= deviation_threshold:
            return 0
        transition_count = sum(1 if sequency[i] != sequency[i + 1] else 0 for i in range(sequency_length - 1))
        p_value = erfc(
            (abs(transition_count - 2 * sequency_length * proportion_of_ones * (1 - proportion_of_ones)))
            / (2 * sqrt(2 * sequency_length) * proportion_of_ones * (1 - proportion_of_ones))
        )
        return p_value
    except Exception as error:
        print(f"An error occurred: {error}")
        return None
from scipy.special import gammainc


def long_sequence_units_test(sequency: str) -> float:
    """
    Calculate the p-value for the long sequence units test.

    This test checks for the proportion of long sequencys of consecutive '1's or '0's in the sequency.

    Parameters:
        sequency (str): The binary sequency for which the p-value is calculated.

    Returns:
        float: The p-value for the long sequence units test.
    """
    try:
        blocks = [
            sequency[i : i + BLOCK_SIZE] for i in range(0, len(sequency), BLOCK_SIZE)
        ]
        V = {"v1": 0, "v2": 0, "v3": 0, "v4": 0}
        for block in blocks:
            current_ones = 0
            max_ones = 0
            for bit in block:
                if bit == "1":
                    current_ones += 1
                    max_ones = max(max_ones, current_ones)
                else:
                    current_ones = 0
            case = min(max_ones, 4)
            V[f"v{case}"] += 1
        X = sum(
            ((V[f"v{i+1}"] - 16 * PI_VALUES[i]) ** 2) / (16 * PI_VALUES[i])
            for i in range(4)
        )
        p_value = gammainc(1.5, X / 2)
        return p_value
    except Exception as error:
        print(f"An error occurred: {error}")
        return None


def main() -> None:
    data = read_json_file(PATH)
    for language, sequency in data.items():
        print(f"Язык генерации: {language}")
        p_value_frequency_bit_test = frequency_bit_test(sequency)
        print(f"p-value frequency_bit_test: {p_value_frequency_bit_test}")
        p_value_consecutive_bits_test = consecutive_bits_test(sequency)
        print(f"p-value p_value_consecutive_bits_test: {p_value_consecutive_bits_test}")
        p_value_long_sequence_units_test = long_sequence_units_test(sequency)
        print(f"p-value p_value_long_sequence_units_test: {p_value_long_sequence_units_test}")
        print()

        
if __name__ == "__main__":
    main()

