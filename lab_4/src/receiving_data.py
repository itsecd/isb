import re
import logging

from tqdm import tqdm
from typing import Set

from .consts import YELLOW, RESET
from .correct_card.moon_algorithm import correct_card_moon
from .anti_hash_sberbank_mastercard.anti_hash import (
    get_cards_according_template,
)

logger = logging.getLogger(__name__)


def generate_bins(prefix_templates: Set[str], count_digits_for_bins: int) -> Set[str]:
    """
    Generate BINs based on prefix templates.

    Args:
        - prefix_templates (set[str]): Set of prefix templates for BINs.
        - count_digits_for_bins (int): Total number of digits for each BIN.

    Returns:
        - set[str]: Set of generated BINs.

    Raises:
        ValueError: If any prefix in prefix_templates is longer than
        count_digits_for_bins or if any prefix is not a string of digits.

    Example:
        >>> generate_bins({'123', '456'}, 6)
        {'123000', '123001', '123002'..., '456000', '456001', '456002'...}
    """

    if not all(
        (len(prefix) <= count_digits_for_bins and re.match("^[0-9]+$", prefix))
        for prefix in prefix_templates
    ):

        raise ValueError(
            f"Prefix templates[{prefix_templates}] or count digits for"
            f"bins[{len(prefix)} <= {count_digits_for_bins}] bad"
        )

    bins: Set[str] = set()

    for prefix in prefix_templates:

        count_generate_digits_for_bin = count_digits_for_bins - len(prefix)

        for generate_numbers in range(0, 10 ** (count_generate_digits_for_bin)):
            bin = prefix + str(generate_numbers).zfill(count_generate_digits_for_bin)
            bins.add(bin)

    logger.info(f"Bins have been generated successfull.")

    return bins


def get_correct_cards(
    cards: Set[str],
    separators: Set[str],
) -> dict:
    """
    Process a set of cards and determine correct ones.

    Args:
        - cards (set): Set of card strings to be processed.
        - separators (set): Set of separator strings.

    Returns:
        - dict: A dictionary containing card strings as keys and their correctness status as values.

    Raises:
        - TypeError: If there's an error during the process.
    """

    try:

        logger.info(f"Start process get correct cards")

        result = {}

        for card in tqdm(cards, desc=f"Cards check:"):

            try:

                result[card] = correct_card_moon(card, separators)
                logger.info(f"Card[{card}]: Reading successful.")

            except Exception as e:

                result[card] = "fail input"
                logger.warning(f"Card[{card}]: Failed to process card. {e}")

        logger.info(f"Process get correct cards, successfull")

        return result

    except Exception as e:

        raise TypeError(f"Get correct cards error: {e}")


def get_rehash(
    hash_values: Set[str],
    bins: Set[set],
    last_digits: str,
    count_digits_into_card: int,
    max_procces_for_one_rehash: int = None,
    name_conf_into_output: str = None,
) -> dict:
    """
    Generate rehashes based on hash values, bins, and last digits.

    Args:
        - hash_values (set): Set of hash values.
        - bins (set): Set of bins.
        - last_digits (str): Last digits for rehashing.
        - count_digits_into_card (int): Count of digits into card.
        - max_procces_for_one_rehash (int, optional): Maximum processes for one rehash. Defaults to None.
        - name_conf_into_output (str, optional): Name of configuration into output. Defaults to None.

    Returns:
        - dict: A dictionary containing hash values as keys and their corresponding searching cards as values.

    Raises:
        - TypeError: If there's an error during the process.
    """

    try:

        logger.info(
            f"Start process get rehash by bins and last digits. Num max process[{max_procces_for_one_rehash}]"
        )

        result = {}

        for hash_value in tqdm(
            hash_values,
            desc=f"{YELLOW}Rehash lines{RESET}",
            bar_format=f"{{l_bar}}{YELLOW}{{bar}}{RESET}{{r_bar}}",
        ):

            result[hash_value] = {
                "searching_cards": list(
                    get_cards_according_template(
                        bins,
                        last_digits,
                        count_digits_into_card,
                        hash_value,
                        max_procces_for_one_rehash,
                    )
                ),
            }

        if name_conf_into_output:
            result[name_conf_into_output] = {
                "using_bins": list(bins),
                "last_digits": last_digits,
                "max_count_digits_into_card": count_digits_into_card,
                "max_count_core_using": max_procces_for_one_rehash,
            }

        logger.info(
            f"Process get rehash by bins and last digits. Num max process[{max_procces_for_one_rehash}], successfull"
        )
        return result

    except Exception as e:

        raise TypeError(f"Get rehash error: {e}")
