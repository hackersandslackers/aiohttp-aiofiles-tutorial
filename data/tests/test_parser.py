import pytest
from typing import List

from data.parser import urls


def test_parse_urls():

    
    assert(type(urls)) == List[str]