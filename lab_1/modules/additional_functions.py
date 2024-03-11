from enum import Enum

class Language(Enum):

    RUS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ENG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def defining_alphabet(text: str) -> str:
    '''
    Determines which language is used in the text.
            Parameters:    
                    text (str): the text being checked                   
            Return value:
                    str: the function returns a string 
                    with the selected alphabet
    '''
    if any(char in Language.RUS.value for char in text):
        return Language.RUS.value
    else:
        return Language.ENG.value
    
        
def frequency_analysis(text: str) -> dict:
    '''
    Performs a frequency analysis of the text.
            Parameters:    
                    text (str): the text that is being analyzed                   
            Return value:
                    dict: the function returns a sorted 
                    dictionary with frequency analysis data
    '''
    frequency = {}
    length = len(text)
    for symbol in set(text):
        count = text.count(symbol)
        frequency[symbol] = round((count / length), 6)
    
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

def get_key(dict1: dict, dict2: dict) -> dict:
    '''
    Auxiliary function for obtaining the encryption key 
    (the keys of both dictionaries are taken and combined into one).
            Parameters:    
                    dict1 (dict): the first dictionary
                    dict2 (dict): the second dictionary                  
            Return value:
                    dict: the function returns a dictionary 
                    with a ready-made key
    '''
    encryption_key = {}
    keys_list = list(dict2.keys())
    for key1 in dict1.keys():
        if keys_list:
            key2 = keys_list.pop(0)
            encryption_key[key2] = key1
    return encryption_key

