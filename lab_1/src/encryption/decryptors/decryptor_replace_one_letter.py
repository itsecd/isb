import os
import json

from typing import List, Dict


class DecryptorReplaceOneLetter:
    """
    Class for text analysis and manipulation.
    """
    
    def __init__(self, text: str):
        """
        Initialize with the provided text.

        Parameters:
        - text (str): The text to be analyzed and manipulated.
        """
        self._text = text
        pass
    
    def change_text(self, text: str):
        """
        Change the current text to the new provided text.

        Parameters:
        - text (str): The new text to replace the current text.
        """
        self._text = text
        pass
    

    @staticmethod
    def analysis_text_s(text: str) -> dict:
        """
        Analyze the frequency of each letter in the text.

        Parameters:
        - text (str): The text to analyze.

        Returns:
        - dict: A dictionary containing the frequency of each letter in the 
        text.
        """
        size = len(text)
        alphabet = sorted(set(text))
        frequency = dict()

        for letter in alphabet:

            frequency[letter] = text.count(letter) / size
        return frequency
    
    def analysis_text(self) -> dict:
        """
        Analyze the frequency of each letter in the stored text.

        Returns:
        - dict: A dictionary containing the frequency of each letter in the   
        stored text.
        """
        return DecryptorReplaceOneLetter.analysis_text_s(self._text)
    

    @staticmethod
    def sort_dict_values_s(dictionary: dict) -> dict:
        """
        Sort a dictionary by its values in descending order.

        Parameters:
        - dictionary (dict): The dictionary to be sorted.

        Returns:
        - dict: The sorted dictionary based on values in descending order.
        """
        new_dict = dict(reversed(sorted(dictionary.items(), 
                                        key=lambda x: x[1])))
        return new_dict
    
    
    @staticmethod
    def analysis_text_and_sort_frequency_s(text: str) -> dict:
        """
        Analyze text and sort the frequency of letters.

        Parameters:
        - text (str): The text to analyze and sort.

        Returns:
        - dict: A dictionary of letters sorted by frequency.
        """
        return DecryptorReplaceOneLetter.sort_dict_values_s(
                                            DecryptorReplaceOneLetter.analysis_text_s(text))
    

    def analysis_text_and_sort_frequency(self) -> dict:
        """
        Analyze stored text and sort the frequency of letters.

        Returns:
        - dict: A dictionary of letters sorted by frequency.
        """
        return DecryptorReplaceOneLetter.sort_dict_values_s(
                                            DecryptorReplaceOneLetter.analysis_text_s(self._text))
    

    @staticmethod
    def size_alphabet_s(text: str) -> int:
        """
        Calculate the size of the alphabet in the text.

        Parameters:
        - text (str): The text to determine the alphabet size.

        Returns:
        - int: The size of the alphabet in the text.
        """
        return len(set(text))
    
    def size_alphabet_text(self) -> int:
        """
        Calculate the size of the alphabet in the stored text.

        Returns:
        - int: The size of the alphabet in the stored text.
        """
        return len(set(self._text))

    
    @staticmethod
    def get_translate_dict_sort_frequency_s(text: str, 
                                            test_alphabet: str) -> dict:
        """
        Generate a translation dictionary based on the frequency of letters.

        Parameters:
        - text (str): The text to analyze for translation.
        - test_alphabet (str): The alphabet to translate to.

        Returns:
        - dict: A translation dictionary based on letter frequency.
        """
        size_alphabet = DecryptorReplaceOneLetter.size_alphabet_s(text)
        size_test_alphabet = len(set(test_alphabet))
        
        if size_alphabet != size_test_alphabet:
            raise Exception(f"Your test_alphabet is very bad size Alphabet: {size_alphabet}, size test Alphabet: {size_test_alphabet}")
        
        alphabet = list(DecryptorReplaceOneLetter.sort_dict_values_s(DecryptorReplaceOneLetter.analysis_text_s(text)).keys())

        translater = dict()

        for index in range(size_test_alphabet):

            translater[alphabet[index]] = test_alphabet[index]
        
        return  translater
    
    def get_translate_dict_frequency(self, 
                                     test_alphabet: str) -> dict:
        """
        Generate a translation dictionary for the stored text based on
        frequency.

        Parameters:
        - test_alphabet (str): The alphabet to translate to.

        Returns:
        - dict: A translation dictionary based on letter frequency.
        """
        return DecryptorReplaceOneLetter.get_translate_dict_sort_frequency_s(self._text,
                                                                             test_alphabet)


    @staticmethod
    def get_translate_dict_sort_alphabet_s(text: str, 
                                           test_alphabet: str) -> dict:
        """
        Generate a translation dictionary based on the order of letters in 
        the alphabet.

        Parameters:
        - text (str): The text to analyze for translation.
        - test_alphabet (str): The alphabet to translate to.

        Returns:
        - dict: A translation dictionary based on the order of letters in the
        alphabet.
        """
        size_alphabet = DecryptorReplaceOneLetter.size_alphabet_s(text)
        size_test_alphabet = len(set(test_alphabet))
        
        if size_alphabet != size_test_alphabet:
            raise Exception(f"Your test_alphabet is very bad size Alphabet: {size_alphabet}, size test Alphabet: {size_test_alphabet}")
        
        alphabet = sorted(set(text))

        translater = dict()

        for index in range(size_test_alphabet):

            translater[alphabet[index]] = test_alphabet[index]
        
        return  translater

    def get_translate_dict_alphabet(self, test_alphabet: str) -> dict:
        """
        Generate a translation dictionary for the stored text based on 
        alphabet order.

        Parameters:
        - test_alphabet (str): The alphabet to translate to.

        Returns:
        - dict: A translation dictionary based on the order of letters in 
        the alphabet.
        """
        return DecryptorReplaceOneLetter.get_translate_dict_sort_alphabet_s(self._text, 
                                                                            test_alphabet)


    @staticmethod
    def __translate(text: str, dictionary: dict) -> str:
        """
        Translate text using the provided dictionary.

        Parameters:
        - text (str): The text to be translated.
        - dictionary (dict): The translation dictionary.

        Returns:
        - str: The translated text based on the dictionary.
        """
        translate = ""
        for i in text:
            translate += dictionary[i]
        return translate


    @staticmethod
    def decryption_sort_alphabet_s(text: str, key: str) -> str:
        """
        Decrypt the text based on an input key using alphabet order.

        Parameters:
        - text (str): The text to decrypt.
        - key (str): The key to decrypt the text.

        Returns:
        - str: The decrypted text based on the key and alphabet order.
        """

        dictionary = DecryptorReplaceOneLetter.get_translate_dict_sort_alphabet_s(text, 
                                                                                  key)
        return DecryptorReplaceOneLetter.__translate(text, dictionary)

    def decryption_sort_alphabet(self, key: str) -> str:
        """
        Decrypt the stored text based on an input key using alphabet order.

        Parameters:
        - key (str): The key to decrypt the stored text.

        Returns:
        - str: The decrypted text based on the key and alphabet order.
        """
        return DecryptorReplaceOneLetter.decryption_sort_alphabet_s(self._text, 
                                                                    key)


    @staticmethod
    def decryption_sort_frequency_s(text: str, key: str) -> str:
        """
        Decrypt the text based on an input key using frequency-based
        translation.

        Parameters:
        - text (str): The text to decrypt.
        - key (str): The key to decrypt the text.

        Returns:
        - str: The decrypted text based on the key and frequency-based 
        translation.
        """
        dictionary = DecryptorReplaceOneLetter.get_translate_dict_sort_frequency_s(text, 
                                                                                   key)
        return DecryptorReplaceOneLetter.__translate(text, dictionary)
        
    def decryption_sort_frequency(self, key: str) -> str:
        """
        Decrypt the stored text based on an input key using frequency-based 
        translation.

        Parameters:
        - key (str): The key to decrypt the stored text.

        Returns:
        - str: The decrypted text based on the key and frequency-based 
        translation.
        """
        return DecryptorReplaceOneLetter.decryption_sort_frequency_s(self._text, 
                                                                     key)

    @staticmethod
    def split_text(text: str, delimiters: list) -> list:
        """
        Split the text into words based on provided delimiters.

        Parameters:
        - text (str): The text to split.
        - delimiters (list): List of delimiters to use for splitting.

        Returns:
        - list: A list of words obtained after splitting the text.
        """
        if len(delimiters) < 1:
            Exception("Doesn't have delimetrs")

        for delimiter in delimiters:
            text = text.replace(delimiter, delimiters[0])
        words = text.split(delimiters[0])
        
        return words
    
    @staticmethod
    def split_text_by_size_s(text: str, 
                             delimiters: list, 
                             size: int) -> list:
        """
        Split the text into words of a specific size.

        Parameters:
        - text (str): The text to split.
        - delimiters (list): List of delimiters to use for splitting.
        - size (int): The size of words to filter.

        Returns:
        - list: A list of words from the text with the specified size.
        """
        words = DecryptorReplaceOneLetter.split_text(text, delimiters)
        filtered_words = [word for word in words if len(word) == size]

        return filtered_words
    
    def split_text_by_size(self, delimiters: list, size: int) -> list:
        """
        Split the stored text into words of a specific size.

        Parameters:
        - delimiters (list): List of delimiters to use for splitting.
        - size (int): The size of words to filter.

        Returns:
        - list: A list of words from the stored text with the specified size.
        """
        return DecryptorReplaceOneLetter.split_text_by_size_s(self._text, 
                                                              delimiters, 
                                                              size) 
        
    @staticmethod
    def swap_letters_in_alphabet(test_alphabet: str, 
                                 letter_1: str, 
                                 letter_2: set) -> str:
        """
        Swap two letters in the test alphabet.

        Parameters:
        - test_alphabet (str): The test alphabet to perform the swap.
        - letter_1 (str): The first letter to swap.
        - letter_2 (str): The second letter to swap.

        Returns:
        - str: The new test alphabet after swapping letters.
        """
        if len(set(test_alphabet)) != len(test_alphabet) \
            or len(letter_1) != 1  or len(letter_2) != 1 \
            or not (letter_1 in test_alphabet) or not \
            (letter_2 in test_alphabet):
            
            raise Exception("Bad Alphabet or letters for swap")
        
        new_text = ""
        for char in test_alphabet:
            if char == letter_1:
                new_text += letter_2
            elif char == letter_2:
                new_text += letter_1
            else:
                new_text += char
        
        return new_text
    
    @staticmethod
    def count_word_size_in_text_s(text: str,
                                  delimiters: list,
                                  size: int) -> int:
        """
        Count the number of words of a specific size in the text.

        Parameters:
        - text (str): The text to analyze.
        - delimiters (list): List of delimiters to use for word separation.
        - size (int): The size of words to count.

        Returns:
        - int: The number of words of the specified size in the text.
        """

        return len(DecryptorReplaceOneLetter.split_text_by_size_s(text, 
                                                                  delimiters, 
                                                                  size))
    
    def count_word_size_in_text(self, delimiters: list, size: int) -> int:
        """
        Count the number of words of a specific size in the stored text.

        Parameters:
        - delimiters (list): List of delimiters to use for word separation.
        - size (int): The size of words to count.

        Returns:
        - int: The number of words of the specified size in the stored text.
        """
        return len(DecryptorReplaceOneLetter.split_text_by_size_s(self._text, delimiters, size))
    
    @staticmethod
    def word_size_in_text_frequency_s(text: str, delimiters: list, size: int) -> float:
        """
        Calculate the frequency of words of a specific size in the text.

        Parameters:
        - text (str): The text to analyze.
        - delimiters (list): List of delimiters to use for word separation.
        - size (int): The size of words to consider for frequency.

        Returns:
        - float: The frequency of words of the specified size in the text.
        """
        return len(DecryptorReplaceOneLetter.split_text_by_size_s(text, delimiters, size)) / len(DecryptorReplaceOneLetter.split_text(text, delimiters))
    
    def word_size_in_text_frequency(self, delimiters: list, size: int) -> float:
        """
        Calculate the frequency of words of a specific size in the stored 
        text.

        Parameters:
        - delimiters (list): List of delimiters to use for word separation.
        - size (int): The size of words to consider for frequency.

        Returns:
        - float: The frequency of words of the specified size in the stored 
        text.
        """
        return len(DecryptorReplaceOneLetter.split_text_by_size_s(self._text, delimiters, size)) / len(DecryptorReplaceOneLetter.split_text(self._text, delimiters))


    @staticmethod
    def swap_set_characters(test_alphabet: str, 
                            set_1: str, 
                            set_2: str) -> str:
        """
        Swap sets of characters in the test alphabet.

        Parameters:
        - test_alphabet (str): The test alphabet to perform the swap.
        - set_1 (str): The first set of characters to swap.
        - set_2 (str): The second set of characters to swap.

        Returns:
        - str: The new test alphabet after swapping sets of characters.
        """
        if len(set(set_1)) != len(set(set_2)) or len(set_1) != len(set_2):

            raise Exception("Bad set_1_2 for swap")

        new_text = test_alphabet
        for c in range(len(set_1)):
            new_text = DecryptorReplaceOneLetter.swap_letters_in_alphabet(new_text, 
                                                                          set_1[c], 
                                                                          set_2[c])
        
        return new_text
        
        
    def export_key_json(self, 
                       alphabetFrequency: str, 
                       fileForExport: str="key_alphabet.json", 
                       nameForHeaderKey:str = "key", 
                       nameForHeaderAlphabet:str = "alphabet") -> None:
        """
        Export the translation key and alphabet frequency to a JSON file.

        Parameters:
        - alphabetFrequency (str): The alphabet frequency for translation.
        - fileForExport (str): The file name for exporting the JSON 
        (default: "key_alphabet.json").
        - nameForHeaderKey (str): The header name for the translation key 
        (default: "key").
        - nameForHeaderAlphabet (str): The header name for the alphabet 
        (default: "alphabet").

        Raises:
        - Exception: If the file for export already exists.

        Writes the translation key and alphabet frequency information toa JSON file in the specified format.
        """
        if os.path.isfile(fileForExport):
            raise Exception(f"{fileForExport} уже существует")
            
        info = self.get_translate_dict_frequency(alphabetFrequency)

        info1 = {nameForHeaderKey: dict(zip(info.keys(), info.values()))}

        info2 = {nameForHeaderAlphabet: dict(zip(info.values(), info.keys()))}

        info = [info1, info2]

        json_data = json.dumps(info, sort_keys=True, indent=2, ensure_ascii=False)

        with open(fileForExport, 'w') as f:
            f.write(json_data)    