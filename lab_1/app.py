from flask import Flask, render_template, request, redirect

from src.ciphers import substitution, caesar, vigenere


app = Flask(__name__)


def cipher_handle(args: dict) -> str:
    """Function for processing arguments passed through a web application.

    Args:
        args (dict): argument dict.

    Returns:
        str: Encryption Result.
    """
    cipher_text = ""

    to_upper = (0, 1)[args.get("to-upper") == "on"]
    message = args.get("plain-text")

    match args.get("cipher-select"):
        case "sub":
            alphabet1 = args.get("alphabet1")
            alphabet2 = args.get("alphabet2")

            cipher_text = substitution(alphabet1, alphabet2, message, to_upper)

        case "caesar":
            alphabet = args.get("alphabet")
            shift = int(args.get("shift"))

            cipher_text = caesar(alphabet, message, shift, to_upper)

        case "vig":
            alphabet = args.get("alphabet")
            key = args.get("key")

            cipher_text = vigenere(alphabet, key, message, to_upper)

    return cipher_text


@app.route("/")
def home():
    """Homepage."""
    return redirect("/cipher")


@app.route("/cipher", methods=["GET", "POST"])
def cipher():
    """Encryption page."""
    if request.method == "GET":
        return render_template("index.html")

    try:
        cipher_text = cipher_handle(request.form.to_dict())
        return render_template(
            "index.html",
            cipher_text=cipher_text,
            hidden="hidden",
            error=""
        )
    except Exception as e:
        return render_template("index.html", error_text=e, hidden="")


@app.route("/<cipher>_inputs.html")
def inputs(cipher):
    """HTML templates for forms."""
    if cipher in ("caesar", "sub", "vig"):
        return render_template(f"{cipher}_inputs.html")

    return ""


if __name__ == "__main__":
    app.run()
