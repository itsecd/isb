def get_proba(key: int) -> int: 
    
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