"""Parse a predetermined CSV of URLs into a Python list."""
import csv
from typing import List


def parse_urls(filepath: str) -> List[str]:
    """
    Parse a single-column CSV into a Python list of URLs.

    :returns: List[str]
    """
    urls = []
    with open(filepath, newline="") as f:
        reader = csv.reader(f)
        for line in reader:
            urls.append(line[0])

    return urls
