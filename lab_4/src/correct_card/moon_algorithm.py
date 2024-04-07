import logging

from typing import Set

from .consts import DEFAULT_SEPARATORS


logger = logging.getLogger(__name__)


def correct_card_moon(number_card: str, separators=DEFAULT_SEPARATORS) -> bool:    
    
    try:
        
        number_card_digits = number_card
        
        for sep in separators:
            number_card_digits = number_card_digits.replace(sep, '')
        
        return sum_moon(number_card=number_card) % 10 == 0
    
    except Exception as e:

        raise ValueError(f"Bad input, delete separators in your card, list separators using {separators}: ", e)


def sum_moon(number_card: str) -> int:

    try:
        
        sum: int = 0
        even: bool = False

        number_card_without_separators = number_card

        for digit in number_card_without_separators[::-1]:

            sum_helper = 2 * int(digit) if even else int(digit)
            sum += sum_helper if sum_helper < 10 else sum_sequence(sum_helper)
            even = not even

        return sum
    
    except Exception as e:
        
        raise ValueError(f"Invalid character in card number, digit:{digit}, arg:{number_card} ", e)


def sum_sequence(sequence_numbers: int) -> int:
    
    iterator_digit: int = sequence_numbers
    sum: int = 0
    
    while iterator_digit > 0:
        
        sum += iterator_digit % 10
        iterator_digit //= 10
    
    return sum
