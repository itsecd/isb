import logging
import math
import mpmath

logging.basicConfig(level=logging.INFO)

pi = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}

class NistTests:
    """ NIST tests sequence checks for randomness
       Args:
           sequence: a pseudorandom sequence
           length: the length of the sequence
       Methods:
           frequency_bitwise_test: Frequency bitwise test
           consecutive_bits_test: Test for the same consecutive bits
           longest_sequence_test: The test for the longest sequence of units in the block
           length_greatest_subsequence: Determining the length of the largest subsequence of units
    """
    BLOCK_LENGTH = 8

    def __init__(self, sequence: str) -> None:
        """Class initializer"""
        self.sequence = sequence
        self.length = len(sequence)

    def frequency_bitwise_test(self) -> float:
        """Frequency bitwise test
         Returns:
           Probability that the generator produces values comparable to the reference (P-value)
         """
        try:
            s_sum = 0
            for bit in self.sequence:
                if int(bit) == 1:
                    s_sum += 1
                else:
                    s_sum -= 1
            s = math.fabs(s_sum) / math.sqrt(self.length)
            return math.erfc(s / math.sqrt(2))
        except ZeroDivisionError as error:
            logging.error("Division be zero")
        except Exception as error:
            logging.error(error)

    def consecutive_bits_test(self) -> float:
        """Test for the same consecutive bits
         Returns:
           P-value
         """
        try:
            percentage_units = self.sequence.count("1") / self.length
            if not (abs(percentage_units - 0.5) < (2 / math.sqrt(self.length))):
                return 0
            v_n = 0
            for i in range(self.length - 1):
                if self.sequence[i] != self.sequence[i + 1]:
                    v_n += 1
            numerator = abs(v_n - 2 * self.length * percentage_units * (1 - percentage_units))
            denominator = 2 * math.sqrt(2 * self.length) * percentage_units * (1 - percentage_units)
            return math.erfc(numerator / denominator)
        except ZeroDivisionError as error:
            logging.error("Division be zero")
        except Exception as error:
            logging.error(error)

    def longest_sequence_test(self) -> float:
        """The test for the longest sequence of units in the block
         Returns:
             P-value
         """
        try:
            block_max_len = {}
            for step in range(0, self.length, self.BLOCK_LENGTH):
                block = self.sequence[step:step + self.BLOCK_LENGTH]
                block_length = self.length_greatest_subsequence(block, "1")
                if block_length not in block_max_len:
                    block_max_len[block_length] = 1
                else:
                    block_max_len[block_length] += 1
            v = {1: 0, 2: 0, 3: 0, 4: 0}
            for i in block_max_len:
                if i <= 1:
                    v[1] += block_max_len[i]
                elif i == 2:
                    v[2] += block_max_len[i]
                elif i == 3:
                    v[3] += block_max_len[i]
                else:
                    v[4] += block_max_len[i]
            xi_square = 0
            for i in range(4):
                xi_square += math.pow(v[i + 1] - 16 * pi[i], 2) / (16 * pi[i])
            return mpmath.gammainc(3 / 2,  xi_square / 2)
        except Exception as error:
            logging.error(error)

    @staticmethod
    def length_greatest_subsequence(sequence: str, item: str) -> int:
        """ Determining the length of the largest subsequence of units
         Args:
           sequence: a pseudorandom sequence
           item: the element whose maximum sequence length needs to be found
         Returns:
           The length of the maximum sequence
         """
        max_lenght = 0
        length = 0
        for letter in sequence:
            if letter == item:
                length += 1
                max_lenght = max(max_lenght, length)
            else:
                length = 0
        return max_lenght

    def __str__(self) -> str:
        """The function of printing test results"""
        response = ""
        response += f"Частотный побитовый тест: {self.frequency_bitwise_test()}\n"
        response += f"Тест на одинаковые подряд идущие биты: {self.consecutive_bits_test()}\n"
        response += f"Тест на самую длинную послед. единиц в блоке: {self.longest_sequence_test()}\n"
        return response