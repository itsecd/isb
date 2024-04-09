from typing import Set


def correct_card_moon(number_card: str, separators: Set[str]) -> bool:
    """
    Check if a card number is valid according to the Luhn algorithm.

    Args:
        - number_card (str): The card number with or without separators.
        - separators (set of str): Set of separator characters to be
        removed from the card number.

    Returns:
        - bool: True if the card number is valid, False otherwise.

    Raises:
        - ValueError: If the input is invalid or contains non-numeric
        characters.

    Example:
        >>> correct_card_moon("1234-5678-9012-3456", {'-', ' '})
        True
    """

    try:
        number_card_digits = number_card

        for sep in separators:
            number_card_digits = number_card_digits.replace(sep, "")

        return sum_moon(number_card_digits) % 10 == 0

    except Exception as e:

        raise ValueError(
            (
                f"Bad input, delete separators in your card, list "
                f"separators using {separators}. Additional: {e}."
            )
        )


def sum_moon(number_card: str) -> int:
    """
    Calculate the sum of digits in a card number according to the Luhn
    algorithm.

    Args:
        - number_card (str): The card number without separators.

    Returns:
        - int: The sum of digits.

    Raises:
        - ValueError: If the card number contains invalid characters.

    Example:
        >>> sum_moon("1234567890123456")
        80
    """

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

        raise ValueError(
            f"Invalid character in card number digit[{digit}]. " f"Additional: {e}."
        )


def sum_sequence(sequence_numbers: int) -> int:
    """
    Calculate the sum of digits in a number.

    Args:
        - sequence_numbers (int): The number whose digits are to be summed.

    Returns:
        - int: The sum of digits.

    Example:
        >>> sum_sequence(123)
        6
    """

    iterator_digit: int = sequence_numbers
    sum: int = 0

    while iterator_digit > 0:

        sum += iterator_digit % 10
        iterator_digit //= 10

    return sum
