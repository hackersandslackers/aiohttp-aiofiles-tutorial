"""Script initialization."""
import asyncio

from aiohttp import ClientSession

from asyncio_tutorial.logger import LOGGER
from config import EXPORT_DIR, HTML_HEADERS
from data import parse_urls

from .tasks import create_tasks


async def aiohttp_aiofiles_tutorial():
    """Open async HTTP session & execute created tasks."""
    LOGGER.info(f"Asyncio tutorial Part II: HTTP Requests with Aiohttp & Aiofiles.")
    urls = parse_urls()
    async with ClientSession(headers=HTML_HEADERS) as session:
        tasks = await create_tasks(session, urls, EXPORT_DIR)
        await asyncio.gather(*tasks)
        LOGGER.success(f"Saved {len(urls)} files to `{EXPORT_DIR}`")


async def inspect_loop():
    """
    Get event loop info.

    :param: List[Task] tasks

    :return: str
    """
    loop = asyncio.get_event_loop()
    LOGGER.info(f"Loop finished in {loop.time()} seconds.")

