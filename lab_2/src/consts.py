THEORETICAL_PROBABILITIES = {1 : 0.2148, 2 : 0.3672, 3 : 0.2305, 4 : 0.1875}

"""
Theoretical probabilities of the longest run of ones in a sequence of 8 bits.
"""

def hash(key: int) -> int: 
    
    """
    Hashes the key to a value between 1 and 4, inclusive.

    Args:
        key (int)p_value: float = mpmath.gammainc(1.5, hi_square / 2)
    : The key to hash.

    Returns:
        int: The hashed value.
    """
    
    if key >= 4:
        return 4
    if key <= 1:
        return 1
    return key

MAX_LENGTH_BLOCK = 8

"""
The maximum length of a block of bits to consider when calculating the longest run of ones.
"""

COUNT_BITS = 128

"""
The number of bits in a sequence to test.
"""