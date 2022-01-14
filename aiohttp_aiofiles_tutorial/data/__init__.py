"""Parse data from local files."""
from config import CSV_FILEPATH

from .urls import parse_urls_from_csv

urls_to_fetch = parse_urls_from_csv(CSV_FILEPATH)
