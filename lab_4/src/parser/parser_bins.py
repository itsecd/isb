import re
import csv
import json
import requests

from bs4 import BeautifulSoup


def write_html(path_output_file: str = "bins.html", url: str = "https://www.freebinchecker.com/sberbank-of-russia-credit-issuer-bin-list-type?hl=ru") -> None:
    
    response = requests.get(url)
    
    with open(path_output_file, "w") as f:
        f.write(response.text)


def get_csv_freebinchecker(path_input_file: str = "bins.html", path_output_file: str = "output.csv") -> None:
    
    with open(path_input_file, "r") as f:
        text = f.read()

    soup = BeautifulSoup(text, "html.parser")
    table = soup.find("table", {"class": "table table-striped text-left"})
    tbody = table.find("tbody")

    with open("output.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['bin','scheme','type'])
        
        for row in tbody.find_all("tr"):
            lines = re.split("\n", row.text, maxsplit=5)
            lines = lines[1:4]
            writer.writerow(lines)


def get_json_from_csv_freebinchecker(path_input_file_csv: str = "output.csv", path_output_file_csv: str = "output.json") -> None:
    
    with open(path_input_file_csv, "r") as f:
    
        reader = csv.reader(f)
        bins = {"bins": []}
        
        for row in reader:
            
            if row[1] == "MASTERCARD" and row[2] == "credit":
                bins["bins"].append(row[0])

    with open(path_output_file_csv, "w") as f:
        json.dump(bins, f, indent=4, sort_keys=True)
