from typing import List, Dict

import exception as error

def encrypt(alphabet: str, key: str, text: str) -> str:
    
    """Encrypts the given text using the Caesar cipher.

    The Caesar cipher is a simple substitution cipher in which each letter in the
    plaintext is replaced by the letter that is a certain number of places down
    the alphabet. The number of places down is determined by the key. For
    example, if the key is 3, then A would be replaced by D, B would be replaced
    by E, and so on.

    Args:
        - alphabet (str): The alphabet to use for encryption.
        - key (str): The key to use for encryption.
        - text (str): The text to encrypt.

    Returns:
        - str: The encrypted text.

    Raises:
        - ValueError: if the alphabet and key are not of the same length, or if the
            text contains characters not in the alphabet.
    """

    errors: List[error.ErrorType] = error.error_types(alphabet, key, text)

    if len(errors) != 0:
        raise ValueError(error.generate_pretty_errors(errors))

    encrypted_text = ""

    for c in text:
        encrypted_text += key[alphabet.index(c)]

    return encrypted_text

def analysis_text(text: str) -> Dict[str, float]:
        """
        Analyze the frequency of each letter in the text.

        Parameters:
        - text (str): The text to analyze.

        Returns:
        - dict: A dictionary containing the frequency of each letter in the 
        text.
        """
        size = len(text)
        alphabet = set(text)
        frequency: Dict[str, float] = {}

        for letter in alphabet:

            frequency[letter] = text.count(letter) / size
        
        return frequency

def sort_dict_values(dictionary: Dict[str, float]) -> Dict[str, float]:
        """
        Sort a dictionary by its values in descending order.

        Parameters:
        - dictionary (dict): The dictionary to be sorted.

        Returns:
        - dict: The sorted dictionary based on values in descending order.
        """
        return  dict(reversed(sorted(dictionary.items(), 
                                     key=lambda x: x[1])))