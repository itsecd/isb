import re
import logging


logging.basicConfig(level=logging.INFO)


def open_file(path: str) -> str:
    with open(path, "r+", encoding="utf-8") as file:  # чтение и запись
        main = file.read()
    return main


def write_text(path: str, data: str) -> None:
    text = open(path, "w", encoding="utf-8")  # запись
    text.write(data)
    text.close()


def saving_text(dict: dict, path: str, header: str) -> None:
    with open(path, "w", encoding="utf-16") as file:
        file.write(f"{header}\n")
        for key, value in dict.items():
            file.write(f"{key} ~ {value}\n")

