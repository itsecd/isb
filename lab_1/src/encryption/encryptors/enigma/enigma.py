from typing import List
from .rotor import Rotor

BASIC_SEED = "x(ГkшЪ+4sЩJpШ)0,хRCЕD`ьQEрP2уйXыj.HЙGгЖж*фЭzhfgч№VFтцСtмнХ ЗТ\
              }KЛ%»-Y1ПУ{кMНв3!oZепД;ЦS7:iu#яcЮmO]dОАзъ@8бБqлР/о'«9ЧvAщynЬb\
              Ё[UаI~LewюКэaМд56B&TWФиЯЫё^ВNсrlИ="


class Enigma:
    """
    The enigma class emulates the work of a famous encoder from the 40s.

    - To create an enigma you need to use the roters that are in this
    same directory.
    - The container (sheet) of rotors is passed to the creation constructor, 
    subsequently an enigma is created on its basis.

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
        - rotors (List[Rotor]): A list of rotor objects to be used in the 
        Enigma machine.

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
        
        standart_alphabet_size = len(roters[0].alphabet)
        
        if standart_alphabet_size < 2:
            raise Exception("These are not alphabets, mate. Change the \
                alphabet size for the rotors as their size is less than 2.")

        list_raise = []

        for rotor in roters:

            if rotor.step != 0:
                raise Exception("Rotors should be in the initial position!")

            list_raise = len(rotor.alphabet)
            if len(rotor.alphabet) != standart_alphabet_size:
                raise Exception(f"Adjust the rotors correctly, currently sizes are inconsistent: {list_raise}")
            
        for index_roter in range(len(roters) - 1):

            if roters[index_roter].start_position_rotor != roters[index_roter + 1].alphabet:
                raise Exception(f"The end path of rotor {index_roter + 1} does not match with the arrival of rotor {index_roter + 2}. Please change the start position of the first rotor or the alphabet of the second rotor.")


    def put_roters_in_start_position(self) -> None:
        """
        Put all rotors in their initial start positions.
        """
        for rotor in self._roters:
            rotor.put_start_position()

    @staticmethod
    def encrypt(text: str, roters: List[Rotor], step: int = 1) -> str:
        """
        Encrypt the given text using a list of rotors with a specified 
        encryption step.

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

            tmp_character = c
            spin_next_rotor = True

            for index_rotor in range(len(roters)):
                
                if spin_next_rotor:
                    if roters[index_rotor].step == len(roters[index_rotor].alphabet) - 1 and step > 0:
                        spin_next_rotor = True
                    elif roters[index_rotor].step == 1 and step < 0:
                        spin_next_rotor = True
                    else:
                        spin_next_rotor = False

                    tmp_character = roters[index_rotor].encrypt(tmp_character, step)
                else:
                    tmp_character = roters[index_rotor].encrypt_without_step(tmp_character)
            
            cihep += tmp_character
        
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
        Reset the rotors to their initial positions, then encrypt the input 
        text.

        Parameters:
        - text (str): The text to be encrypted.
        - step (int, optional): The encryption step, default is 1.

        Returns:
        - str: The encrypted text.
        """
        self.put_roters_in_start_position()
        return self.encrypt(text, self._roters, step)

    @staticmethod
    def translate(text: str, roters_encrypt_and_start_position: List[Rotor], 
                  step_for_encrypt_and_start_position: int = 1) -> str:
        """
        Translate the input text using a list of rotors with reversed settings.

        Parameters:
        - text (str): The text to be translated.
        - roters_encrypt_and_start_position (List[Rotor]): List of rotors with encryption and start positions.
        - step_for_encrypt_and_start_position (int, optional): The step for encryption and start positions, default is 1.

        Returns:
        - str: The translated text.
        """
        
        Enigma.rotors_are_tuned(roters_encrypt_and_start_position)

        reversed_roters = []

        for rotor in roters_encrypt_and_start_position[::-1]:
            reversed_roters.append(rotor.reverse_rotor_safe_step())

        return Enigma.encrypt(text, reversed_roters, 
                              -step_for_encrypt_and_start_position)
    
    def translate_old_roters(self, text: str, step: int = 1) -> str:
        """
        Translate the input text using the current set of rotors with reversed
        settings.

        Parameters:
        - text (str): The text to be translated.
        - step (int, optional): The translation step, default is 1.

        Returns:
        - str: The translated text.
        """
        return self.translate(text, self._roters, step)

    def translate_update_roters(self, text: str, step: int = 1) -> str:
        """
        Reset the rotors to their initial positions, then translate the input
        text.
        
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
        - seed (str, optional): Seed value for additional randomness, default 
        seed provided.

        Raises:
        - Exception: If the key length is less than 3 or generating a valid 
        Enigma configuration fails.

        Returns:
        - Enigma: An instance of the Enigma machine created with the generated
        settings.
        """
        if len(set(key)) < 3:
            raise Exception("It makes no sense to build keys less than three")

        size_alphabet = len(set(key))
        alphabet = "".join(sorted(set(key)))

        summ = len(seed)
        for i in range(len(key)):
            summ += ord(key[i]) * i


        trash = seed[0:summ % len(seed)] + "".join(sorted(set(key))) + seed[summ % len(seed) : len(seed)]
        count_massive = summ % 14

        if count_massive < 4:
            count_massive += 4

        alphabets = [alphabet]
        index = 0
        flag = True
        summ = summ * 9 
        while flag:

            test_tmp = ""
            
            for c in range(size_alphabet):
                test_tmp += trash[(summ + index )% len(trash)]
                index += 1
            index -= size_alphabet - 1

            if len(set(test_tmp)) == len(test_tmp) and size_alphabet == len(test_tmp):
                alphabets.append(test_tmp)

            if len(alphabets) == count_massive:
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
        new_str = ""
        for i in self._roters:
            new_str += f"\nRoter№{index}:\n|{i.alphabet}|->|{i.start_position_rotor()}|\n"
            index += 1
        return new_str