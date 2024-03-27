import logging
import math
import mpmath

from constants import MAX_LENGTH_BLOCK, PI, SEQ_PATH
from file_util import json_reader

logging.basicConfig(level=logging.DEBUG, filename="tests.txt", filemode='w')


def frequency_bitwise_test(seq: str) -> float:
    """
    Perform the frequency bitwise test and return the p-value.
    :param seq: str input binary sequence
    :return: float p-value of the test
    """
    try:
        x_list = [1 if bit == '1' else -1 for bit in seq]
        sum_list = sum(x_list)

        s_n = math.fabs(sum_list) / math.sqrt(len(seq))

        p_value = math.erfc(s_n / math.sqrt(2))
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


def consecutive_bits_test(seq: str) -> float:
    """
    Perform the same consecutive bits test and return the p-value.
    :param seq: str input binary sequence
    :return: float p-value of the test
    """
    try:
        sum_list = seq.count("1") / len(seq)
        if abs(sum_list - 0.5) >= (2 / math.sqrt(len(seq))):
            return 0

        v_n = 0
        v_n += sum(1 if seq[i] != seq[i + 1] else 0 for i in range(len(seq) - 1))

        p_value = math.erfc(abs(v_n - 2 * len(seq) * sum_list * (1 - sum_list)) / (
                2 * math.sqrt(2 * len(seq)) * sum_list * (1 - sum_list)))
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


def longest_sequence_in_block_test(seq: str) -> float:
    """
    Perform the longest run of ones in a block test and return the p-value.
    :param seq: str input binary sequence
    :return: float p-value of the test
    """
    try:
        block_max_len = {}
        for step in range(0, len(seq), MAX_LENGTH_BLOCK):
            block = seq[step:step + MAX_LENGTH_BLOCK]
            max_length, length = 0, 0
            for bit in block:
                length = length + 1 if bit == "1" else 0
                max_length = max(max_length, length)
            block_max_len[max_length] = block_max_len.get(max_length, 0) + 1

        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for i in block_max_len:
            key = min(i, 4)
            v[key] += block_max_len[i]

        xi_square = 0
        for i in range(4):
            xi_square += math.pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])

        return mpmath.gammainc(3 / 2, xi_square / 2)
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


if __name__ == "__main__":
    sequences = json_reader(SEQ_PATH)

    logging.info("frequency bitwise test result for C++: %s", frequency_bitwise_test(sequences["cpp"]))
    logging.info("consecutive bits test result for C++: %s", consecutive_bits_test(sequences["cpp"]))
    logging.info("longest sequence in block test result for C++: %s", longest_sequence_in_block_test(sequences["cpp"]))

    logging.info("frequency bitwise test result for Java: %s", frequency_bitwise_test(sequences["java"]))
    logging.info("consecutive bits test result for Java: %s", consecutive_bits_test(sequences["java"]))
    logging.info("longest sequence in block test result for Java: %s",
                 longest_sequence_in_block_test(sequences["java"]))

