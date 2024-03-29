import math

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
                     (2 * math.sqrt(2 * len(array_bits)) * fraction_ones * (1 - fraction_ones))
                    )

def longest_sequence_ones_block_eight_test(array_bits: str) -> float:
    
    if not all(char in '01' for char in array_bits):
        raise ValueError("Это не строка битов")
    
    if len(array_bits) != 128:
        raise ValueError("Этот тест работает только с 128 битами")
    
    
    