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
    
    def changeText(self, text: str):
        """
        Change the current text to the new provided text.

        Parameters:
        - text (str): The new text to replace the current text.
        """
        self._text = text
        pass
    

    @staticmethod
    def analysisText_s(text: str) -> dict:
        """
        Analyze the frequency of each letter in the text.

        Parameters:
        - text (str): The text to analyze.

        Returns:
        - dict: A dictionary containing the frequency of each letter in the text.
        """
        size = len(text)
        alphabet = sorted(set(text))
        frequency = dict()

        for letter in alphabet:

            frequency[letter] = text.count(letter) / size
        return frequency
    
    def analysisText(self) -> dict:
        """
        Analyze the frequency of each letter in the stored text.

        Returns:
        - dict: A dictionary containing the frequency of each letter in the stored text.
        """
        return DecryptorReplaceOneLetter.analysisText_s(self._text)
    

    @staticmethod
    def sortDictValues_s(dictionary: dict) -> dict:
        """
        Sort a dictionary by its values in descending order.

        Parameters:
        - dictionary (dict): The dictionary to be sorted.

        Returns:
        - dict: The sorted dictionary based on values in descending order.
        """
        newDict = dict(reversed(sorted(dictionary.items(), key=lambda x: x[1])))
        return newDict
    
    
    @staticmethod
    def analysisTextAndSortFrequency_s(text: str) -> dict:
        """
        Analyze text and sort the frequency of letters.

        Parameters:
        - text (str): The text to analyze and sort.

        Returns:
        - dict: A dictionary of letters sorted by frequency.
        """
        return DecryptorReplaceOneLetter.sortDictValues_s(DecryptorReplaceOneLetter.analysisText_s(text))
    

    def analysisTextAndSortFrequency(self) -> dict:
        """
        Analyze stored text and sort the frequency of letters.

        Returns:
        - dict: A dictionary of letters sorted by frequency.
        """
        return DecryptorReplaceOneLetter.sortDictValues_s(DecryptorReplaceOneLetter.analysisText_s(self._text))
    

    @staticmethod
    def sizeAlphabet_s(text: str) -> int:
        """
        Calculate the size of the alphabet in the text.

        Parameters:
        - text (str): The text to determine the alphabet size.

        Returns:
        - int: The size of the alphabet in the text.
        """
        return len(set(text))
    
    def sizeAlphabetText(self) -> int:
        """
        Calculate the size of the alphabet in the stored text.

        Returns:
        - int: The size of the alphabet in the stored text.
        """
        return len(set(self._text))

    
    @staticmethod
    def getTranslateDictSortFrequency_s(text: str, testAlphabet: str) -> dict:
        """
        Generate a translation dictionary based on the frequency of letters.

        Parameters:
        - text (str): The text to analyze for translation.
        - testAlphabet (str): The alphabet to translate to.

        Returns:
        - dict: A translation dictionary based on letter frequency.
        """
        sizeAlphabet = DecryptorReplaceOneLetter.sizeAlphabet_s(text)
        sizeTestAlphabet = len(set(testAlphabet))
        
        if sizeAlphabet != sizeTestAlphabet:
            raise Exception(f"Your testAlphabet is very bad size Alphabet: {sizeAlphabet}, size test Alphabet: {sizeTestAlphabet}")
        
        alphabet = list(DecryptorReplaceOneLetter.sortDictValues_s(DecryptorReplaceOneLetter.analysisText_s(text)).keys())

        translater = dict()

        for index in range(sizeTestAlphabet):

            translater[alphabet[index]] = testAlphabet[index]
        
        return  translater
    
    def getTranslateDictFrequency(self, testAlphabet: str) -> dict:
        """
        Generate a translation dictionary for the stored text based on frequency.

        Parameters:
        - testAlphabet (str): The alphabet to translate to.

        Returns:
        - dict: A translation dictionary based on letter frequency.
        """
        return DecryptorReplaceOneLetter.getTranslateDictSortFrequency_s(self._text, testAlphabet)


    @staticmethod
    def getTranslateDictSortAlphabet_s(text: str, testAlphabet: str) -> dict:
        """
        Generate a translation dictionary based on the order of letters in the alphabet.

        Parameters:
        - text (str): The text to analyze for translation.
        - testAlphabet (str): The alphabet to translate to.

        Returns:
        - dict: A translation dictionary based on the order of letters in the alphabet.
        """
        sizeAlphabet = DecryptorReplaceOneLetter.sizeAlphabet_s(text)
        sizeTestAlphabet = len(set(testAlphabet))
        
        if sizeAlphabet != sizeTestAlphabet:
            raise Exception(f"Your testAlphabet is very bad size Alphabet: {sizeAlphabet}, size test Alphabet: {sizeTestAlphabet}")
        
        alphabet = sorted(set(text))

        translater = dict()

        for index in range(sizeTestAlphabet):

            translater[alphabet[index]] = testAlphabet[index]
        
        return  translater

    def getTranslateDictAlphabet(self, testAlphabet: str) -> dict:
        """
        Generate a translation dictionary for the stored text based on alphabet order.

        Parameters:
        - testAlphabet (str): The alphabet to translate to.

        Returns:
        - dict: A translation dictionary based on the order of letters in the alphabet.
        """
        return DecryptorReplaceOneLetter.getTranslateDictSortAlphabet_s(self._text, testAlphabet)


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
    def decryptionSortAlphabet_s(text: str, key: str) -> str:
        """
        Decrypt the text based on an input key using alphabet order.

        Parameters:
        - text (str): The text to decrypt.
        - key (str): The key to decrypt the text.

        Returns:
        - str: The decrypted text based on the key and alphabet order.
        """

        dictionary = DecryptorReplaceOneLetter.getTranslateDictSortAlphabet_s(text, key)
        return DecryptorReplaceOneLetter.__translate(text, dictionary)

    def decryptionSortAlphabet(self, key: str) -> str:
        """
        Decrypt the stored text based on an input key using alphabet order.

        Parameters:
        - key (str): The key to decrypt the stored text.

        Returns:
        - str: The decrypted text based on the key and alphabet order.
        """
        return DecryptorReplaceOneLetter.decryptionSortAlphabet_s(self._text, key)


    @staticmethod
    def decryptionSortFrequency_s(text: str, key: str) -> str:
        """
        Decrypt the text based on an input key using frequency-based translation.

        Parameters:
        - text (str): The text to decrypt.
        - key (str): The key to decrypt the text.

        Returns:
        - str: The decrypted text based on the key and frequency-based translation.
        """
        dictionary = DecryptorReplaceOneLetter.getTranslateDictSortFrequency_s(text, key)
        return DecryptorReplaceOneLetter.__translate(text, dictionary)
        
    def decryptionSortFrequency(self, key: str) -> str:
        """
        Decrypt the stored text based on an input key using frequency-based translation.

        Parameters:
        - key (str): The key to decrypt the stored text.

        Returns:
        - str: The decrypted text based on the key and frequency-based translation.
        """
        return DecryptorReplaceOneLetter.decryptionSortFrequency_s(self._text, key)

    @staticmethod
    def splitText(text: str, delimiters: list) -> list:
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
    def splitTextBySize_s(text: str, delimiters: list, size: int) -> list:
        """
        Split the text into words of a specific size.

        Parameters:
        - text (str): The text to split.
        - delimiters (list): List of delimiters to use for splitting.
        - size (int): The size of words to filter.

        Returns:
        - list: A list of words from the text with the specified size.
        """
        words = DecryptorReplaceOneLetter.splitText(text, delimiters)
        filtered_words = [word for word in words if len(word) == size]

        return filtered_words
    
    def splitTextBySize(self, delimiters: list, size: int) -> list:
        """
        Split the stored text into words of a specific size.

        Parameters:
        - delimiters (list): List of delimiters to use for splitting.
        - size (int): The size of words to filter.

        Returns:
        - list: A list of words from the stored text with the specified size.
        """
        return DecryptorReplaceOneLetter.splitTextBySize_s(self._text, delimiters, size) 
        
    @staticmethod
    def swapLettersInTestAlphabet(testAlphabet: str, letter_1: str, letter_2: set) -> str:
        """
        Swap two letters in the test alphabet.

        Parameters:
        - testAlphabet (str): The test alphabet to perform the swap.
        - letter_1 (str): The first letter to swap.
        - letter_2 (str): The second letter to swap.

        Returns:
        - str: The new test alphabet after swapping letters.
        """
        if len(set(testAlphabet)) != len(testAlphabet) or len(letter_1) != 1 \
            or len(letter_2) != 1 or not (letter_1 in testAlphabet) or not \
            (letter_2 in testAlphabet):
            
            raise Exception("Bad Alphabet or letters for swap")
        
        new_text = ""
        for char in testAlphabet:
            if char == letter_1:
                new_text += letter_2
            elif char == letter_2:
                new_text += letter_1
            else:
                new_text += char
        
        return new_text
    
    @staticmethod
    def countWordSizeInText_s(text: str, delimiters: list, size: int) -> int:
        """
        Count the number of words of a specific size in the text.

        Parameters:
        - text (str): The text to analyze.
        - delimiters (list): List of delimiters to use for word separation.
        - size (int): The size of words to count.

        Returns:
        - int: The number of words of the specified size in the text.
        """

        return len(DecryptorReplaceOneLetter.splitTextBySize_s(text, delimiters, size))
    
    def countWordSizeInText(self, delimiters: list, size: int) -> int:
        """
        Count the number of words of a specific size in the stored text.

        Parameters:
        - delimiters (list): List of delimiters to use for word separation.
        - size (int): The size of words to count.

        Returns:
        - int: The number of words of the specified size in the stored text.
        """
        return len(DecryptorReplaceOneLetter.splitTextBySize_s(self._text, delimiters, size))
    
    @staticmethod
    def wordSizeInTextFrequency_s(text: str, delimiters: list, size: int) -> float:
        """
        Calculate the frequency of words of a specific size in the text.

        Parameters:
        - text (str): The text to analyze.
        - delimiters (list): List of delimiters to use for word separation.
        - size (int): The size of words to consider for frequency.

        Returns:
        - float: The frequency of words of the specified size in the text.
        """
        return len(DecryptorReplaceOneLetter.splitTextBySize_s(text, delimiters, size)) / len(DecryptorReplaceOneLetter.splitText(text, delimiters))
    
    def wordSizeInTextFrequency(self, delimiters: list, size: int) -> float:
        """
        Calculate the frequency of words of a specific size in the stored text.

        Parameters:
        - delimiters (list): List of delimiters to use for word separation.
        - size (int): The size of words to consider for frequency.

        Returns:
        - float: The frequency of words of the specified size in the stored text.
        """
        return len(DecryptorReplaceOneLetter.splitTextBySize_s(self._text, delimiters, size)) / len(DecryptorReplaceOneLetter.splitText(self._text, delimiters))


    @staticmethod
    def swapSetCharacters(testAlphabet: str, set_1: str, set_2: str) -> str:
        """
        Swap sets of characters in the test alphabet.

        Parameters:
        - testAlphabet (str): The test alphabet to perform the swap.
        - set_1 (str): The first set of characters to swap.
        - set_2 (str): The second set of characters to swap.

        Returns:
        - str: The new test alphabet after swapping sets of characters.
        """
        if len(set(set_1)) != len(set(set_2)) or len(set_1) != len(set_2):

            raise Exception("Bad set_1_2 for swap")

        newText = testAlphabet
        for c in range(len(set_1)):
            newText = DecryptorReplaceOneLetter.swapLettersInTestAlphabet(newText, set_1[c], set_2[c])
        
        return newText
        
        
    def export_KeyJSON(self, 
                       alphabetFrequency: str, 
                       fileForExport: str="key_alphabet.json", 
                       nameForHeaderKey:str = "key", 
                       nameForHeaderAlphabet:str = "alphabet") -> None:
        """
        Export the translation key and alphabet frequency to a JSON file.

        Parameters:
        - alphabetFrequency (str): The alphabet frequency for translation.
        - fileForExport (str): The file name for exporting the JSON (default: "key_alphabet.json").
        - nameForHeaderKey (str): The header name for the translation key (default: "key").
        - nameForHeaderAlphabet (str): The header name for the alphabet (default: "alphabet").

        Raises:
        - Exception: If the file for export already exists.

        Writes the translation key and alphabet frequency information toa JSON file in the specified format.
        """
        if os.path.isfile(fileForExport):
            raise Exception(f"{fileForExport} уже существует")
            
        info = self.getTranslateDictFrequency(alphabetFrequency)

        info1 = {nameForHeaderKey: dict(zip(info.keys(), info.values()))}

        info2 = {nameForHeaderAlphabet: dict(zip(info.values(), info.keys()))}

        info = [info1, info2]

        json_data = json.dumps(info, sort_keys=True, indent=2, ensure_ascii=False)

        with open(fileForExport, 'w') as f:
            f.write(json_data)    