"""Parse list of URLs from a local CSV (for demonstration)."""
import csv
from typing import List

from config import BASE_DIR


def parse_urls() -> List[str]:
    """
    Parse URLs from CSV file into a Python list.

    :returns: List[str]
    """
    urls = []
    with open(f"{BASE_DIR}/urls.csv", newline="") as f:
        reader = csv.reader(f)
        for line in reader:
            urls.append(line[0])

    return urls
