"""Prepare tasks to be executed."""
import asyncio
from asyncio import Task
from typing import List

from aiofiles.threadpool.text import AsyncTextIOWrapper
from aiohttp import ClientSession

from .fetcher import fetch_url_and_save_title


async def create_tasks(session: ClientSession, urls: List[str], output_file: AsyncTextIOWrapper) -> List[Task]:
    """
    Create asyncio tasks to execute the `fetch_url_and_save_title` coroutine.

    :param ClientSession session: Async HTTP requests session.
    :param List[str] urls: Resource URLs to fetch.
    :param AsyncTextIOWrapper output_file: Filepath to local .txt file to write output to.

    :returns: List[Task]
    """
    tasks = []
    i = 0
    for url in urls:
        task = asyncio.create_task(fetch_url_and_save_title(session, url, output_file, len(urls), i))
        tasks.append(task)
        i += 1
    return tasks
