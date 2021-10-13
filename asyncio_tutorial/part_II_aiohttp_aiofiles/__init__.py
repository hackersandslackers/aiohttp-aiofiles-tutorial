"""Make hundreds of requests concurrently and save responses to disk."""
import asyncio
import time

from aiohttp import ClientSession

from asyncio_tutorial.logger import LOGGER
from config import EXPORT_DIR, HTML_HEADERS
from data import urls

from .futures import register_future
from .loops import inspect_event_loop
from .tasks import create_tasks


async def aiohttp_aiofiles_tutorial(start_time: float):
    """
    Open async HTTP session & execute created tasks.

    :param float start_time: Counter representing the time the script was initialized.
    """
    LOGGER.info(f"Asyncio tutorial Part II: HTTP Requests with Aiohttp & Aiofiles.")
    future = register_future()
    async with ClientSession(headers=HTML_HEADERS) as session:
        tasks = await create_tasks(session, urls, EXPORT_DIR)
        inspect_event_loop()
        await asyncio.gather(*tasks)
    future.set_result(
        f"Executed {__name__} in {time.perf_counter() - start_time:0.2f} seconds."
    )
