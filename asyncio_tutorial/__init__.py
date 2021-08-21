"""Script event loop initialization."""
import asyncio
from typing import List

from .fetcher import create_and_execute_tasks


def bulk_task_runner(urls: List[str]):
    """
    Create an event loop to execute a function per argument.

    :param List[str] urls: URLs to fetch.
    """
    asyncio.run(create_and_execute_tasks(urls))
