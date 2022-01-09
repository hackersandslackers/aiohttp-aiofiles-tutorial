"""Parse data from local files."""
from config import CSV_FILEPATH

from .parser import parse_urls_from_csv

urls = parse_urls_from_csv(CSV_FILEPATH)
