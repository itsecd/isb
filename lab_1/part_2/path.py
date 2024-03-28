import os

def path_settings()->str:
    """
    Все пути к файлам нужно проработать во 2 части
    Agruments:
        None
    Returns:
        input_file_path: Путь к файлу, в котором есть исходный текст необходимо расшифровать.
        freq_dict_path: Путь к файлу, в котором есть частота символов
        key_dict_path: Путь к файлу, в котором есть ключ расшифровки.
        output_file_path: Путь к файлу, в котором содержит расшифрованный текст.
    """
    abs_path = os.path.abspath("")
    input_file_path=os.path.join(abs_path,"part_2","cod1.txt")
    freq_dict_path=os.path.join(abs_path,"part_2","frep.json")
    key_dict_path=os.path.join(abs_path,"part_2","key.json")
    output_file_path=os.path.join(abs_path,"part_2","decoded_text.txt")

    return input_file_path, freq_dict_path, key_dict_path,output_file_path
