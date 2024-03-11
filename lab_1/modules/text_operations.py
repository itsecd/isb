import json

def read_text(path: str) -> str :
    '''
    Reads text from a file.
            Parameters:    
                    path (str): the path to the file                  
            Return value:
                    str: returns the text
    '''
    text = ""
    try:
        with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
        return text
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")

def write_file(path: str, text: str) -> None:
    '''
    Writes text to a file.
            Parameters:    
                    path (str): the path to the file 
                    text (str): the text to be written to a file                 
            Return value:
                    None
    '''  
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
        print("The text has been successfully recorded")
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")

def write_dict_to_json(path: str, data: dict) -> None:
    '''
    Writes the dictionary to a json file.
            Parameters:    
                    path (str): the path to the file 
                    data (dict): the dictionary to be written to a file             
            Return value:
                    None
    '''    
    try:
        with open(path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False)
                file.write('\n')
    except Exception as e:
         print(f"An error occurred while writing to the json file: {str(e)}")    

def read_json(path: str) -> dict:
    '''
    Reads a dictionary from a file.
            Parameters:    
                    path (str): the path to the file
            Return value:
                    dict: returns the dictionary
    '''  
    try:           
        with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
    except Exception as e:
         print(f"An error occurred while reading the json file: {str(e)}")