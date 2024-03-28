def read_from_file(path: str) -> str:
    """
    Читает данные в файл.
    Argument:
        path : Путь к файлу, в который нужно читать данные. Тип str.
    Return:
        Данные, которые записаны в файл. Тип str.
    """
    try:
        with open(path, "r+", encoding="utf-8") as file:
            data = file.read()
        return data
    except Exception as ex:
       raise Exception(f"Failed to open file or file was not found!\n Exception:{ex}\n")

def write_to_file(path: str, data: str) -> None:
    """
    Записывает данные в файл.
    Arguments:
        path : Путь к файлу, в который нужно записать данные. Тип str.
        data : Данные для записи в файл. Тип str.
    Return:
        None
    """
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as ex:
        raise Exception(f"Failed to write data or file was not found!\n Exception:{ex}\n")