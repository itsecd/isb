import re
import logging
import multiprocessing

from typing import Set
from hashlib import blake2s

from consts import DEFAULT_COUNT_DIGITS_INTO_CARD, DEFAULT_PREFIX_TEMPLATES_FOUR_DIGIT_SBERBANK_MASTERCARD_CREDIT



logger = logging.getLogger(__name__)


def get_cards_according_template(bins: Set[str], last_digits: str, hash_value: str) -> Set[str]:
    
    try:
        cards: Set[str] = set()

        pool = multiprocessing.Pool()
        results = []

        for bin in bins:
            result = pool.apply_async(get_cards_matching_hash, (bin, last_digits, hash_value))
            results.append(result)

        pool.close()
        pool.join()

        for result in results:
            cards.update(result.get())

        return cards
    
    except Exception as e:
        raise ValueError("Get cards about template fail, ", e)


def get_cards_matching_hash(bin: str, last_digits: str, hash_value: str) -> Set[str]:

    if not bool(re.match("^[0-9]+$", bin)):

        raise ValueError(f"Bin are not a string of digits [value: {bin}], maps cannot be generated")

    if not bool(re.match("^[0-9]+$", last_digits)):

        raise ValueError(f"Last digits are not a string of digits [value: {last_digits}], maps cannot be generated")

    count_digits_generate = DEFAULT_COUNT_DIGITS_INTO_CARD - len(bin) - len(last_digits)

    if count_digits_generate < 1:

        raise ValueError(f"The required number for generating cards has been exceeded: need [bin+last_digits:{len(bin) + len(last_digits)} > count_digits:{DEFAULT_COUNT_DIGITS_INTO_CARD}]")

    cards: Set[str] = set()

    for generate_numbers in range(0, 10**count_digits_generate):

        card_number = bin + str(generate_numbers).zfill(count_digits_generate) + last_digits
        
        generated_hash = blake2s(card_number.encode()).hexdigest()

        if generated_hash == hash_value:
            cards.add(card_number)

    return cards


def generate_bins_sberbank_mastercard(prefix_templates:str = DEFAULT_PREFIX_TEMPLATES_FOUR_DIGIT_SBERBANK_MASTERCARD_CREDIT) -> Set[str]:
    
    if not all((len(prefix) == 4 and re.match("^[0-9]+$", prefix)) for prefix in prefix_templates):
        
        raise ValueError("Prefix templates is not good")
        
    bins: Set[str] = set()
    
    for prefix in prefix_templates:
    
        for generate_numbers in range(0, 10**2):

            bin = prefix + str(generate_numbers).zfill(2)
            bins.add(bin)
    
    return bins

# print(get_cards_according_template(generate_bins_sberbank_mastercard(), "2301", "140495200b351b7f18a46e3796f2875ebdf0023568933ef3b99efb285af3f06b"))
