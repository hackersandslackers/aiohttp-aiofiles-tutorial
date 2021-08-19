import csv
from typing import List

from config import BASE_DIR


def get_list_of_urls() -> List[str]:
    """
    Read list of URLs from CSV file.

    :returns: List[str]
    """
    urls = []
    with open(f"{BASE_DIR}/asyncio_tutorial/urls.csv", newline="") as f:
        reader = csv.reader(f)
        for line in reader:
            urls.append(line[0])

    return urls
