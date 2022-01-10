"""Test reading tutorial sample data URLs."""
from aiohttp_aiofiles_tutorial.data.parser import parse_urls_from_csv
from config import CSV_FILEPATH


def test_parse_urls():
    """Ensure URL sample data is parsed correctly."""

    urls = parse_urls_from_csv(CSV_FILEPATH)

    assert (type(urls)) == list
    assert "https://" in urls[0]
