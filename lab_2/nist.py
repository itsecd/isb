import logging
import math
import mpmath

from constants import MAX_LENGTH_BLOCK, PI, SEQUENCE_PATH, TEST_RESULTS
from file_work import json_reader, txt_writer

logging.basicConfig(level=logging.INFO)


class NIST:
    """
    NIST Statistical Test Suite implementation for binary sequences.

    Attributes:
        sequence (str): The binary sequence on which the tests are performed.
        len_sequence (int): The length of the binary sequence.

    Methods:
        bitwise_frequency_test() -> float:
            Perform the Bitwise Frequency Test and return the p-value.

        consecutive_bits_test() -> float:
            Perform the Consecutive Bits Test and return the p-value.

        longest_sequence_units_test() -> float:
            Perform the Longest Run of Ones in a Block Test and return the p-value.
    """

    def __init__(self, seq: str) -> None:
        """
        Initialize NistTests with params
        :param seq: (str) input sequence of bits
        :return None:
        """
        self.sequence = seq
        self.len_sequence = len(seq)

    def frequency_bitwise_test(self) -> float:
        """
        Perform the frequency bitwise test and return the p-value.
        :return: float p-value of the test
        """
        try:
            x_list = [1 if bit == '1' else -1 for bit in self.sequence]
            sum_list = sum(x_list)

            s_n = math.fabs(sum_list) / math.sqrt(self.len_sequence)

            p_value = math.erfc(s_n / math.sqrt(2))
            return p_value
        except Exception as ex:
            logging.error(f"Error during the test execution: {ex}\n")

    def consecutive_bits_test(self) -> float:
        """
        Perform the same consecutive bits test and return the p-value.
        :return: float p-value of the test
        """
        try:
            sum_list = self.sequence.count("1") / self.len_sequence
            if abs(sum_list - 0.5) >= (2 / math.sqrt(self.len_sequence)):
                return 0

            v_n = 0
            v_n += sum(1 if self.sequence[i] != self.sequence[i + 1] else 0 for i in range(self.len_sequence - 1))

            p_value = math.erfc(abs(v_n - 2 * self.len_sequence * sum_list * (1 - sum_list)) / (
                    2 * math.sqrt(2 * self.len_sequence) * sum_list * (1 - sum_list)))
            return p_value
        except Exception as ex:
            logging.error(f"Error during the test execution: {ex}\n")

    def longest_sequence_in_block_test(self) -> float:
        """
        Perform the longest run of ones in a block test and return the p-value.
        :return: float p-value of the test
        """
        try:
            block_max_len = {}
            for step in range(0, self.len_sequence, MAX_LENGTH_BLOCK):
                block = self.sequence[step:step + MAX_LENGTH_BLOCK]
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
    sequences = json_reader(SEQUENCE_PATH)
    test_cpp = NIST(sequences["cpp"])
    test_java = NIST(sequences["java"])

    txt_writer(TEST_RESULTS, f'C++\n\nfrequency_bitwise_test: {NIST.frequency_bitwise_test(test_cpp)}\n'
                             f'consecutive_bits_test: {NIST.consecutive_bits_test(test_cpp)}\n'
                             f'longest_sequence_in_block_test: {NIST.longest_sequence_in_block_test(test_cpp)}\n\n'
                             f'Java\n\nfrequency_bitwise_test: {NIST.frequency_bitwise_test(test_java)}\n'
                             f'consecutive_bits_test: {NIST.consecutive_bits_test(test_java)}\n'
                             f'longest_sequence_in_block_test: {NIST.longest_sequence_in_block_test(test_java)}')
    logging.info('Results successful written in file')
