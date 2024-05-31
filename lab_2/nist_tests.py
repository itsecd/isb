import logging
import math
import mpmath

from constants import MAX_LENGTH_BLOCK, PI, SEQUENCE_PATH, TEST_RESULTS
from file_work import json_reader, txt_writer

logging.basicConfig(level=logging.DEBUG, filemode='w')


def frequency_bitwise_test(sequence: str) -> float:
    """
    Perform the frequency bitwise test and return the p-value.
    :param sequence: str binary sequence
    :return: float p-value of the test
    """
    try:
        
        n = len(sequence)
        count_ones = sequence.count('1')
        count_zeroes = n - count_ones

        s = abs(count_ones - count_zeroes) / math.sqrt(n)

        p_value = math.erfc(s / math.sqrt(2))
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


def consecutive_bits_test(sequence: str) -> float:
    """
    Perform the same consecutive bits test and return the p-value.
    :param sequence: str binary sequence
    :return: float p-value of the test
    """
    try:

        size_seq = len(sequence)
        s = sequence.count('1') / size_seq
        if not (abs(s - 0.5) < (2 / math.sqrt(size_seq))):
            return 0.0        
        
        v = sum(1 for i in range(size_seq - 1)
                   if sequence[i] != sequence[i + 1])
        p_value = mpmath.erfc(abs(v - 2 * size_seq * s * (1 - s)) /
                           (2 * math.sqrt(2 * size_seq) * s * (1 - s)))
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


def longest_sequence_in_block_test(sequence: str) -> float:
    """
    Perform the longest run of ones in a block test and return the p-value.
    :param sequence: str binary sequence
    :return: float p-value of the test
    """
    try:

        blocks = [sequence[i:i + MAX_LENGTH_BLOCK] for i in range(0, len(sequence), MAX_LENGTH_BLOCK)]
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for block in blocks:
            max_seq = max(len(seq_ones) for seq_ones in block.split('0'))
            match max_seq:
                case max_seq if max_seq < 2:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case max_seq if max_seq > 3:
                    v[4] += 1

        x = sum(math.pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i]) for i in range(0, 4))
        p_value = mpmath.gammainc(3 / 2, x / 2)
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


if __name__ == "__main__":
    sequences = json_reader(SEQUENCE_PATH)
    test_cpp = sequences["cpp"]
    test_java = sequences["java"]

    txt_writer(TEST_RESULTS, f'C++\n\nfrequency_bitwise_test: {frequency_bitwise_test(test_cpp)}\n'
                             f'consecutive_bits_test: {consecutive_bits_test(test_cpp)}\n'
                             f'longest_sequence_in_block_test: {longest_sequence_in_block_test(test_cpp)}\n\n'
                             f'Java\n\nfrequency_bitwise_test: {frequency_bitwise_test(test_java)}\n'
                             f'consecutive_bits_test: {consecutive_bits_test(test_java)}\n'
                             f'longest_sequence_in_block_test: {longest_sequence_in_block_test(test_java)}')
 