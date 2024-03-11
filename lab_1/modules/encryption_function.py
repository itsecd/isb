from modules.cypher import *
from modules.decypher import *
from modules.text_operations import *

class Method(Enum):
   CAESAR = 'caesar'
   FREQUENCY = 'frequency'

def encryption_or_decryption_Caesar(mode: Mode,
                                    path_to_key: str, 
                                    path_to_source_text: str, 
                                    path_to_output_file: str) -> None:
   '''
    The function does all the work with encryption in the aggregate.
            Parameters:    
                    mode (Mode): function operation mode ('encrypt' - encrypt text, 'decrypt' - decrypt text)                    
                    path_to_key (str): the path to the encryption key
                    path_to_source_text (str): the path to the source text
                    path_to_output_file (str): the path to the output file
            Return value:
                    None
    '''
   if not path_to_key or not path_to_source_text or not path_to_output_file:
         print('to perform the action, you must specify the encryption key, '
               'the path to the text file and the path to the output file') 

   else:
         try:
            source_text = read_text(path_to_source_text)
            key = read_json(path_to_key)['key']
            final_text = сaesar_cypher(source_text, key, mode)
            write_file(path_to_output_file, final_text) 
         except Exception as e:
            print(f'An error occurred while encrypting: {str(e)}')

def decryption_frequency_analysis(path_to_key: str, 
                                    path_to_source_text: str, 
                                    path_to_output_file: str) -> None:
   '''
    The function does all the work with encryption in the aggregate.
            Parameters:                                           
                    path_to_key (str): the path to the encryption key
                    path_to_source_text (str): the path to the source text
                    path_to_output_file (str): the path to the output file
            Return value:
                    None
    '''
   if not path_to_key or not path_to_source_text or not path_to_output_file:
         print('to perform the action, you must specify the encryption key, '
               'the path to the text file and the path to the output file') 
   else:
         try:
            source_text = read_text(path_to_source_text)
            key = read_json(path_to_key)
            final_text = decrypt_by_key(source_text, key)
            write_file(path_to_output_file, final_text)
         except Exception as e:
            print(f'An error occurred while encrypting: {str(e)}')
