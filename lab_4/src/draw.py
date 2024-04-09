import time
import logging

from tqdm import tqdm
from typing import Set

import matplotlib.pyplot as plt

from .receiving_data import get_rehash
from .consts import GREEN, RESET

logger = logging.getLogger(__name__)


def measure_execution_time(
    hash_values: Set[str],
    bins: Set[set],
    last_digits: str,
    count_digits_into_card: int,
    count_processing: int,
) -> dict:

    try:

        logger.info(f"Start process get times")

        results = {}

        with tqdm(
            total=count_processing,
            desc=f"{GREEN}View time:{RESET}",
            bar_format=f"{{l_bar}}{GREEN}{{bar}}{RESET}{{r_bar}}",
        ) as pbar:

            for count_process in range(1, count_processing + 1):

                start_time = time.time()
                get_rehash(
                    hash_values,
                    bins,
                    last_digits,
                    count_digits_into_card,
                    count_process,
                )
                end_time = time.time()

                execution_time = end_time - start_time
                results[count_process] = execution_time

                pbar.update(1)

        logger.info(f"Process get times successfull.")
        return results

    except Exception as e:

        raise ValueError(f"Measure execution time by count processing error, {e}")


def plot_graphs_from_dict(data_dict: dict, output_file: str):

    try:
        keys = list(data_dict.keys())
        values = list(data_dict.values())

        plt.xlabel("Processing")
        plt.ylabel("Time")
        plt.figure(figsize=(15, 5))

        plt.subplot(1, 3, 1)
        plt.plot(keys, values, marker="o", color="b")
        plt.title("Linear")

        plt.subplot(1, 3, 2)
        plt.bar(keys, values, color="g")
        plt.title("Diagram")

        plt.subplot(1, 3, 3)
        plt.pie(values, labels=keys, autopct="%1.1f%%", startangle=140)
        plt.title("Pie")

        plt.tight_layout()

        plt.savefig(output_file)
        plt.close()

        logger.info(f"Generate and write[{output_file}] draws successfull.")

    except Exception as e:

        raise ValueError(f"Generate and write[{output_file}] draws error, {e}")
