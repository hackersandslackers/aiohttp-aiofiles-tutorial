"""Test reading tutorial sample data URLs."""
from config import CSV_FILEPATH

from aiohttp_aiofiles_tutorial.data.urls import parse_urls_from_csv


def test_parse_urls():
    """Ensure URL sample data is parsed correctly."""

    urls_to_fetch = parse_urls_from_csv(CSV_FILEPATH)

    assert (type(urls_to_fetch)) == list
    assert "https://" in urls_to_fetch[0]
