from work_with_files import load_json_file, save_json_file
import os
from typing import Dict

def merge_key(json_path1: str, json_path2: str, output_json_path: str) -> None:
    """
    Merge keys from two JSON files and save the result to an output JSON file.

    :param json_path1: Path to the first JSON file.
    :param json_path2: Path to the second JSON file.
    :param output_json_path: Path to the output JSON file.
    """
    try:
        merged_dict: Dict[str, str] = {}

        dict1 = load_json_file(json_path1)
        dict2 = load_json_file(json_path2)

        keys1 = list(dict2.keys())
        keys2 = list(dict1.keys())

        for i in range(min(len(keys1), len(keys2))):
            merged_dict[keys1[i]] = keys2[i]

        save_json_file(output_json_path, merged_dict)

        os.remove(json_path2)

    except Exception as e:
        print(f"An error occurred: {e}")