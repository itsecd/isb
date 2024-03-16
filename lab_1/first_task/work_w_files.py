import logging 

def read_file(path: str) -> str:
    """
    reads data from a file and returns an array of strings
    """
    try:
        with open(path,'r', encoding ='utf-8') as file:
            return file.read()
    except:
        logging.error('error in read_file')
    
def write_file(path: str, new_text: list[str]) -> None:
    """
    write data to file
    """
    try:
        with open(path, 'w', encoding ='utf-8') as file:
            for char in new_text: 
                file.write(char)
    except:
        logging.error('error in write_file')

def json_to_dict(path: str) -> dict:
    """
    make json to dict
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
           return json.load(file)
    except:
        logging.error('error in json_to_dict')
        
