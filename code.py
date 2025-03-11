def caesar_code(text, shift, alph):
    """
    Function to code your text
    :param text: plain text
    :param shift: key to code
    :param alph: alphabet
    :return: text
    """

    code_alph = alph[shift:] + alph[:shift]
    table_to_code = str.maketrans(alph, code_alph)
    return text.translate(table_to_code)

