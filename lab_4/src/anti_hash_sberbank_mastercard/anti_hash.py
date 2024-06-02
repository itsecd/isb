import re
import logging
import multiprocessing

from tqdm import tqdm
from typing import Set
from hashlib import blake2s

logger = logging.getLogger(__name__)


def get_cards_according_template(
    bins: Set[str],
    last_digits: str,
    count_digits_in_card: int,
    hash_value: str,
    max_processes=None,
) -> set[str]:
    """
    Generate a set of card numbers based on a template and hash value.

    Args:
        - bins (Set[str]): A set of strings representing the bin numbers.
        - last_digits (str): The string representing the last digits of
        the card number template.
        - count_digits_in_card (int): The total number of digits in each
        card number.
        - hash_value (str): The hash value to match generated card numbers
        against.
        - max_processes (int, optional): The maximum number of processes
        to use for parallel processing.Defaults to None.

    Returns:
        - set[str]: A set of card numbers matching the provided template and hash value.

    Raises:
        - ValueError: If last_digits contain non-digit characters.

    Example:
        >>> bins = {'1234', '5678'}
        >>> last_digits = '5678'
        >>> count_digits_in_card = 16
        >>> hash_value = 'f7b6dc471100141c44f1443541de2c7e'
        >>> get_cards_according_template(bins, last_digits, count_digits_in_card, hash_value)
        {'123400015678', '567800015678'}
    """

    try:
        logger.info(f"Start processing cards hash[{hash_value}]")

        if not bool(re.match("^[0-9]+$", last_digits)):
            raise ValueError(
                f"Last digits are not a string of digits "
                f"value:[{last_digits}], maps cannot be generated"
            )

        cards: set[str] = set()

        with multiprocessing.Pool(processes=max_processes) as pool:

            results = list(
                tqdm(
                    pool.imap(
                        get_cards_matching_hash_wrapper,
                        [
                            (
                                bin,
                                last_digits,
                                count_digits_in_card,
                                hash_value,
                            )
                            for bin in bins
                        ],
                    ),
                    total=len(bins),
                    desc=f"{hash_value} rehash",
                )
            )

        for result in results:

            cards.update(result)

        logger.info(f"Processing cards by hash[{hash_value}] successful")
        return cards

    except Exception as e:

        if not last_digits:
            logger.error(
                f"Error processing cards hash[{hash_value}]. Last"
                f" digits:[{last_digits}] is None, please indicate another "
                f"value"
            )

        else:
            logger.error(f"Error processing cards by hash[{hash_value}]. {e}")


def get_cards_matching_hash(
    prefix_digits: str,
    last_digits: str,
    count_digits_in_card: int,
    hash_value: str,
) -> Set[str]:
    """
    Generate a set of card numbers matching a given hash value.

    Args:
        - prefix_digits (str): The string representing the prefix digits of
        the card number.
        - last_digits (str): The string representing the last digits of
        the card number.
        - count_digits_in_card (int): The total number of digits in each
        card number.
        - hash_value (str): The hash value to match generated card numbers
        against.

    Returns:
        - Set[str]: A set of card numbers matching the provided hash value.

    Raises:
        - ValueError: If prefix_digits or last_digits contain non-digit
        characters, or if the count of digits required for generating
        cards exceeds the specified count_digits_in_card.

    Example:
        >>> get_cards_matching_hash('1234', '5678', 16, 'f7b6dc471100141c44f1443541de2c7e')
        {'123400015678'}
    """

    if not bool(re.match("^[0-9]+$", prefix_digits)):
        raise ValueError(
            f"Prefix digits are not a string of digits [value: "
            f"{prefix_digits}], maps cannot be generated"
        )

    if not bool(re.match("^[0-9]+$", last_digits)):
        raise ValueError(
            f"Last digits are not a string of digits value:[{last_digits}],"
            f" maps cannot be generated"
        )

    count_digits_generate = count_digits_in_card - len(prefix_digits) - len(last_digits)

    if count_digits_generate < 1:
        raise ValueError(
            f"The required number for generating cards has been exceeded: "
            f"need: bin[{prefix_digits}]+last_digits[{last_digits}]:"
            f"{len(prefix_digits) + len(last_digits)} < count_digits["
            f"{count_digits_in_card}]"
        )

    cards: Set[str] = set()

    for generate_numbers in range(0, 10**count_digits_generate):

        card_number = (
            prefix_digits
            + str(generate_numbers).zfill(count_digits_generate)
            + last_digits
        )
        generated_hash = blake2s(card_number.encode()).hexdigest()

        if generated_hash == hash_value:
            cards.add(card_number)

    return cards


def get_cards_matching_hash_wrapper(args):
    """
    Wrapper function to get cards matching a hash.

    Args:
        - args: Arguments for the get_cards_matching_hash function.

    Returns:
        - set: Set of cards matching the hash.

    Example:
        >>> get_cards_matching_hash_wrapper(("hash_value", "param_2", "param_3"))
        {'1234567890123456', '9876543210987654'}
    """

    try:

        return get_cards_matching_hash(*args)

    except Exception as e:

        logger.warning(f"Could not check the cards according hash:[{args[2]}]. {e}")
        return set()
