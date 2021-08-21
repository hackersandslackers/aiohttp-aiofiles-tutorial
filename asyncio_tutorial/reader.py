"""Parse list of URLs from a local CSV."""
import csv
from typing import List

from config import CSV_FILEPATH


def parse_urls() -> List[str]:
    """
    Parse URLs from CSV file into a Python list.

    :returns: List[str]
    """
    urls = []
    with open(CSV_FILEPATH, newline="") as f:
        reader = csv.reader(f)
        for line in reader:
            urls.append(line[0])

    return urls
