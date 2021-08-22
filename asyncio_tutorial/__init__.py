"""Script entry point."""
from typing import List

from .loop import create_and_execute_tasks
from .reader import parse_urls


async def init_script(urls: List[str]):
    """
    Create an event loop to execute a function per argument.

    :param List[str] urls: URLs to fetch.
    """
    await create_and_execute_tasks(urls)
