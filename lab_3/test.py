import os


def generate_symmetric_key():
    return os.urandom(16)


def seriliaze_key(path:str, key:str)-> None:
    with open(path,'wb') as file:
        file.write(key)


def deseriliaze_key(path:str) -> str:
    with open(path,'rw') as file:
        return file.read()

a=generate_symmetric_key()
print(a)

