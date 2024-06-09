import math
import mpmath


def frequency_bit_test(bit_string: str) -> float:
    """
    Performs frequency bit test.

    The frequency bit test is a statistical test used to determine whether a sequence of bits is random.
    The test is based on the assumption that the probability of a 0 or 1 bit occurring is equal.
    The test statistic is the sum of the differences between the number of 0s and 1s in the sequence.
    The p-value is the probability of obtaining a test statistic as extreme as, or more extreme than,
    the observed test statistic, assuming that the sequence is random.

    Args:
        bit_string (str): The bit sequence to test.

    Returns:
        float: The p-value of the test. 
        If the value tends to 1, then it is said that the generator tends to be ideal.
        If the P-value tends to 0, the generator is completely predictable.

    Raises:
        ValueError: the input string is not a bitstring.
    """

    if any([symbol not in ['0','1'] for symbol in bit_string]):
        raise ValueError("This is not a bitstring")

    sum = 0
    for bit in bit_string:
        if bit == '1':
            sum += 1
        else:
            sum += -1

    p_value = math.erfc(abs(sum / math.sqrt(len(bit_string)) / math.sqrt(2)))
    return p_value


def consecutive_bits_test(bit_string: str) -> float:
    """
    Performs consecutive bits test.

    The test is about finding all sequences of the same bits. 
    Then the number and sizes of these sequences are analyzed for compliance with a truly random
    reference sequence. The main task of this test is to determine how often the change from "1" to "0" and back occurs.

    Args:
        bit_string (str): The bit sequence to test.

    Returns:
        float: The p-value of the test. 
        If the value tends to 1, then it is said that the generator tends to be ideal.
        If the P-value tends to 0, the generator is completely predictable.

    Raises:
        ValueError: the input string is not a bitstring.
    """

    if any([symbol not in ['0','1'] for symbol in bit_string]):
        raise ValueError("This is not a bitstring")

    ones_ratio = bit_string.count('1') / len(bit_string)

    if abs(ones_ratio - 0.5) < (2 / math.sqrt(len(bit_string))):
        sign_alteration_count = sum(
            [0 if bit_string[i] == bit_string[i + 1] else 1
            for i in range(len(bit_string) - 1)]
            )

        p_value = math.erfc(
            abs(sign_alteration_count - 2 * len(bit_string) * ones_ratio * (1 - ones_ratio)) / (
                2 * math.sqrt(2 * len(bit_string)) * ones_ratio * (1 - ones_ratio))
            )
    else:
        p_value = 0
    
    return p_value


def longest_sequence_test(bit_string: str) -> float:
    """
    Calculates the longest sequence of ones block eight test.

    The longest sequence of ones block eight test is a statistical test used to determine whether a sequence of bits is random.
    The test is based on the assumption that the probability of a 0 or 1 bit occurring is equal.
    The test statistic is the length of the longest sequence of consecutive 1s in the sequence.
    The p-value is the probability of obtaining a test statistic as extreme as, or more extreme than,
    the observed test statistic, assuming that the sequence is random.

    Args:
        array_bits (str): The sequence of bits to test.

    Returns:
        float: The p-value of the test. 
        If the value tends to 1, then it is said that the generator tends to be ideal.
        If the P-value tends to 0, the generator is completely predictable.

    Raises:
        ValueError:  the input string is not a bitstring.
    """

    NATURAL_PROBABILITIES = {1: 0.2148, 2: 0.3672, 3: 0.2305, 4: 0.1875}
    MAX_BLOCK_LENGTH = 8

    if any([symbol not in ['0','1'] for symbol in bit_string]):
        raise ValueError("This is not a bitstring")

    if len(bit_string) != 128:
        raise ValueError(f"This test is designed for 128 bits long string")

    block_stats = {key: 0 for key in NATURAL_PROBABILITIES.keys()}

    for i in range(0, len(bit_string), MAX_BLOCK_LENGTH):
        block = bit_string[i:i + MAX_BLOCK_LENGTH]

        length = 0
        max_length = 0
        for bit in block:
            if bit == '1':
                length += 1 
            else:
                max_length = max(max_length, length)
                length = 0

        if max_length >= 4:
            max_length = 4
        elif max_length < 1:
            max_length = 1
        block_stats[max_length] += 1

    hi_square = 0
    for block in block_stats.keys():
        hi_square += ((block_stats[block] - 16 * NATURAL_PROBABILITIES[block])**2) / (
            16 * NATURAL_PROBABILITIES[block])
    p_value = float(mpmath.gammainc(3 / 2, hi_square / 2))

    return p_value