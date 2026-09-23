import json
from pathlib import Path

def get_data(file_name: str) -> list:
    # 1. Construct the absolute path to your test_data folder
    # 2. Open the file and use json.load()
    # 3. Return the parsed list
    file_path = Path("testdata") / file_name
    with open(file_path, "r") as f:
        return json.load(f)