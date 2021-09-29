"""Script initialization."""
import asyncio

from aiohttp import ClientSession

from asyncio_tutorial.logger import LOGGER
from config import EXPORT_DIR, HTML_HEADERS
from data import urls

from .futures import register_future
from .loops import inspect_event_loop
from .tasks import create_tasks


async def aiohttp_aiofiles_tutorial():
    """Open async HTTP session & execute created tasks."""
    LOGGER.info(f"Asyncio tutorial Part II: HTTP Requests with Aiohttp & Aiofiles.")
    future = register_future()
    async with ClientSession(headers=HTML_HEADERS) as session:
        tasks = await create_tasks(session, urls, EXPORT_DIR)
        inspect_event_loop()
        await asyncio.gather(*tasks)
    future.set_result(f"Saved {len(urls)} files to `{EXPORT_DIR}`")
