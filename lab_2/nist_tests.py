import json
import logging
import math
import os

import mpmath

logging.basicConfig(level=logging.INFO)

PI = {1: 0.2148, 2: 0.3672, 3: 0.2305, 4: 0.1875}


class NistTest:
    """
    This class represents a NIST test on a given sequence of bits.

    Attributes:
    sequence : str
        The sequence of bits.
    len:int
        sequence length

    Methods:
    bitwise_test(self) -> bool:
        Performs the bitwise test on the sequence of bits.

    same_bits_test(self) -> bool:
        Performs the same bits test on the sequence of bits.

    split_bits(self) -> list:
        Splits the sequence of 8 bits into a list.

    largest_number_of_units(self, blocks: list) -> dict:
        Calculates the largest number of consecutive zeros or ones in the sequence.

    length_test(self, dictionary: dict) -> bool:
        Performs the length test on the sequence of bits using the largest number of units calculated.

    """

    def __init__(self, bit_sequence: str) -> None:

        self.sequence = bit_sequence
        self.len = len(bit_sequence)

    def bitwise_test(self) -> float:
        """
        Performs the bitwise test on the sequence of bits.

        returns:
        float:p-value.
        """
        try:
            sum = 0
            for i in self.sequence:
                if int(i) == 1:
                    sum += 1
                else:
                    sum -= 1
            sum = math.fabs(sum) / math.sqrt(self.len)
            p_value = math.erfc(sum / math.sqrt(2))
            return p_value
        except Exception as ex:
            logging.error(f"ZeroDivisionError: {ex.message}\n{ex.args}\n")

    def same_bits_test(self) -> float:
        """
        Performs the same bits test on the sequence of bits.

        returns:
        float:p-value.
        """
        try:
            counter = self.sequence.count("1")
            counter *= 1 / self.len
            if abs(counter - 0.5) < 2 / math.sqrt(self.len):
                v = 0
                for i in range(self.len - 1):
                    if self.sequence[i] != self.sequence[i + 1]:
                        v += 1
                num = abs(v - 2 * self.len * counter * (1 - counter))
                denom = 2 * math.sqrt(2 * self.len) * counter * (1 - counter)
                p_value = math.erfc(num / denom)
            else:
                p_value = 0
            return p_value
        except Exception as ex:
            logging.error(f"ZeroDivisionError: {ex.message}\n{ex.args}\n")

    def split_bits(self) -> list:
        """
        Splits the sequence of 8 bits into a list.

        returns:
        list:list of integers representing the split bits.
        """
        blocks = []
        quantity = self.len - (self.len % 8)
        for i in range(0, quantity, 8):
            block = self.sequence[i : i + 8]
            blocks.append(block)
        return blocks

    def largest_number_of_units(self, blocks: list) -> dict:
        """
        Calculates the largest number of consecutive zeros or ones in the sequence.

        parameters:
        blocks: list of blocks of bits.

        returns:
        dict: dictionary containing the count of the largest units of consecutive zeros or ones.
        """
        try:
            unit_counts = {}
            for block in blocks:
                counter = 0
                max_counter = 0
                for i in block:
                    if int(i) == 1:
                        counter += 1
                        max_counter = max(max_counter, counter)
                        if max_counter > 4:
                            max_counter = 4
                    else:
                        counter = 0
                if max_counter in unit_counts:
                    unit_counts[max_counter] += 1
                else:
                    unit_counts[max_counter] = 1
            sorted_dict = dict(sorted(unit_counts.items(), key=lambda x: x[1]))
            return sorted_dict
        except Exception as ex:
            logging.error(f"TypeError block wasn't str: {ex.message}\n{ex.args}\n")

    def length_test(self, dictionary: dict) -> float:
        """
        Performs the length test on the sequence of bits
        using the largest number of units calculated.

        parameters:
        dictionary: dictionary containing the count of the
        largest units of consecutive zeros or ones.

        returns:
        float:p-value.
        """
        try:
            square_x = 0
            for i, value in dictionary.items():
                square_x += pow(value - 16 * PI[i], 2) / (16 * PI[i])
            p_value = mpmath.gammainc(3 / 2, square_x / 2)
            return p_value
        except Exception as ex:
            logging.error(
                f"Length of the dictionary is longer than number of pi-constants: {ex.message}\n{ex.args}\n"
            )


if __name__ == "__main__":

    with open(os.path.join("lab_2", "sequence.json"), "r") as file:
        seq = json.load(file)

    sequence_java = NistTest(seq["java_sequence"])
    print(sequence_java.bitwise_test())
    print(sequence_java.same_bits_test())
    print(
        sequence_java.length_test(
            sequence_java.largest_number_of_units(sequence_java.split_bits())
        )
    )
    sequence_c = NistTest(seq["c_sequence"])
    print(sequence_c.bitwise_test())
    print(sequence_c.same_bits_test())
    print(
        sequence_c.length_test(
            sequence_c.largest_number_of_units(sequence_c.split_bits())
        )
    )
