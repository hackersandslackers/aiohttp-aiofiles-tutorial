"""Script event loop initialization."""
import asyncio
from typing import List

from .fetcher import run


def bulk_task_runner(urls: List[str]):
    """
    Create an event loop to execute a function per argument.

    :param List[str] urls: URLs to fetch.
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(urls))
    loop.close()
