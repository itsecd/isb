class Vigenere:
    """
    Represents a Vigenere cipher for encryption and decryption.

    Attributes:
    - _alphabet (str): The alphabet used for the Vigenere cipher.
    - _key (str): The key for the Vigenere cipher.
    """

    def __init__(self, alphabet: str, key: str):
        """
        Initialize the Enigma machine with the provided alphabet and key.

        Parameters:
        - alphabet (str): The alphabet used for the Enigma machine.
        - key (str): The key representing the initial settings of the Enigma machine.

        Raises:
        - Exception: If the key contains characters not present in the alphabet,
                    or if the key length is greater than the alphabet length,
                    or if the alphabet contains duplicate characters.
        """
        if not all( elem in alphabet for elem in key ) or len(set(key)) > len(alphabet) or len(set(alphabet)) != len(alphabet):
            raise Exception("Your key not contants in alphabet or this is not alphabet or key")
        

        self._alphabet = alphabet
        self._key = key

    @staticmethod
    def encrypt(alphabet: str, key: str, text: str) -> str:
        """
        Encrypt the input text using the Vigenere cipher.

        Parameters:
        - alphabet (str): The alphabet used for the Vigenere cipher.
        - key (str): The key for encryption.
        - text (str): The text to be encrypted.

        Returns:
        - str: The encrypted text.
        """
        
        if not all( elem in alphabet for elem in key ) or len(set(alphabet)) != len(alphabet)\
           or len(set(text)) > len(alphabet) or len(alphabet) == 0 or len(key) == 0 or len(text) == 0:
            raise Exception("Your key not contants in alphabet or bad alphabet")
        
        cihep = ""

        indexForKey = 0

        for c in text:
                
            indexLetterInOriginalAlphabet = (alphabet.index(key[indexForKey % len(key)]) + alphabet.index(c)) % len(alphabet)
            cihep += alphabet[indexLetterInOriginalAlphabet]
            indexForKey += 1
        
        return cihep

    @staticmethod
    def translate(alphabet: str, key: str, text: str) -> str:
        """
        Decrypt the input text using the Vigenere cipher.

        Parameters:
        - alphabet (str): The alphabet used for the Vigenere cipher.
        - key (str): The key for decryption.
        - text (str): The text to be decrypted.

        Returns:
        - str: The decrypted text.
        """
        if not all( elem in alphabet for elem in key ) or len(set(alphabet)) != len(alphabet)\
           or len(set(text)) > len(alphabet) or len(alphabet) == 0 or len(key) == 0 or len(text) == 0:
            raise Exception("Your key not contants in alphabet or bad alphabet")

        cihep = ""

        indexForKey = 0

        for c in text:
                
            indexLetterInOriginalAlphabet = (alphabet.index(c) - alphabet.index(key[indexForKey % len(key)])) % len(alphabet)
            cihep += alphabet[indexLetterInOriginalAlphabet]
            indexForKey += 1
        
        return cihep