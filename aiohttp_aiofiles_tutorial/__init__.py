"""Make hundreds of requests concurrently and save responses to disk."""
import asyncio
import time
from time import perf_counter as timer

import aiofiles
from aiofiles.threadpool.text import AsyncTextIOWrapper as AsyncIOFile
from aiohttp import ClientSession
from config import EXPORT_FILE, HTML_HEADERS
from logger import LOGGER

from .data import urls
from .loops import inspect_event_loop
from .tasks import create_tasks


async def init_script():
    """Initiate script by preparing an output file prior to executing tasks."""
    start_time = timer()
    async with aiofiles.open(EXPORT_FILE, mode="w+") as outfile:
        await outfile.write("title,url,\n")
        await create_and_execute_tasks(outfile)
        await outfile.close()
    LOGGER.success(f"Executed {__name__} in {time.perf_counter() - start_time:0.2f} seconds.")


async def create_and_execute_tasks(outfile: AsyncIOFile):
    """
    Open async HTTP session & execute created tasks.

    :param AsyncIOFile outfile: Path of local file to write to.
    """
    async with ClientSession(headers=HTML_HEADERS) as session:
        task_list = await create_tasks(session, urls, outfile)
        inspect_event_loop()
        await asyncio.gather(*task_list)
