"""Event loop initialization."""
import asyncio
from typing import List

from aiohttp import ClientSession

from asyncio_tutorial.logger import LOGGER
from asyncio_tutorial.tasks import create_tasks

from data import URLS
from config import HTML_EXPORT_DIR, HTML_HEADERS


async def init_script():
    """Open async HTTP session & execute created tasks."""
    async with ClientSession(headers=HTML_HEADERS) as session:
        tasks = await create_tasks(session, URLS)
        await asyncio.gather(*tasks)
        LOGGER.success(
            f"Successfully saved {len(URLS)} HTML pages to `{HTML_EXPORT_DIR}`"
        )
