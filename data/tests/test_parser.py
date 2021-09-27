import pytest
from typing import List


def test_parse_urls():
    urls = parse_urls()
    
    assert(type(urls)) == List[str]