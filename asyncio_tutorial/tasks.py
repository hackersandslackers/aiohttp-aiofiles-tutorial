"""Fetch and save HTML pages asynchronously."""
import asyncio
from asyncio import Task
from typing import List

from aiohttp import ClientSession

from .fetcher import fetch_and_save_url


async def create_and_execute_tasks(urls: List[str], headers: dict, directory: str):
    """
    Open async HTTP session & execute created tasks.

    :param List[str] urls: URLs to fetch responses from.
    :param dict headers: HTTP headers to send requests with.
    :param str directory: Target directory to save fetched data.
    """
    async with ClientSession(headers=headers) as session:
        tasks = await create_tasks(session, urls, directory)
        await asyncio.gather(*tasks)


async def create_tasks(
    session: ClientSession, urls: List[str], directory
) -> List[Task]:
    """
    Create asyncio tasks to be executed.

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
