import json

from math import sqrt
from scipy.special import erfc 

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

def bit_test(sequence: str) -> float:
    """
    Frequency bit test function.
    
    This function calculates the frequency bit test p-value for a given binary sequence.
    
    Parameters:
        sequence (str): The binary sequence for which the p-value is calculated.
        
    Returns:
        float: The p-value for the frequency bit test.
    """
    try:
        if not sequence:
            raise ValueError("Input sequence is empty")
        if not all(bit in ('0', '1') for bit in sequence):
            raise ValueError("Input sequence contains characters other than '0' and '1'")
        N = len(sequence)
        Sn = sum(1 if bit == "1" else -1 for bit in sequence) / sqrt(N)
        p_value = erfc(Sn / sqrt(2))
        return p_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None