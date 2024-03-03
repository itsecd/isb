class Vigener:

    operation = lambda x, y, translate: x + y if not translate else x - y

    def __init__(self, alphabet: str, key: str):

        Vigener.checkRaise(alphabet, key)

        self._alphabet = alphabet
        self._key = key

    @staticmethod
    def encoder(alphabet: str, key: str, text: str) -> str:
        return Vigener.__encoder(alphabet, key, text, False)
    
    def encrypt(self, text) -> str:
        return Vigener.__encoder(self._alphabet, self._key, text, False)
    
    @staticmethod
    def translator(alphabet: str, key: str, text: str) -> str:
        return Vigener.__encoder(alphabet, key, text, True)
    
    def translate(self, text) -> str:
        return Vigener.__encoder(self._alphabet, self._key, text, True)


    @staticmethod
    def __encoder(alphabet: str, key: str, text: str, translate: bool = False) -> str:
        
        Vigener.checkRaise(alphabet, key)

        if len(text) == 0:
            raise Exception("Мне нечего зашифровывать или расшифровывать")
        
        encode = ""
        indexForKey = 0    

        for c in text:
                
            indexLetterInOriginalAlphabet = (  Vigener.operation(alphabet.index(c), alphabet.index(key[indexForKey % len(key)]), translate)) % len(alphabet)
            encode += alphabet[indexLetterInOriginalAlphabet]
            indexForKey += 1
        
        return encode

    def checkRaise(alphabet: str, key: str) -> None:
        
        if  len(set(alphabet)) != len(alphabet):
            raise Exception("Твой алфавит - не алфавит. Не все буквы уникальны. Смени алфавит")
        
        if not all( elem in alphabet for elem in sorted(set(key)) ):
            raise Exception("Буквы твоего ключа не содержатся в алфавите. Исправь ключ")
        
        if len(alphabet) == 0:
            raise Exception("Мне не с чем работать. Алфавита не существует")
        
        if len(key) == 0:
            raise Exception("Мне не с чем работать. Ключа не существует")
            


