import math

import mpmath

from consts import THEORETICAL_PROBABILITIES, MAX_LENGTH_BLOCK, COUNT_BITS, hash

def frequency_bit_test(array_bits: str) -> float:
    
    if not all(char in '01' for char in array_bits):
        raise ValueError("Это не строка битов")
    
    sum = 0
    
    for bit in array_bits:        
        if bit == '1':
            sum += 1
        elif bit =='0':
            sum += -1

    return math.erfc(sum / math.sqrt(len(array_bits)) / math.sqrt(len(2)))
        
def identical_consecutive_bits_test(array_bits: str) -> float:
    
    if not all(char in '01' for char in array_bits):
        raise ValueError("Это не строка битов")
    
    fraction_ones = array_bits.count("1") / len(array_bits)
    
    if abs(fraction_ones - 0.5) >= (2 / math.sqrt(len(array_bits))):
        return 0
    
    count_alternating_signs = sum(1 if array_bits[i] != array_bits[i + 1] else 0 for i in range(len(array_bits) - 1))
    
    return math.erfc(abs(count_alternating_signs - 2 * len(array_bits) * fraction_ones * (1 - fraction_ones)) / 
                     (2 * math.sqrt(2 * len(array_bits)) * fraction_ones * (1 - fraction_ones)))

def longest_sequence_ones_block_eight_test(array_bits: str):
    
    if not all(char in '01' for char in array_bits):
        raise ValueError("Это не строка битов")
    
    if len(array_bits) != COUNT_BITS:
        raise ValueError(f"Этот тест работает только с {COUNT_BITS} битами")
        
    blocks_info = {key: 0 for key in THEORETICAL_PROBABILITIES.keys()}

    for step in range(0, len(array_bits), MAX_LENGTH_BLOCK):
    
        block = array_bits[step: step + MAX_LENGTH_BLOCK]    
        max_length, length = 0, 0
        
        for bit in block:
            
            length = length + 1 if bit == '1' else 0
            max_length = max(max_length, length)
    
        blocks_info[hash(max_length)] += 1
        
    hi_square = 0
    for key in blocks_info.keys():
        hi_square += math.pow(blocks_info[key] - 16 * THEORETICAL_PROBABILITIES[key], 2) / (16 * THEORETICAL_PROBABILITIES[key])
                
    return mpmath.gammainc(1.5, hi_square / 2)