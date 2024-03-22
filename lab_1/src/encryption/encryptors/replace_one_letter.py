class ReplaceOneLetter:
    """
    Class for encryption and decryption using a one-to-one replacement cipher.
    
    Attributes:
        _encryptor (dict): Dictionary mapping each character from the 
        alphabet to its corresponding character in the cipher.
        _translator (dict): Dictionary mapping each character from the 
        cipher back to its original character in the alphabet.
    """


    def __init__(self, alphabet: str, cihep: str):
        """
        Initialize the ReplaceOneLetter object with the specified alphabet 
        and cipher.
        
        Args:
            alphabet (str): The original alphabet.
            cihep (str): The corresponding cipher characters.
        
        Raises:
            Exception: If the length of the alphabet does not match the 
            length of the cipher or if there are duplicates.
        """
        
        if len(alphabet) != len(cihep) \
           or ReplaceOneLetter.check_duplicatesIn_string(alphabet)\
           or ReplaceOneLetter.check_duplicatesIn_string(cihep):
                
            raise Exception("Length alphabet != cihep or (alphabet or cihep\
                             have duplicates)")

        self._encryptor = dict(zip(alphabet, cihep))
        self._translator = dict(zip(cihep, alphabet))
    
    def encrypt(self, text_for_encrypt: str) -> str:
        """
        Encrypts the input text using the defined cipher.
        
        Args:
            text_for_encrypt (str): The text to be encrypted.
        
        Returns:
            str: The encrypted text.
        
        Raises:
            Exception: If the text contains characters that are not in the
            dictionary.
        """
        
        if not self.have_all_charactersIn_text(text_for_encrypt, 
                                               self._encryptor.keys()):
            raise Exception("The text contains characters that are not in the\
                             dictionary")
        
        encryptik = ""

        for i in text_for_encrypt:
            encryptik += self._encryptor[i]

        return encryptik

    def translate(self, textForTranslate: str) -> str:
        """
        Translates the input text using the defined cipher.
        
        Args:
            textForTranslate (str): The text to be translated back to the 
            original alphabet.
        
        Returns:
            str: The translated text.
        
        Raises:
            Exception: If the text contains characters that are not in the 
            dictionary.
        """
        
        if not self.have_all_charactersIn_text(textForTranslate, 
                                               self._translator.keys()):
            raise Exception("The text contains characters that are not in the\
                             dictionary")
        
        encryptik = ""

        for i in textForTranslate:
            encryptik += self._translator[i]

        return encryptik

    @staticmethod
    def check_duplicatesIn_string(string: str) -> bool:
        """
        Check if a given string contains duplicates.
        
        Args:
            string (str): The string to check for duplicates.
            
        Returns:
            bool: True if duplicates are found, False otherwise.
        """
        return len(set(string)) != len(string)
    
    @staticmethod
    def have_all_charactersIn_text(text: str, characters: set) -> bool:
        """
        Check if all characters in a text are present in a given set of 
        characters.
        
        Args:
            text (str): The text to check.
            characters (set): Set of characters to compare against.
            
        Returns:
            bool: True if all characters are present, False otherwise.
        """
        
        for i in set(text):
            
            if i not in characters:
                return False
            
        return True