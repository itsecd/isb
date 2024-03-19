class Rotor:
    """
    Class representing a rotor in an Enigma machine.
    """
    def __init__(self, alphabet: str, startPositionRotor: str, step: int = 0):
        """
        Initialize a Rotor object with the specified alphabet, start position, and optional step.

        Parameters:
        - alphabet (str): The alphabet string to be used on the rotor.
        - startPositionRotor (str): The starting position of the rotor.
        - step (int, optional): The step of the rotor, default is 0.

        Returns:
        - None

        Raises:
        - Exception: If the lengths or uniqueness of alphabet and starting position are not consistent.
        """
        forRaiseSPR = len(set(startPositionRotor))
        forRaiseAlphabet = len(set(alphabet))

        if len(alphabet) != len(startPositionRotor) or \
           forRaiseAlphabet != forRaiseSPR or forRaiseSPR != len(startPositionRotor) or forRaiseAlphabet != len(alphabet):
            raise Exception(f"Invalid alphabets. Alphabet size: {len(alphabet)}, Start Position size: { len(startPositionRotor)}")

        self._step = step
        self._originalAlphabet = alphabet
        self._startPositionRotor = startPositionRotor

    def shift(self, step:int  = 1) -> int:
        """
        Shift the rotor by the specified number of steps.

        Parameters:
        - step (int, optional): The number of steps to shift the rotor by, default is 1.

        Returns:
        - int: The new step position of the rotor.
        """
        self._step = (step + self._step) % len(self._originalAlphabet)
        return self._step
    
    def __shift(self, step:int  = 1) -> int:
        """
        Shift the rotor by the specified number of steps internally without updating the step attribute.

        Parameters:
        - step (int, optional): The number of steps to shift the rotor by, default is 1.

        Returns:
        - int: The previous step position of the rotor before shifting.
        """
        tmpStep = self._step
        self._step = (step + self._step) % len(self._originalAlphabet)
        return tmpStep
    
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
        return self._originalAlphabet
    
    @property
    def start_position_rotor(self) -> str:
        """
        Get the current start position of the rotor.

        Returns:
        - str: The starting position of the rotor.
        """
        return self._startPositionRotor

    @property
    def rotor(self) -> str:
        """
        Get the rotor mapping based on the current step position.

        Returns:
        - str: The character mapping based on the rotor's current position after stepping.
        """
        newStr = ""

        for i in range(len(self._startPositionRotor)):
            newStr += self._startPositionRotor[ (i + self._step)% len(self._startPositionRotor)]
        
        return newStr
    
    def encrypt_without_step(self, character: str) -> str:
        """
        Encrypt a character using the rotor without changing the step position.

        Parameters:
        - character (str): The character to be encrypted.

        Returns:
        - str: The encrypted character.
        """
        if len(character) != 1 or not(character in self._originalAlphabet):
            raise Exception("Это ротор, а не шифр замены. Проверь свой символ с помощью getAlphabet()")
        
        return self._startPositionRotor[(self._step + self._originalAlphabet.index(character)) % len(self._originalAlphabet)]
    
    def encrypt(self, character: str, step: int = 1) -> str:
        """
        Encrypt a character using the rotor with the specified step.

        Parameters:
        - character (str): The character to be encrypted.
        - step (int, optional): The number of steps to shift the rotor by during encryption, default is 1.

        Returns:
        - str: The encrypted character.
        """
        if len(character) != 1 or not(character in self._originalAlphabet):
            raise Exception("Это ротор, а не шифр замены. Проверь свой символ с помощью getAlphabet()")
        return self._startPositionRotor[(self.__shift(step) + self._originalAlphabet.index(character)) % len(self._originalAlphabet)]
    

    def reverse_rotor_safe_step(self) -> "Rotor":
        """
        Create a new Rotor object with the same settings as the current rotor, preserving the step position.

        Returns:
        - Rotor: A new Rotor object with the same settings and step position.
        """
        return Rotor(self._startPositionRotor, self._originalAlphabet, self._step)
    
    def reverse_rotor_not_safe_step(self, step : int = 0) -> "Rotor":
        """
        Create a new Rotor object with the same settings as the current rotor, allowing for a different step setting.

        Parameters:
        - step (int, optional): The step position for the new rotor, default is 0.

        Returns:
        - Rotor: A new Rotor object with the specified step position.
        """
        return Rotor(self._startPositionRotor, self._originalAlphabet, step)