from modules.additional_functions import *

class Mode(Enum):

    ENCRYPT = 'encrypt'
    DECRYPT = 'decrypt'

def сaesar_cypher(text: str, key: int, mode: Mode) -> str:
    '''
    Encrypts or decrypts the source text using the Caesar method using the specified key.
            Parameters:    
                    text (str): the source text
                    key (int): encryption key
                    mode (Mode): select the mode of operation 
                            of the function               
            Return value:
                    str: the function returns the 
                    encrypted text as a string
    '''  
    text = text.upper()
    alphabet = defining_alphabet(text)
   
    final_text = ""
    
    for symbol in text:
        if symbol in alphabet:
            match mode:
                case Mode.ENCRYPT.value:
                    index = (alphabet.index(symbol) + key) % len(alphabet)
                case Mode.DECRYPT.value:
                    index = (alphabet.index(symbol) + (len(alphabet) - key)) % len(alphabet)

            final_text += alphabet[index]
        else:
            final_text += symbol

    return final_text