"""Parse data from local files."""
from config import INPUT_FILEPATH

from .urls import parse_urls_from_csv

urls_to_fetch = parse_urls_from_csv(INPUT_FILEPATH)
