"""Prepare tasks to be executed."""
import asyncio
from asyncio import Task
from typing import List

from aiohttp import ClientSession

from .fetcher import fetch_and_save_url


async def create_tasks(
    session: ClientSession, urls: List[str], directory
) -> List[Task]:
    """
    Create asyncio tasks to be execute the `fetch_and_save_url` coroutinne.

    :param ClientSession session: Async HTTP requests session.
    :param List[str] urls: Resource URLs to fetch.
    :param str directory: Target directory to save fetched data.

    :returns: List[Task]
    """
    tasks = []
    for i, url in enumerate(urls):
        task = asyncio.create_task(
            fetch_and_save_url(session, url, directory, i, len(urls))
        )
        tasks.append(task)
    return tasks
