# по сути это усовершенствованный метод простой замены, но большим количеством методов
class Roter:

    def __init__(self, alphabet: str, startPositionRotor: str, step: int = 0):
        
        forRaiseSPR = len(set(startPositionRotor))
        forRaiseAlphabet = len(set(alphabet))

        if len(alphabet) != len(startPositionRotor) or \
           forRaiseAlphabet != forRaiseSPR or forRaiseSPR != len(startPositionRotor) or forRaiseAlphabet != len(alphabet):
            raise Exception(f"Плохие алфавиты. размер первого: {len(alphabet)}, стартовая позиция: {len(startPositionRotor)}")

        self._step = step
        self._originalAlphabet = alphabet
        self._startPositionRotor = startPositionRotor

    def shift(self, step:int  = 1) -> int:
        
        self._step = (step + self._step) % len(self._originalAlphabet)
        return self._step
    
    def __shift(self, step:int  = 1) -> int:
        
        tmpStep = self._step
        self._step = (step + self._step) % len(self._originalAlphabet)
        return tmpStep
    
    def putStartPosition(self) -> None:
        self._step = 0
        return

    @property
    def step(self) -> int:
        return self._step


    @property
    def alphabet(self) -> str:
        return self._originalAlphabet
    
    @property
    def startPositionRoter(self) -> str:
        return self._startPositionRotor

    @property
    def roter(self) -> str:
        
        newStr = ""

        for i in range(len(self._startPositionRotor)):
            newStr += self._startPositionRotor[ (i + self._step)% len(self._startPositionRotor)]
        
        return newStr
    
    def encryptWithoutStep(self, character: str) -> str:

        if len(character) != 1 or not(character in self._originalAlphabet):
            raise Exception("Это ротор, а не шифр замены. Проверь свой символ с помощью getAlphabet()")
        
        return self._startPositionRotor[(self._step + self._originalAlphabet.index(character)) % len(self._originalAlphabet)]
    
    def encrypt(self, character: str, step: int = 1) -> str:

        if len(character) != 1 or not(character in self._originalAlphabet):
            raise Exception("Это ротор, а не шифр замены. Проверь свой символ с помощью getAlphabet()")
        return self._startPositionRotor[(self.__shift(step) + self._originalAlphabet.index(character)) % len(self._originalAlphabet)]
    

    def reverseRoterSafeStep(self) -> "Roter":

        return Roter(self._startPositionRotor, self._originalAlphabet, self._step)
    
    def reverseRoterNotSafeStep(self, step : int = 0) -> "Roter":
        return Roter(self._startPositionRotor, self._originalAlphabet, step)
    


        
