ERRORS = {
    "auto_input_conflict_with_key": "You cannot use --auto together with --input, --output or --key",
    "auto_input_conflict_without_key": "You cannot use --auto together with --input or --output",
    "auto_key_missing": "The --auto or --key parameters must be specified",
    "auto_input_missing": "The --auto or --input parameters must be specified",
    
    "alphabets_empty": "One or both alphabets are empty",
    "alphabet1_same_chars": "The alphabet1 (plaintext) contains the same characters",
    "alphabet2_shorter": "The length of the alphabet2 (ciphertext) is shorter than the length of the alphabet1 (plaintext)",
    "alphabet_empty": "The alphabet is empty",
    "alphabet_contains_same_chars": "The alphabet contains the same characters",
    "key_empty": "The key is empty",
    "key_invalid_char": "The key contains an invalid character: '{key_char}'",

    "invalid_file_path": "Invalid path to file: '{path}'",
    "file_not_json": "The file '{path}' is not a json file",
    "invalid_json": "Json file '{path}' is invalid: {e}",
    "invalid_lang_key": "The language key '{key}' is incorrect"
}


PROG_DESC = {
    "cipher": "The program encrypts the required text using substitution, Caesar and Vigenère ciphers.",
    "analysis": "Performs frequency analysis of the text and replaces ciphertext letters with similar real letters by frequency. Outputs the result necessary for further manual processing"
}


MESSAGES = {
    "write_to": "Writing to file {output_file}",
    "res_plain": "Result plain text:",
    "res_cipher": "Result cipher text:"
}


SUB_PROG_DESC = {
    "cipher": "Available ciphers (substitution, Caesar, Vigenère)",
    "sub": "Substitution cipher",
    "caesar": "Caesar cipher",
    "vig": "Vigenère cipher"
}


SUB_PROG_HELP = {
    "cipher": "Defines the cipher used",
    "sub": "Encrypts the text using a substitution cipher",
    "caesar": "Encrypts the text using a Caesar cipher",
    "vig": "Encrypts the text using a Vigenère cipher"
}


ARG_HELP = {
    "auto": "Using values from the settings.json file",
    "input": "Input text or path to text.txt",
    "output": "Output file for encrypted text",
    "uppercase": "Bring all input data to UPPER CASE",
    "alpha": "RU, EN or alphabetical string",
    "alpha_freq": "'ru' or 'en' letters frequency. Defaults to 'ru'",
    "key": "Key string or path to key.json",
    "shift": "A shift in Caesar's cipher (can be neg or pos)"
}
