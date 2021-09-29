"""Parse data from local files."""
from config import CSV_FILEPATH

from .parser import parse_urls

urls = parse_urls(CSV_FILEPATH)
