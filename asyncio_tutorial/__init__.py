"""Event loop initialization."""
import asyncio
from asyncio import Task
from typing import List

from aiohttp import ClientSession

from asyncio_tutorial.logger import LOGGER
from asyncio_tutorial.tasks import create_tasks
from config import HTML_EXPORT_DIR, HTML_HEADERS
from data import parse_urls

from .logger import LOGGER
from .tasks import create_and_execute_tasks


async def init_script():
    """Open async HTTP session & execute created tasks."""
    urls = parse_urls()
    async with ClientSession(headers=HTML_HEADERS) as session:
        tasks = await create_tasks(session, urls, HTML_EXPORT_DIR)
        inspect_loop(tasks)
        await asyncio.gather(*tasks)
        LOGGER.success(
            f"Successfully saved {len(urls)} HTML pages to `{HTML_EXPORT_DIR}`"
        )
        inspect_loop(tasks)


def inspect_loop(tasks: List[Task]):
    """Get async loop info."""
    loop = tasks[0].get_loop()
    LOGGER.info(f"Loop info: {loop}")
