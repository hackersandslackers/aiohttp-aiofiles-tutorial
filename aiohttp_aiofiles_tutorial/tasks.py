"""Prepare tasks to be executed."""
import asyncio
from asyncio import Task
from typing import List

from aiofiles.threadpool.text import AsyncTextIOWrapper as AsyncIOFile
from aiohttp import ClientSession

from .fetcher import fetch_url_and_save_data


async def create_tasks(
    session: ClientSession, urls: List[str], outfile: AsyncIOFile
) -> List[Task]:
    """
    Create asyncio tasks to parse HTTP request responses.

    :param ClientSession session: Async HTTP requests session.
    :param List[str] urls: Resource URLs to fetch.
    :param AsyncIOFile outfile: Path of local file to write to.

    :returns: List[Task]
    """
    task_list = []
    for i, url in enumerate(urls):
        task = asyncio.create_task(
            fetch_url_and_save_data(session, url, outfile, len(urls), i)
        )
        task_list.append(task)
    return task_list
