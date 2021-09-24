"""Script initialization."""
import asyncio
from asyncio import SelectorEventLoop, Task
from typing import List

from aiohttp import ClientSession

from asyncio_tutorial.logger import LOGGER
from asyncio_tutorial.tasks import create_tasks
from config import HTML_EXPORT_DIR, HTML_HEADERS
from data import parse_urls

from .logger import LOGGER


async def init_script():
    """Open async HTTP session & execute created tasks."""
    urls = parse_urls()
    async with ClientSession(headers=HTML_HEADERS) as session:
        tasks = await create_tasks(session, urls, HTML_EXPORT_DIR)
        await asyncio.gather(*tasks)
        loop = inspect_loop(tasks)
        LOGGER.success(
            f"Saved {len(urls)} HTML pages to `{HTML_EXPORT_DIR}`. Loop: {loop}"
        )


def inspect_loop(tasks: List[Task]) -> SelectorEventLoop:
    """
    Get async loop info.

    :param: List[Task] tasks

    :return: SelectorEventLoop
    """
    loop = tasks[0].get_loop()
    LOGGER.info(f"Loop info: {loop}")
    return loop
