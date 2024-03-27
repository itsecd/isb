import os
import logging

from sys import argv
from constants import PATHS
from reader import json_reader
from writer import write_caesar
from writer import write_route

KEYWORD = argv[1]
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    paths = json_reader(PATHS)
    try:
        write_route(os.path.join(paths["folder"], paths["input"]), KEYWORD, 
                     os.path.join(paths["folder"], paths["output"]), os.path.join(paths["folder"], paths["key"]))
        logging.info("Programm successfully ended")
    except Exception as exc:
        logging.error(f"Programm error: {exc}")



