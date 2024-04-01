import enum

from typing import List

@enum.unique
class ErrorType(enum.Enum):
    """
    Error codes for the `error_types` function.
    """

    ALPHABET_VALUES_NOT_UNIQUE = 1
    KEY_VALUES_NOT_UNIQUE = 2
    LEN_KEY_NOT_EQUAL_LEN_ALPHABET = 3
    CHARACTERS_ALPHABET_NOT_CONTAINS_IN_TEXT = 4

    def __str__(self) -> str:
        return error_type_to_string[self]

error_type_to_string = {
    ErrorType.ALPHABET_VALUES_NOT_UNIQUE: "Alphabet values are not unique",
    ErrorType.KEY_VALUES_NOT_UNIQUE: "Key values are not unique",
    ErrorType.LEN_KEY_NOT_EQUAL_LEN_ALPHABET: "Key length is not equal to alphabet length",
    ErrorType.CHARACTERS_ALPHABET_NOT_CONTAINS_IN_TEXT: "Alphabet characters are not contained in the text",
}

def error_types(alphabet: str, key: str, text: str) -> List[ErrorType]:
    
    """Checks the given alphabet and key for errors.

    Args:
        - alphabet (str): The alphabet to check.
        - key (str): The key to check.

    Returns:
        - List[ErrorType]: A list of errors found.
    """

    error_list: List[ErrorType] = []

    len_alphabet: int = len(alphabet)
    len_key: int = len(key)
    len_set_alphabet: int = len(set(alphabet))
    len_set_key: int = len(set(key))

    if len_alphabet != len_set_alphabet:
        error_list.append(ErrorType.ALPHABET_VALUES_NOT_UNIQUE)

    if len_key != len_set_key:
        error_list.append(ErrorType.KEY_VALUES_NOT_UNIQUE)

    if len_alphabet != len_key:
        error_list.append(ErrorType.LEN_KEY_NOT_EQUAL_LEN_ALPHABET)
    
    if not all(c in alphabet for c in set(text)):
        error_list.append(ErrorType.CHARACTERS_ALPHABET_NOT_CONTAINS_IN_TEXT)

    return error_list

def generate_pretty_errors(error_list: List[ErrorType]) -> str:
    
    """Generates a pretty string of errors.

    Args:
        - error_list (List[ErrorType]): The list of errors to generate a string for.

    Returns:
        - str: A pretty string of errors.
    """
    
    error_string: List[str] = []
    
    for index, error in enumerate(error_list):
        error_string.append(f"{index + 1}. {str(error)}")
    
    return ", ".join(error_string)