import os
import logging
import tabulate
import argparse

from typing import Set

from src import ser
from src import receiving_data
from src.correct_card.moon_algorithm import correct_card_moon
from src.draw import measure_execution_time, plot_graphs_from_dict
from src.anti_hash_sberbank_mastercard.anti_hash import get_cards_according_template

from src.consts import (
    DEFAULT_SEPARATORS,
    DEFAULT_COUNT_DIGITS_INTO_CARD,
    DEFAULT_COUNT_DIGITS_INTO_BIN_SBERBANK_MASTERCARD,
    DEFAULT_PREFIX_TEMPLATES_FOUR_DIGIT_SBERBANK_MASTERCARD_CREDIT,
)


def generate_args() -> argparse.ArgumentParser:
    """
    Generate the command-line arguments parser.

    Returns:
        - argparse.ArgumentParser: The configured argument parser.
    """

    parser = argparse.ArgumentParser(description="...")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-un",
        "--unhash_card",
        action="store_true",
        help="Specify this option to unhash a card.",
    )

    group.add_argument(
        "-cor",
        "--correct_card",
        action="store_true",
        help="Specify this option to correct a card.",
    )

    group.add_argument(
        "-gen",
        "--gen_default_file_bins",
        action="store_true",
        help="Specify this option to generate default file bins",
    )

    group.add_argument(
        "-dr",
        "--draw_diagrams",
        action="store_true",
        help="Specify this option to draw diagrams.",
    )

    # Input/output information
    parser.add_argument(
        "-i",
        "--value_input",
        type=str,
        default=None,
        help=f"Specify the input value.",
    )

    parser.add_argument(
        "-x",
        "--file_input",
        type=str,
        default=None,
        help=f"ЗPath file input program",
    )

    parser.add_argument(
        "-o",
        "--path_object_output",
        type=str,
        default=os.path.join("output.json"),
        help=f"Path to save output " f'default:({os.path.join("output.json")})',
    )

    # logs
    parser.add_argument(
        "-sl",
        "--save_logs",
        type=str,
        default=None,
        help=f"Path to the file save logs default(None).",
    )

    parser.add_argument(
        "-lp",
        "--logs_pretty",
        type=bool,
        default=False,
        help=f"Path to the file save pretty logs " f"default(False).",
    )

    # For correct_cards mode
    parser.add_argument(
        "-sep",
        "--separators",
        type=Set[str],
        default=DEFAULT_SEPARATORS,
        help=f"Specify the separators for correct_cards mode",
    )

    # For unhash_card mode
    parser.add_argument(
        "-b",
        "--bins_file_lines",
        type=str,
        default=None,
        help=f"Specify the file containing bins file lines.",
    )

    parser.add_argument(
        "-ld",
        "--last_digits",
        type=str,
        default=None,
        help=f"Specify the last digits of the card number",
    )

    parser.add_argument(
        "-cdc",
        "--count_digits_in_card",
        type=int,
        default=DEFAULT_COUNT_DIGITS_INTO_CARD,
        help=f"Specify the count of digits in each card number.",
    )

    parser.add_argument(
        "-mp",
        "--max_processing_using_for_unhash",
        type=int,
        default=None,
        help=f"Specify the maximum number of cores to use.",
    )

    parser.add_argument(
        "-cnf",
        "--name_conf_in_output",
        type=str,
        default=None,
        help=f"Specify the name of the configuration in the output.",
    )

    return parser


def main():
    """
    Main function to execute the program.
    """

    try:

        parser = generate_args()
        args = parser.parse_args()

        if args.save_logs:
            logging.basicConfig(
                filename=args.save_logs,
                filemode="w",
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(name)s:%(lineno)d"
                " - %(message)s",
            )
            logger = logging.getLogger(__name__)

        match args:
            case args if args.correct_card:

                if args.value_input:

                    print(correct_card_moon(args.value_input, args.separators))

                if args.file_input:

                    cards = ser.read_file_lines(args.file_input)

                    correct_cards = receiving_data.get_correct_cards(cards, args.separators)

                    ser.write_json(args.path_object_output, correct_cards)

            case args if args.unhash_card:

                bins = ser.read_file_lines(args.bins_file_lines)

                if args.value_input:

                    print(
                        get_cards_according_template(
                            bins,
                            args.last_digits,
                            args.count_digits_in_card,
                            args.value_input,
                            args.max_processing_using_for_unhash,
                        )
                    )

                if args.file_input:

                    hash_values = ser.read_file_lines(args.file_input)

                    rehash = receiving_data.get_rehash(
                        hash_values,
                        bins,
                        args.last_digits,
                        args.count_digits_in_card,
                        args.max_processing_using_for_unhash,
                        args.name_conf_in_output,
                    )

                    ser.write_json(args.path_object_output, rehash)

            case args if args.gen_default_file_bins:

                bins = receiving_data.generate_bins(
                    DEFAULT_PREFIX_TEMPLATES_FOUR_DIGIT_SBERBANK_MASTERCARD_CREDIT,
                    DEFAULT_COUNT_DIGITS_INTO_BIN_SBERBANK_MASTERCARD,
                )

                ser.write_file_lines(args.path_object_output, bins)

            case args if args.draw_diagrams:
            
                bins = ser.read_file_lines(args.bins_file_lines)
                hash_values = ser.read_file_lines(args.file_input)
    
                times_dict = measure_execution_time(
                    hash_values,
                    bins,
                    args.last_digits,
                    args.count_digits_in_card,
                    args.max_processing_using_for_unhash,
                )
    
                plot_graphs_from_dict(times_dict, args.path_object_output)

    except Exception as e:

        if args.save_logs:
            logger.error(f"ERROR: {e}")
        else:
            raise RuntimeError(f"ERROR: {e}")

    finally:

        if args.save_logs and args.logs_pretty:
            with open(args.save_logs, "r") as f:
                logs = f.readlines()

            table = tabulate.tabulate(
                [log.split(" - ") for log in logs],
                headers=["Time", "Level", "File", "Message"],
                tablefmt="fancy_grid",
            )

            with open(args.save_logs, "w") as f:
                f.write(table)


if __name__ == "__main__":

    try:

        main()

    except Exception as e:

        print(e)
