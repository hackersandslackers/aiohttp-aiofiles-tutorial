"""Script configuration."""
from os import path

# Base directory of project
BASE_DIR = path.abspath(path.dirname(__file__))

# Filepath to CSV containing URLs
CSV_FILEPATH = f"{BASE_DIR}/data/urls.csv"

# Directory in which HTML export will be saved
EXPORT_DIR = f"{BASE_DIR}/export/"

# Headers to be passed to async HTTP client session
HTML_HEADERS = {
    "content-type": "text/html; charset=UTF-8",
    "connection": "keep-alive",
    "accept": "*/*",
}

# Determine environment based on log folder
ENVIRONMENT = "development"
if path.isdir("/var/log/asyncio_tutorial"):
    ENVIRONMENT = "production"
