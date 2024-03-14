import logging 

def read_file(path: str) -> list[str]:
    """
    reads data from a file and returns an array of strings
    """
    try:
        with open(path,'r', encoding ='utf-8') as file:
            return file.readlines()
    except:
        logging.error('error in read_file')
    
def write_file(path: str, new_text: list[str]):
    """
    write data to file
    """
    try:
        with open(path, 'w', encoding ='utf-8') as file:
            for char in new_text: 
                file.write(char)
    except:
        logging.error('error in write_file')
