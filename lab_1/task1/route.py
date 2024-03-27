import logging

logging.basicConfig(level=logging.INFO)


def route_transposition(text : str, keyword : str) -> str:
    """Encrypts text from file using route transposition method.
    :param text: str of text that is needed to encrypt
    "param keyword: keyword for route transposition method
    :return: str of encrypted text
    """
    try:
        route = [keyword.index(char) for char in sorted(keyword)]
        for i in range(len(route) - 1):
            if route[i] == route[i+1]:
                route[i + 1] = keyword.index(keyword[route[i]], route[i] + 1)
        width = max(route) + 1
        encrypted_text=""
        height = int((len(text)) / (width + 1)) + 1
        matrix = [[text[((width * j) + i) % len(text)] for i in range(width)] for j in range(height)]
        for i in route:
            for j in range(height):
                encrypted_text += matrix[j][i]
        return encrypted_text
    except Exception as exc:
        logging.error(f'Encrypting error: {exc}\n')
