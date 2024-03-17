class ReplaceOneLetter:


    def __init__(self, alphabet: str, cihep: str):
        
        if len(alphabet) != len(cihep) or ReplaceOneLetter.checkDuplicatesInString(alphabet) or ReplaceOneLetter.checkDuplicatesInString(cihep):
            raise Exception("Length alphabet != cihep or (alphabet or cihep have duplicates)")

        self._encryptor = dict(zip(alphabet, cihep))
        self._translator = dict(zip(cihep, alphabet))
    
    def encrypt(self, textForEncrypt: str) -> str:

        if not self.haveAllCharactersInText(textForEncrypt, self._encryptor.keys()):
            raise Exception("The text contains characters that are not in the dictionary")
        
        encryptik = ""

        for i in textForEncrypt:
            encryptik += self._encryptor[i]

        return encryptik

    def translate(self, textForTranslate: str) -> str:

        if not self.haveAllCharactersInText(textForTranslate, self._translator.keys()):
            raise Exception("The text contains characters that are not in the dictionary")
        
        encryptik = ""

        for i in textForTranslate:
            encryptik += self._translator[i]

        return encryptik

    @staticmethod
    def checkDuplicatesInString(string: str) -> bool:
        
        return len(set(string)) != len(string)
    
    @staticmethod
    def haveAllCharactersInText(text: str, characters: set) -> bool:
        
        for i in set(text):
            
            if i not in characters:
                return False
            
        return True
        

        
