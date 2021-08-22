"""Event loop initialization."""
import asyncio
from typing import List

from aiohttp import ClientSession

from asyncio_tutorial.logger import LOGGER
from config import HTML_EXPORT_DIR, HTML_HEADERS

from .tasks import create_tasks


async def create_and_execute_tasks(urls: List[str]):
    """
    Open async HTTP session & execute created tasks.

    :param List[str] urls: URLs to fetch responses from.
    """
    async with ClientSession(headers=HTML_HEADERS) as session:
        tasks = await create_tasks(session, urls)
        await asyncio.gather(*tasks)
        LOGGER.success(
            f"Successfully saved {len(urls)} HTML pages to `{HTML_EXPORT_DIR}`"
        )
