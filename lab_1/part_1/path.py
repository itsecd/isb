import os

def path_settings()->str:
    """
    Все пути к файлам нужно проработать во 1 части.
    Arguments:
        None.
    Returns:
        input_path: Путь к файлу, содержащему исходный текст, который нужно зашифровать.
        output_path: Путь к файлу, в котором содержит зашифрованный текст.
        step_path: Путь к файлу, в котором содержит ключ зашифровки.
        alphabet_path: Путь к файлу, в котором содержит символы
    """
    abs_path = os.path.abspath("")
    input_path=os.path.join(abs_path,"part_1","original_text.txt")
    output_path=os.path.join(abs_path,"part_1","encode_text.txt")
    step_path=os.path.join(abs_path,"part_1","step.txt")
    alphabet_path=os.path.join(abs_path,"part_1","alphabet.txt")

    return input_path, output_path, step_path, alphabet_path