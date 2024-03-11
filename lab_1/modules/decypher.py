from modules.additional_functions import *

def decrypt_by_key(encrypted_text: str, key: dict) -> str:
    '''
    Decrypts the text by frequency analysis using the specified key.
            Parameters:    
                    encrypted_text (str): encrypted text
                    key (dict): encryption key                   
            Return value:
                    str: the function returns 
                    the decrypted text as a string
    '''
    decr_text = ""
    for symbol in encrypted_text:
        decr_text += symbol.replace(symbol, key[symbol])
    return decr_text