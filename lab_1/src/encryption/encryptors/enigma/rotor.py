class Rotor:
    """
    Class representing a rotor in an Enigma machine.
    """
    def __init__(self, alphabet: str, start_position_rotor: str, 
                 step: int = 0):
        """
        Initialize a Rotor object with the specified alphabet, start position,
        and optional step.

        Parameters:
        - alphabet (str): The alphabet string to be used on the rotor.
        - start_position_rotor (str): The starting position of the rotor.
        - step (int, optional): The step of the rotor, default is 0.

        Returns:
        - None

        Raises:
        - Exception: If the lengths or uniqueness of alphabet and starting 
        position are not consistent.
        """
        for_raise_spr = len(set(start_position_rotor))
        for_raise_alphabet = len(set(alphabet))

        if len(alphabet) != len(start_position_rotor) \
           or for_raise_alphabet != for_raise_spr \
           or for_raise_spr != len(start_position_rotor) \
           or for_raise_alphabet != len(alphabet):
            raise Exception(f"Invalid alphabets. Alphabet size: {len(alphabet)}, Start Position size: { len(start_position_rotor)}")

        self._step = step
        self._original_alphabet = alphabet
        self._start_position_rotor = start_position_rotor

    def shift(self, step:int  = 1) -> int:
        """
        Shift the rotor by the specified number of steps.

        Parameters:
        - step (int, optional): The number of steps to shift the rotor by, 
        default is 1.

        Returns:
        - int: The new step position of the rotor.
        """
        self._step = (step + self._step) % len(self._original_alphabet)
        return self._step
    
    def __shift(self, step:int  = 1) -> int:
        """
        Shift the rotor by the specified number of steps internally without 
        updating the step attribute.

        Parameters:
        - step (int, optional): The number of steps to shift the rotor by, 
        default is 1.

        Returns:
        - int: The previous step position of the rotor before shifting.
        """
        tmp_step = self._step
        self._step = (step + self._step) % len(self._original_alphabet)
        return tmp_step
    
    def put_start_position(self) -> None:
        """
        Reset the rotor to its initial start position.
        """
        self._step = 0
        return

    @property
    def step(self) -> int:
        """
        Get the current step position of the rotor.

        Returns:
        - int: The current step position.
        """
        return self._step


    @property
    def alphabet(self) -> str:
        """
        Get the alphabet used on the rotor.

        Returns:
        - str: The alphabet string.
        """
        return self._original_alphabet
    
    @property
    def start_position_rotor(self) -> str:
        """
        Get the current start position of the rotor.

        Returns:
        - str: The starting position of the rotor.
        """
        return self._start_position_rotor

    @property
    def rotor(self) -> str:
        """
        Get the rotor mapping based on the current step position.

        Returns:
        - str: The character mapping based on the rotor's current position 
        after stepping.
        """
        new_str = ""

        for i in range(len(self._start_position_rotor)):
            new_str += self._start_position_rotor[ (i + self._step)% len(self._start_position_rotor)]
        
        return new_str
    
    def encrypt_without_step(self, character: str) -> str:
        """
        Encrypt a character using the rotor without changing the step 
        position.

        Parameters:
        - character (str): The character to be encrypted.

        Returns:
        - str: The encrypted character.
        """
        if len(character) != 1 or not(character in self._original_alphabet):
            raise Exception("Это ротор, а не шифр замены. Проверь свой \
                            символ с помощью getAlphabet()")
        
        return self._start_position_rotor[(self._step + self._original_alphabet.index(character)) % len(self._original_alphabet)]
    
    def encrypt(self, character: str, step: int = 1) -> str:
        """
        Encrypt a character using the rotor with the specified step.

        Parameters:
        - character (str): The character to be encrypted.
        - step (int, optional): The number of steps to shift the rotor by
        during encryption, default is 1.

        Returns:
        - str: The encrypted character.
        """
        if len(character) != 1 or not(character in self._original_alphabet):
            raise Exception("Это ротор, а не шифр замены. Проверь свой символ\
                             с помощью getAlphabet()")
        
        return self._start_position_rotor[(self.__shift(step) + self._original_alphabet.index(character)) % len(self._original_alphabet)]
    

    def reverse_rotor_safe_step(self) -> "Rotor":
        """
        Create a new Rotor object with the same settings as the current 
        rotor, preserving the step position.

        Returns:
        - Rotor: A new Rotor object with the same settings and step position.
        """
        return Rotor(self._start_position_rotor, self._original_alphabet, 
                     self._step)
    
    def reverse_rotor_not_safe_step(self, step : int = 0) -> "Rotor":
        """
        Create a new Rotor object with the same settings as the current 
        rotor, allowing for a different step setting.

        Parameters:
        - step (int, optional): The step position for the new rotor, default 
        is 0.

        Returns:
        - Rotor: A new Rotor object with the specified step position.
        """
        return Rotor(self._start_position_rotor, 
                     self._original_alphabet, 
                     step)