import os
import logging

from sys import argv
from reader import json_reader
from writer import write_decrypted, write_frequency
from constants import PATHS, ALPHABET

logging.basicConfig(level=logging.INFO)
KEY = ALPHABET


if __name__ == "__main__":
    paths = json_reader(PATHS)
    try:
        write_frequency(os.path.join(paths["folder"], paths["input"]), os.path.join(paths["folder"], paths["frequency"]))

        write_decrypted(os.path.join(paths["folder"], paths["input"]), KEY, 
                     os.path.join(paths["folder"], paths["output"]), os.path.join(paths["folder"], paths["key"]))
        logging.info("Programm successfully ended")
    except Exception as exc:
        logging.error(f"Programm error: {exc}")