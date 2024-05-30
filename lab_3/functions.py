import json
import logging
import os
from math import erfc, fabs, sqrt, pow
from mpmath import gammainc

logging.basicConfig(level=logging.INFO)

SEQUENCE_FILE_PATH = os.path.join('lab_2', 'sequence.json')
OUTPUT_FILE_PATH = os.path.join('lab_2', 'result.txt')
PROBABILITIES = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}

def bit_frequency_test(sequence: str) -> float:
    """
    Conducts a bit frequency test.

    Parameters:
    sequence: str - Input binary sequence as a string.

    Returns: float - Probability value indicating randomness.
    """
    try:
        int_sequence = list(map(int, sequence))
        adjusted_sequence = [-1 if bit == 0 else bit for bit in int_sequence]
        result_sum = fabs(sum(adjusted_sequence)) / sqrt(len(adjusted_sequence))
        p_value = erfc(result_sum / sqrt(2))
        return p_value
    except Exception as ex:
        logging.error(f"Error processing sequence: {ex}")

def test_identical_consecutive_bits(sequence: str) -> float:
    """
    Tests for identical consecutive bits.

    Parameters:
    sequence: str - Input binary sequence as a string.

    Returns: float - Probability value indicating randomness.
    """
    try:
        int_sequence = list(map(int, sequence))
        proportion_of_ones = sum(int_sequence) / len(int_sequence)
        
        if fabs(proportion_of_ones - 0.5) >= 2 / sqrt(len(int_sequence)):
            return 0.0
        
        changes = sum(1 for i in range(len(int_sequence) - 1) if int_sequence[i] != int_sequence[i + 1])
        expected_changes = 2 * len(int_sequence) * proportion_of_ones * (1 - proportion_of_ones)
        p_value = erfc(fabs(changes - expected_changes) / (2 * sqrt(2 * len(int_sequence)) * proportion_of_ones * (1 - proportion_of_ones)))
        
        return p_value
    except Exception as ex:
        logging.error(f"Error processing sequence: {ex}")

def longest_ones_sequence_test(sequence: str) -> float:
    """
    Tests the longest sequence of ones in blocks.

    Parameters:
    sequence: str - Input binary sequence as a string.

    Returns: float - Probability value indicating randomness.
    """
    try:
        int_sequence = list(map(int, sequence))
        block_size = 8
        blocks = [int_sequence[i:i + block_size] for i in range(0, len(int_sequence), block_size)]
        v_counts = {1: 0, 2: 0, 3: 0, 4: 0}
        
        for block in blocks:
            max_ones = 0
            current_ones = 0
            for bit in block:
                current_ones = current_ones + 1 if bit == 1 else 0
                if max_ones < current_ones:
                    max_ones = current_ones
            if max_ones in v_counts:
                v_counts[max_ones] += 1
            elif max_ones >= 4:
                v_counts[4] += 1

        chi_square = sum(pow(v_counts[i] - 16 * PROBABILITIES[i - 1], 2) / (16 * PROBABILITIES[i - 1]) for i in range(1, 5))
        p_value = gammainc(1.5, chi_square / 2)
        return p_value
    except Exception as ex:
        logging.error(f"Error processing sequence: {ex}")

if __name__ == "__main__":
    with open(SEQUENCE_FILE_PATH, 'r', encoding='utf-8') as file:
        sequences = json.load(file)

    cpp_sequence = sequences.get('cpp', '')
    java_sequence = sequences.get('java', '')

    with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as file:
        file.write("Results for C++ sequence\n")
        file.write(f"Frequency Bit Test: {bit_frequency_test(cpp_sequence)}\n")
        file.write(f"Identical Consecutive Bits Test: {test_identical_consecutive_bits(cpp_sequence)}\n")
        file.write(f"Longest Sequence of Ones in a Block Test: {longest_ones_sequence_test(cpp_sequence)}\n")

        file.write("\nResults for Java sequence\n")
        file.write(f"Frequency Bit Test: {bit_frequency_test(java_sequence)}\n")
        file.write(f"Identical Consecutive Bits Test: {test_identical_consecutive_bits(java_sequence)}\n")
        file.write(f"Longest Sequence of Ones in a Block Test: {longest_ones_sequence_test(java_sequence)}\n")
