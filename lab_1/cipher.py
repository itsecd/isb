import src.ciphers as ciphers

from src.utils import write_to_file, read_settings
from src.parsing import parse_cipher_arguments, parse_input_param, \
    parse_alpha_param, parse_key_param
from config.messages import MESSAGES


def cipher():
    """Function for the encryption program."""
    args = parse_cipher_arguments()

    if args.auto:
        task1_settings = read_settings().get("task1", {})
        plain_text = parse_input_param(task1_settings.get("plain_text", ""))
        output_file = task1_settings.get("cipher_text", "")
    else:
        plain_text = parse_input_param(args.input)
        output_file = args.output

    match args.cipher:
        case "sub":
            alpha1 = parse_alpha_param(args.alpha1)
            alpha2 = parse_alpha_param(args.alpha2)
            cipher_text = ciphers.substitution(
                alpha1,
                alpha2,
                plain_text,
                args.to_upper
            )
        case "caesar":
            alpha = parse_alpha_param(args.alpha)
            cipher_text = ciphers.caesar(
                alpha,
                plain_text,
                args.shift,
                args.to_upper
            )
        case "vig":
            alpha = parse_alpha_param(args.alpha)
            key = parse_key_param(task1_settings.get("key", "") \
                                  if args.auto else args.key)

            cipher_text = ciphers.vigenere(
                alpha,
                key,
                plain_text,
                args.to_upper
            )

    print(MESSAGES["res_cipher"])
    print(cipher_text)

    if output_file:
        write_to_file(output_file, cipher_text)
        print(MESSAGES["write_to"].format(output_file=output_file))


def main():
    """Program Entry Point."""
    try:
        cipher()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
