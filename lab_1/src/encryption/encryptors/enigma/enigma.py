from typing import List
from .rotor import Rotor

BASIC_SEED = "x(ГkшЪ+4sЩJpШ)0,хRCЕD`ьQEрP2уйXыj.HЙGгЖж*фЭzhfgч№VFтцСtмнХ ЗТ}KЛ%»-Y1ПУ{кMНв3!oZепД;ЦS7:iu#яcЮmO]dОАзъ@8бБqлР/о'«9ЧvAщynЬbЁ[UаI~LewюКэaМд56B&TWФиЯЫё^ВNсrlИ="


class Enigma:
    """
    The enigma class emulates the work of a famous encoder from the 40s.

    - To create an enigma you need to use the roters that are in this
    same directory.
    - The container (sheet) of rotors is passed to the creation constructor, subsequently
    an enigma is created on its basis.

    Attributes:
    _roters (List[Roter]): Container of roters for working with enigma (must
    follow the rotors_are_tuned function standards).

    Methods:
    ...
    """

    def __init__(self, roters: List[Rotor]):
        """
          Constructor for the Enigma machine.

        Parameters:
        - rotors (List[Rotor]): A list of rotor objects to be used in the Enigma machine.

        Returns:
        - None
        """
        Enigma.rotors_are_tuned(roters)
                   
        self._roters = roters

        return

    @staticmethod
    def rotors_are_tuned(roters: List[Rotor]) -> None:
        """
        Check if the rotors are correctly tuned for the Enigma machine.

        Parameters:
        - rotors (List[Rotor]): A list of rotor objects to be checked for correct tuning.

        Returns:
        - None

        Raises:
        - Exception: If the rotors are not properly tuned according to Enigma machine requirements.
        """
        if len(roters) < 1:
            raise Exception("Don't have rotors? Add some rotors, bro!")
        
        standartAlphabetSize = len(roters[0].alphabet)
        
        if standartAlphabetSize < 2:
            raise Exception("These are not alphabets, mate. Change the alphabet size for the rotors as their size is less than 2.")

        listRaise = []

        for rotor in roters:

            if rotor.step != 0:
                raise Exception("Rotors should be in the initial position!")

            listRaise = len(rotor.alphabet)
            if len(rotor.alphabet) != standartAlphabetSize:
                raise Exception(f"Adjust the rotors correctly, currently sizes are inconsistent: {listRaise}")
            
        for indexRoter in range(len(roters) - 1):

            if roters[indexRoter].start_position_rotor != roters[indexRoter + 1].alphabet:
                raise Exception(f"The end path of rotor {indexRoter + 1} does not match with the arrival of rotor {indexRoter + 2}. Please change the start position of the first rotor or the alphabet of the second rotor.")


    def put_roters_in_start_position(self) -> None:
        """
        Put all rotors in their initial start positions.
        """
        for rotor in self._roters:
            rotor.put_start_position()

    @staticmethod
    def encrypt(text: str, roters: List[Rotor], step: int = 1) -> str:
        """
        Encrypt the given text using a list of rotors with a specified encryption step.

        Parameters:
        - text (str): The text to be encrypted.
        - roters (List[Rotor]): List of rotors used for encryption.
        - step (int, optional): The encryption step, default is 1.

        Raises:
        - Exception: If characters in the text are not present in the rotor's alphabet.

        Returns:
        - str: The encrypted text.
        """
        Enigma.rotors_are_tuned(roters)

        if not set(text).issubset(set(roters[0].alphabet)):
            raise Exception("Text characters are not in the router. Give me another text")
        
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
                    tmpCharacter = roters[indexRotor].encrypt_without_step(tmpCharacter)
            
            cihep += tmpCharacter
        
        return cihep

    def encrypt_old_roters(self, text: str, step: int = 1) -> str:
        """
        Encrypt the given text using the current set of rotors.

        Parameters:
        - text (str): The text to be encrypted.
        - step (int, optional): The encryption step, default is 1.

        Returns:
        - str: The encrypted text.
        """
        return self.encrypt(text, self._roters, step)

    def encrypt_update_roters(self, text: str, step: int = 1) -> str:
        """
        Reset the rotors to their initial positions, then encrypt the input text.

        Parameters:
        - text (str): The text to be encrypted.
        - step (int, optional): The encryption step, default is 1.

        Returns:
        - str: The encrypted text.
        """
        self.put_roters_in_start_position()
        return self.encrypt(text, self._roters, step)

    @staticmethod
    def translate(text: str, rotersEncryptAndStartPosition: List[Rotor], stepForEncryptAndStartPosition: int = 1) -> str:
        """
        Translate the input text using a list of rotors with reversed settings.

        Parameters:
        - text (str): The text to be translated.
        - rotersEncryptAndStartPosition (List[Rotor]): List of rotors with encryption and start positions.
        - stepForEncryptAndStartPosition (int, optional): The step for encryption and start positions, default is 1.

        Returns:
        - str: The translated text.
        """
        
        Enigma.rotors_are_tuned(rotersEncryptAndStartPosition)

        reversedRotors = []

        for rotor in rotersEncryptAndStartPosition[::-1]:
            reversedRotors.append(rotor.reverse_rotor_safe_step())

        return Enigma.encrypt(text, reversedRotors, -stepForEncryptAndStartPosition)
    
    def translate_old_roters(self, text: str, step: int = 1) -> str:
        """
        Translate the input text using the current set of rotors with reversed settings.

        Parameters:
        - text (str): The text to be translated.
        - step (int, optional): The translation step, default is 1.

        Returns:
        - str: The translated text.
        """
        return self.translate(text, self._roters, step)

    def translate_update_roters(self, text: str, step: int = 1) -> str:
        """
        Reset the rotors to their initial positions, then translate the input text.
        
        Parameters:
        - text (str): The text to be translated.
        - step (int, optional): The translation step, default is 1.
        
        Returns:
        - str: The translated text.
         """
        self.put_roters_in_start_position()
        return self.translate(text, self._roters, step)

    @staticmethod
    def create_enigma_into_key(key: str, seed: str = BASIC_SEED):
        """
        Create an Enigma machine based on the provided key and seed.

        Parameters:
        - key (str): The key used to generate the Enigma settings.
        - seed (str, optional): Seed value for additional randomness, default seed provided.

        Raises:
        - Exception: If the key length is less than 3 or generating a valid Enigma configuration fails.

        Returns:
        - Enigma: An instance of the Enigma machine created with the generated settings.
        """
        if len(set(key)) < 3:
            raise Exception("It makes no sense to build keys less than three")

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
        summ = summ * 9 
        while flag:

            testTmp = ""
            
            for c in range(sizeAlphabet):
                testTmp += trash[(summ + index )% len(trash)]
                index += 1
            index -= sizeAlphabet - 1

            if len(set(testTmp)) == len(testTmp) and sizeAlphabet == len(testTmp):
                alphabets.append(testTmp)

            if len(alphabets) == countMassive:
                flag = False
            

            if index > len(trash):
                raise Exception("Your key is very bad")
        
        rotors = []
        
        for alp in range(len(alphabets) - 1):
            rotors.append(Rotor(alphabets[alp], alphabets[alp + 1]))

        return Enigma(rotors)

    def get_start_roters(self) -> str:
        """
        Get the starting positions of all rotors in the Enigma machine.

        Returns:
        - str: A formatted string showing the rotor number, alphabet, and start position.
        """
        index = 1
        newStr = ""
        for i in self._roters:
            newStr += f"\nRoter№{index}:\n|{i.alphabet}|->|{i.start_position_rotor()}|\n"
            index += 1
        return newStr