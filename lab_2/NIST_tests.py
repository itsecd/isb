import logging

from math import sqrt, erfc
from mpmath import gammainc

PI = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}

def frequency_bitwise_test(sequence: str) -> float:
    """
    Calculate the frequency bitwise test for a given binary sequence.

        Parameters:
            sequence (str): The binary sequence for which the test is to be performed.

        Returns:
            float: The result of the frequency bitwise test.
            
    """
    try:
        s_n = sum([(-1 if bit == '0' else 1) for bit in sequence]) / sqrt(len(sequence))
        return erfc(abs(s_n) / sqrt(2))
    except Exception as e:  
        logging.error(f"error in 'frequency_bitwise_test' {e}")


def same_consecutive_bits_test(sequence: str) -> float:
    """
    This function calculates a statistical test value based on the input binary sequence.

        Parameters:
            sequence (str): The binary sequence for which the test is to be performed.

        Returns:
            float: The statistical test value calculated based on the input sequence.
    """
    try:
        percentage_of_units = sequence.count("1") / len(sequence)        
        if abs((percentage_of_units - 0.5)) >= 2 / sqrt(len(sequence)):
            return 0         
        v_n = sum([(0 if sequence[i] == sequence[i + 1] else 1) for i in range(0, (len(sequence) - 1))])
        return erfc((abs(v_n - (2 * len(sequence) * percentage_of_units * (1 - percentage_of_units))))
                    / (2 * sqrt(2 * len(sequence)) * percentage_of_units * (1 - percentage_of_units)))
    except Exception as e:
        logging.error(f"error in 'same_consecutive_bits_test' {e}")


def longest_sequence_test(sequence: str, block_size: int = 8) -> float:
    """
    This function calculates a statistical test 
    value based on the longest sequences of '1's in 
    blocks of the input binary sequence.

        Parameters:
            sequence (str): The binary sequence for which the test is to be performed.
            block_size (int): The size of each block to divide the sequence into (default is 8).

        Returns:
            float: The statistical test value calculated based on the longest sequences of '1's in the blocks.
    """
    try:
        blocks = [sequence[i : i + block_size] for i in range(0, len(sequence), block_size)]
        number_of_ones = [(maximum_sequence_length(i)) for i in blocks]

        v = {0: 0, 1: 0, 2: 0, 3: 0}

        for i in number_of_ones:
            match i:
                case 0 | 1:                
                    v[0] += 1
                case 2:
                    v[1] += 1
                case 3:
                    v[2] += 1
                case _:
                    v[3] += 1
        chi = sum([((pow(v[i] - 16 * PI[i], 2)) / (16 * PI[i])) for i in range(0, 4)])
        return gammainc(1.5, (chi / 2))

    except Exception as e:
        logging.error(f"error in 'longest_sequence_test' {e}")


def maximum_sequence_length(sequence: str) -> int:
    """ 
    This function calculates the length of the maximum consecutive 
    sequence of '1's in the input binary sequence.

        Parameters:
            sequence (str): The binary sequence for which the test is to be performed.

        Returns:
            int: The length of the maximum consecutive sequence of '1's in the input sequence.
    """
    max_len = 0
    cur_len = 0
    try:        
        for i in sequence:
            cur_len = cur_len + 1 if i == "1" else 0
            max_len = max(max_len, cur_len)           
        return max_len
    except Exception as e:
       logging.error(f"error in 'maximum_sequence_length' {e}")