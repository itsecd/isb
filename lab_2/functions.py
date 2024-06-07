import json
import math

from scipy.special import erfc, gammainc

from constants import PI


def read_json(file_path: str) -> dict:
    """
    Read JSON from file.
    Args:
    - file_path (str): The path to the JSON file to be read.
    Returns:
    - dict: The JSON data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exist") from e
    except Exception as e:
        raise e


def frequency_test(sequence: str) -> float:
    """
    Perform the Frequency (Monobit) Test.
    Args:
    - sequence (str): Binary sequence to be tested.
    Returns: 
    - float: P-value of the test.
    """
    try:
        sequence_length = len(sequence)
        count_ones = sequence.count('1')
        count_zeros = sequence.count('0')

        if count_ones + count_zeros != sequence_length:
            raise ValueError("The sequence contains non-binary values.")

        sum_value = count_ones - count_zeros
        observed_statistic = abs(sum_value) / math.sqrt(sequence_length)
        p_value = erfc(observed_statistic / math.sqrt(2))
        return p_value
    except Exception as e:
        print(f"Error in frequency_test: {e}")
        raise e


def runs_test(sequence: str) -> float:
    """
    Perform the Runs Test.
    Args:
    - sequence: Binary sequence to be tested.
    Returns: 
    - float: P-value of the test.
    """
    try:
        sequence_length = len(sequence)
        pi = sequence.count('1') / sequence_length

        if abs(pi - 0.5) > (2 / math.sqrt(sequence_length)):
            return 0.0

        num_runs = 1
        for i in range(1, sequence_length):
            if sequence[i] == sequence[i - 1]:
                num_runs += 1

        p_value = erfc((math.fabs(num_runs - 2 * sequence_length * pi * (1 - pi))) /
                       (2 * math.sqrt(2 * sequence_length) * pi * (1 - pi)))
        return p_value
    except Exception as e:
        print(f"Error in runs_test: {e}")
        raise e


def longest_run_of_ones_in_block(block) -> int:
    """
    Find the longest run of 1s in a block.
    Args:
    - block (str): A binary string block.
    Returns:
    - int: The length of the longest run of 1s.
    """
    max_run = 0
    current_run = 0

    for bit in block:
        if bit == '1':
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 0

    return max_run


def longest_run_test(sequence: str, block_size: int = 8) -> float:
    """
    Perform the Longest Run of Ones in a Block Test.
    Args:
    - sequence (str): Binary sequence to be tested.
    - block_size (int): Size of each block (default is 8).
    Returns:
    - float: P-value of the test.
    """
    sequence_length = len(sequence)
    num_blocks = sequence_length // block_size

    if num_blocks == 0:
        raise ValueError("Sequence is too short for the given block size.")

    longest_runs = []
    for i in range(num_blocks):
        block = sequence[i * block_size:(i + 1) * block_size]
        longest_runs.append(longest_run_of_ones_in_block(block))

    v = [0] * 4
    for run in longest_runs:
        match run:
            case 0 | 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case _:
                v[3] += 1

    expected_counts = [num_blocks * PI[i] for i in range(4)]

    chi_square = sum((observed - expected) ** 2 / expected for observed,
    expected in zip(v, expected_counts))
    p_val = gammainc(3 / 2, chi_square / 2)

    return p_val
