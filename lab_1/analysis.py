from src.letter_frequency import calculate_frequency, replace_by_freq
from src.utils import read_settings, get_frequency, write_to_file
from src.parsing import parse_analysis_arguments, parse_input_param
from config.messages import MESSAGES


def analysis():
    """Program function for frequency analysis"""
    args = parse_analysis_arguments()

    if args.auto:
        task2_settings = read_settings().get("task2", {})
        cipher_text = parse_input_param(task2_settings.get("cipher_text", ""))
        output_file = task2_settings.get("plain_text", "")
    else:
        cipher_text = parse_input_param(args.input)
        output_file = args.output

    real_freq = get_frequency(args.alpha_freq)

    cip_freq = calculate_frequency(cipher_text)

    plain_text = replace_by_freq(cipher_text, cip_freq, real_freq)

    print(MESSAGES["res_plain"])
    print(plain_text)

    if output_file:
        write_to_file(output_file, plain_text)
        print(MESSAGES["write_to"].format(output_file=output_file))


def main():
    """Program Entry Point."""
    try:
        analysis()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
