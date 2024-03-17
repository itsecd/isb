from typing import List
from .Roter import Roter

#Функция претендует быть похожей на машину энигма, однако есть ряд ключевых отличий. Во-первых ротеры идут только в одну

class Enigma:
    """
    Класс претендует быть похожим на машину энигма, но есть ряд ключевых отличий.
    
    1. Мы не ограничены никаким алфавитом для ротеров.
    2. Текст поступает только в одну сторону(мы не имеем рефлектора). То есть начальные значения конечного ротера(перевод) - есть язык перевода символов.
    3. Между ротерами существует связь. Стартовое положение первого должны совпадать с алфавитом второго ротера. Чтобы однозначно переводить символы из первого ротера во второй.
    4. Возможна автоматическая генерация ротеров с помощью функции, начальные положения ротеров можно получить с помощью функции getRoters()
    5. Для генерации ключей можно поменять константу, чтобы они были разные
    6. Существует понятие шага для каждого ротера. То есть можно задать смещение при шифровании и дешифровании для алфавитов каждого ротера. Это реализовано в функциях шифрования и дешифрования
    ...
    Атрибуты
    --------
    _roters : List[Rotor]
        Содержит список используемых ротеров одинаковой длинны алфавита
    Методы
    ------
    """

    #КОНСТАНТА ДЛЯ КЛЮЧЕЙ. ВСЕ ЗНАЧЕНИЯ УНИКАЛЬНЫ
    CONST_FOR_CREATE_KEY = "x(ГkшЪ+4sЩJpШ)0,хRCЕD`ьQEрP2уйXыj.HЙGгЖж*фЭzhfgч№VFтцСtмнХ ЗТ}KЛ%»-Y1ПУ{кMНв3!oZепД;ЦS7:iu#яcЮmO]dОАзъ@8бБqлР/о'«9ЧvAщynЬbЁ[UаI~LewюКэaМд56B&TWФиЯЫё^ВNсrlИ="
        

    @staticmethod
    def rotorsAreTuned(roters: List[Roter]) -> None:

        if len(roters) < 1:
            raise Exception("Don't have roters? Добавь роторы б")
        
        standartAlphabetSize = len(roters[0].alphabet)
        
        if standartAlphabetSize < 2:
            raise Exception("Это не алфавиты, д. Измени размер алфавита для ротеров их размер <2")

        listRaise = []

        for roter in roters:

            if roter.step != 0:
                raise Exception("Ротеры должны быть в нулевом положении!")

            listRaise = len(roter.alphabet)
            if len(roter.alphabet) != standartAlphabetSize:
                raise Exception(f"Настрой правильно ротеры, сейчас размеры: {listRaise}")
            
        for indexRoter in range(len(roters) - 1):

            if roters[indexRoter].startPositionRoter != roters[indexRoter + 1].alphabet:
                raise Exception(f"Конечный путь ротера {indexRoter + 1} не совпадает с приездом ротера {indexRoter + 2}. Измени startPosition первого ротера или alphabet второго ротера")
                        
    def __init__(self, roters: List[Roter]):
        
        Enigma.rotorsAreTuned(roters)
                   
        self._roters = roters

        return
    
    def putRotorsInStartPosition(self) -> None:
        
        for rotor in self._roters:
            rotor.putStartPosition()

    @staticmethod
    def encrypt(text: str, roters: List[Roter], step: int = 1) -> str:

        Enigma.rotorsAreTuned(roters)

        if not set(text).issubset(set(roters[0].alphabet)):
            raise Exception("Символы текста не находятся в ротере. Давай другой текст д")
        
        cihep = ""

        for c in text:

            tmpCharacter = c
            spinNextRotor = True

            for indexRotor in range(len(roters)):
                
                if spinNextRotor:
                    if roters[indexRotor].step == len(roters[indexRotor].alphabet) - 1 and step > 0:
                        spinNextRotor = True
                    elif roters[indexRotor].step == 1 and step < 0:
                        spinNextRotor = True
                    else:
                        spinNextRotor = False

                    tmpCharacter = roters[indexRotor].encrypt(tmpCharacter, step)
                else:
                    tmpCharacter = roters[indexRotor].encryptWithoutStep(tmpCharacter)
            
            cihep += tmpCharacter
        
        return cihep

    def encryptOldRotors(self, text: str, step: int = 1) -> str:
        return self.encrypt(text, self._roters, step)

    def encrypt_update_rotors(self, text: str, step: int = 1) -> str:
        self.putRotorsInStartPosition()
        return self.encrypt(text, self._roters, step)

    @staticmethod
    def translate(text: str, rotersEncryptAndStartPosition: List[Roter], stepForEncryptAndStartPosition: int = 1) -> list:

        Enigma.rotorsAreTuned(rotersEncryptAndStartPosition)

        reversedRotors = []

        for rotor in rotersEncryptAndStartPosition[::-1]:
            reversedRotors.append(rotor.reverseRoterSafeStep())

        return Enigma.encrypt(text, reversedRotors, -stepForEncryptAndStartPosition)
    
    def translateOldRotors(self, text: str, step: int = 1) -> str:
        return self.translate(text, self._roters, step)

    def translate_update_rotors(self, text: str, step: int = 1) -> str:
        self.putRotorsInStartPosition()
        return self.translate(text, self._roters, step)


    @staticmethod
    def __swapLettersInText(text: str, letter_1: str, letter_2: set) -> str:

        if letter_1 >= len(text) or letter_1 < 0 or letter_2 >= len(text) or letter_2 < 0:
            
            raise Exception("Буквы не части текста, или они не буквы")
        
        new_text = ""
        for char in range(len(text)):
            if char == letter_1:
                new_text += text[letter_2]
            elif char == letter_2:
                new_text += text[letter_1]
            else:
                new_text += text[char]
        
        return new_text

    @staticmethod
    def create_enigma_into_key(key: str, seed: str="x(ГkшЪ+4sЩJpШ)0,хRCЕD`ьQEрP2уйXыj.HЙGгЖж*фЭzhfgч№VFтцСtмнХ ЗТ}KЛ%»-Y1ПУ{кMНв3!oZепД;ЦS7:iu#яcЮmO]dОАзъ@8бБqлР/о'«9ЧvAщynЬbЁ[UаI~LewюКэaМд56B&TWФиЯЫё^ВNсrlИ=") -> "Enigma":

        if len(set(key)) < 3:
            raise Exception("Бессмысленно строить ключи меньше трёх")

        sizeAlphabet = len(set(key))
        alphabet = "".join(sorted(set(key)))

        summ = len(seed)
        for i in range(len(key)):
            summ += ord(key[i]) * i


        trash = ""
        ak = seed
        trash = ak[0:summ % len(ak)] + "".join(sorted(set(key))) + ak[summ % len(ak) : len(ak)] 

        countMassive = summ % 14

        if countMassive < 4:
            countMassive += 4

        alphabets = [alphabet]
        index = 0
        flag = True

        while flag:

            testTmp = ""
            
            for c in range(sizeAlphabet):
                testTmp += trash[(summ + index )% len(trash)]
                summ = summ * 9 + 2
                index += 1
            index -= (sizeAlphabet + 1)

            if len(set(testTmp)) == len(testTmp) and sizeAlphabet == len(testTmp):
                alphabets.append(testTmp)

            if len(alphabets) == countMassive:
                flag = False
            

            if index > len(trash):
                raise Exception("Меняй ключ, по нему невозможно построить норм шифратор")
        
        rotors = []
        
        for alp in range(len(alphabets) - 1):
            rotors.append(Roter(alphabets[alp], alphabets[alp + 1]))

        return Enigma(rotors)

    def getStartRoters(self) -> str:
        index = 1
        newStr = ""
        for i in self._roters:
            newStr += f"\nRoter№{index}:\n|{i.alphabet}|->|{i.startPositionRoter}|\n"
            index += 1
        return newStr

    

