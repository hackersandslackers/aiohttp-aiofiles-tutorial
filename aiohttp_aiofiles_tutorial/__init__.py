"""Make hundreds of requests concurrently and save responses to disk."""
import asyncio
import time
from time import perf_counter as timer

import aiofiles
from aiofiles.threadpool.text import AsyncTextIOWrapper as AsyncIOFile
from aiohttp import ClientSession
from config import EXPORT_FILEPATH, HTTP_HEADERS
from logger import LOGGER

from .data import urls_to_fetch
from .tasks import create_tasks


async def init_script():
    """Prepare output file & kickoff task creation/execution."""
    start_time = timer()
    async with aiofiles.open(EXPORT_FILEPATH, mode="w+") as outfile:
        await outfile.write("title,description,primary_tag,url,published_at\n")
        await execute_fetcher_tasks(outfile)
        await outfile.close()
    LOGGER.success(
        f"Executed {__name__} in {time.perf_counter() - start_time:0.2f} seconds."
    )


async def execute_fetcher_tasks(outfile: AsyncIOFile):
    """
    Open async HTTP session & execute created tasks.

    :param AsyncIOFile outfile: Path of local file to write to.
    """
    async with ClientSession(headers=HTTP_HEADERS) as session:
        task_list = await create_tasks(session, urls_to_fetch, outfile)
        await asyncio.gather(*task_list)
