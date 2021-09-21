"""Script entry point."""
from typing import List

from config import HTML_EXPORT_DIR, HTML_HEADERS

from .logger import LOGGER
from .reader import parse_urls
from .tasks import create_and_execute_tasks


async def init_script(urls: List[str]):
    """
    Create an event loop to execute a function per argument.

    :param List[str] urls: URLs to fetch.
    """
    fetcher_tasks = await create_and_execute_tasks(urls, HTML_HEADERS, HTML_EXPORT_DIR)
    LOGGER.success(
        f"Successfully saved {fetcher_tasks} HTML pages to `{HTML_EXPORT_DIR}`"
    )
