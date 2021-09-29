from typing import List

import pytest

from data.parser import parse_urls


def test_parse_urls():

    urls = parse_urls()

    assert (type(urls)) == List[str]
