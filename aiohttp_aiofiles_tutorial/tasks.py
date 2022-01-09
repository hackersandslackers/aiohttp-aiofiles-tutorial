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
    task_list = []
    for i, url in enumerate(urls):
        task = asyncio.create_task(fetch_url_and_save_title(session, url, output_file, len(urls), i))
        task_list.append(task)
    return task_list