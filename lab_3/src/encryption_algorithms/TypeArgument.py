from enum import Enum

class TypeArgument(Enum):
    
    """
    This class represents the type of argument for the length of the padding 
    block or key.

    Attributes:
        - BIT: The type of argument is bits.
        - BYTE: The type of argument is bytes.
    """
    
    BIT = 1
    BYTE = 2

    @property
    def bytes(self):
       
        """
        Returns the value of the argument in bytes.

        Returns:
            - The value of the argument in bytes.
        """
       
        return {
            TypeArgument.BIT: 0.125,
            TypeArgument.BYTE: 1,
        }[self]

    @property
    def bits(self):
        
        """
        Returns the value of the argument in bits.

        Returns:
            - The value of the argument in bits.
        """
        
        return {
            TypeArgument.BIT: 1,
            TypeArgument.BYTE: 8,
        }[self]