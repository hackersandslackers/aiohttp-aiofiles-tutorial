from typing import List

import pytest
from aiohttp_aiofiles_tutorial.data.parser import parse_urls_from_csv
from config import CSV_FILEPATH


def test_parse_urls():

    urls = parse_urls_from_csv(CSV_FILEPATH)

    assert (type(urls)) == list
