class Vigenere:


    def __init__(self, alphabet: str, key: str):

        if not all( elem in alphabet for elem in key ) or len(set(key)) > len(alphabet) or len(set(alphabet)) != len(alphabet):
            raise Exception("Your key not contants in alphabet or this is not alphabet or key")
        

        self._alphabet = alphabet
        self._key = key

    @staticmethod
    def encrypt(alphabet: str, key: str, text: str) -> str:

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

        if not all( elem in alphabet for elem in key ) or len(set(alphabet)) != len(alphabet)\
           or len(set(text)) > len(alphabet) or len(alphabet) == 0 or len(key) == 0 or len(text) == 0:
            raise Exception("Your key not contants in alphabet or bad alphabet")
        
        alphabetDict = dict(zip(alphabet, range(len(alphabet))))

        cihep = ""

        indexForKey = 0

        for c in text:
                
            indexLetterInOriginalAlphabet = (alphabet.index(c) - alphabet.index(key[indexForKey % len(key)])) % len(alphabet)
            cihep += alphabet[indexLetterInOriginalAlphabet]
            indexForKey += 1
        
        return cihep

            


