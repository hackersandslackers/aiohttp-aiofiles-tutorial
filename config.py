"""Script configuration."""
from os import path

# Base directory of project
BASE_DIR = path.abspath(path.dirname(__file__))

# Filepath to CSV containing URLs.
INPUT_FILEPATH = f"{BASE_DIR}/aiohttp_aiofiles_tutorial/data/urls.csv"

# Filepath of asynchronously generated CSV containing page data.
EXPORT_FILEPATH = f"{BASE_DIR}/export/hackers_pages_metadata.csv"

# Headers to be passed to async HTTP client session.
HTTP_HEADERS = {
    "content-type": "text/html; charset=UTF-8",
    "connection": "keep-alive",
    "accept": "*/*",
}
