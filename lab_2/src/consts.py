THEORETICAL_PROBABILITIES = {1 : 0.2148, 2 : 0.3672, 3 : 0.2305, 4 : 0.1875}

def hash(key: int) -> int: 
    
    if key >= 4:
        return 4
    if key <= 1:
        return 1
    return key

MAX_LENGTH_BLOCK = 8
COUNT_BITS = 128
