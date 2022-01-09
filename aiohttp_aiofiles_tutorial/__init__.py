"""Make hundreds of requests concurrently and save responses to disk."""
from asyncio import Task
from typing import Tuple, List, Optional

import asyncio
import time
from time import perf_counter as timer

import aiofiles
from aiofiles.threadpool.text import AsyncTextIOWrapper
from aiohttp import ClientSession
from config import FETCHED_URL_TITLES, HTML_HEADERS
from logger import LOGGER

from .data import urls
from .loops import inspect_event_loop
from .tasks import create_tasks


async def init_script():
    """Initiate script by preparing an output file prior to executing tasks."""
    start_time = timer()
    async with aiofiles.open(FETCHED_URL_TITLES, mode="w+") as output_file:
        await output_file.write("title,url\n")
        done, pending = await create_and_execute_tasks(output_file)
        if len(pending) == 0:
            await output_file.close()

    LOGGER.success(f"Executed {__name__} in {time.perf_counter() - start_time:0.2f} seconds.")


async def create_and_execute_tasks(output_file: AsyncTextIOWrapper) -> Tuple[List[Optional[Task]], List[Optional[Task]]]:
    """
    Open async HTTP session & execute created tasks.

    :param AsyncTextIOWrapper output_file: Filepath to local .json file to write output to.

    :returns: Tuple[List[Optional[Task]], List[Optional[Task]]]
    """
    async with ClientSession(headers=HTML_HEADERS) as session:
        task_list = await create_tasks(session, urls, output_file)
        inspect_event_loop()
        done, pending = await asyncio.wait(task_list)
        return done, pending
