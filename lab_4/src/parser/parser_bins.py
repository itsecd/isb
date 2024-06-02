import re
import csv
import json
import requests

from bs4 import BeautifulSoup


def write_html(
    path_output_file: str = "bins.html",
    url: str = "https://www.freebinchecker.com/sberbank-of-russia-credit-issuer-bin-list-type?hl=ru",
) -> None:
    """
    Writes the HTML content of a webpage to a file.

    Args:
        - path_output_file (str): Path to the output HTML file.
        Defaults to "bins.html".
        - url (str): URL of the webpage to fetch HTML content from.
        Defaults to "https://www.freebinchecker.com/sberbank-of-russia-credit-issuer-bin-list-type?hl=ru".
    """
    response = requests.get(url)

    with open(path_output_file, "w") as f:
        f.write(response.text)


def get_csv_freebinchecker(
    path_input_file: str = "bins.html", path_output_file: str = "output.csv"
) -> None:
    """
    Extracts BIN data from HTML and writes it to a CSV file.

    Args:
        - path_input_file (str): Path to the input HTML file.
        Defaults to "bins.html".
        - path_output_file (str): Path to the output CSV file.
        Defaults to "output.csv".
    """

    with open(path_input_file, "r") as f:
        text = f.read()

    soup = BeautifulSoup(text, "html.parser")
    table = soup.find("table", {"class": "table table-striped text-left"})
    tbody = table.find("tbody")

    with open("output.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["bin", "scheme", "type"])

        for row in tbody.find_all("tr"):
            lines = re.split("\n", row.text, maxsplit=5)
            lines = lines[1:4]
            writer.writerow(lines)


def get_json_from_csv_freebinchecker(
    path_input_file_csv: str = "output.csv",
    path_output_file_csv: str = "output.json",
) -> None:
    """
    Converts relevant BIN data from CSV to JSON format.

    Args:
        - path_input_file_csv (str): Path to the input CSV file.
        Defaults to "output.csv".
        - path_output_file_json (str): Path to the output JSON file.
        Defaults to "output.json".
    """

    with open(path_input_file_csv, "r") as f:

        reader = csv.reader(f)
        bins = {"bins": []}

        for row in reader:

            if row[1] == "MASTERCARD" and row[2] == "credit":
                bins["bins"].append(row[0])

    with open(path_output_file_csv, "w") as f:
        json.dump(bins, f, indent=4, sort_keys=True)
