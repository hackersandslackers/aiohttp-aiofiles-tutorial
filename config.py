"""Script configuration."""
from os import path

# Set base directory of project
BASE_DIR = path.abspath(path.dirname(__file__))

# Directory in which HTML export will be saved
HTML_EXPORT_DIR = f"{BASE_DIR}/export/"

HTML_HEADERS = {
    "content-type": "text/html; charset=UTF-8",
    "connection": "keep-alive",
    "accept": "*/*",
}
