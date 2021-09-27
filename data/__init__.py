"""Parse data from local files."""
from .parser import parse_urls
from config import CSV_FILEPATH


urls = parse_urls(CSV_FILEPATH)