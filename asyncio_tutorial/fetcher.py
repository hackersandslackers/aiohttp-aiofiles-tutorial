"""Fetch and save HTML pages asynchronously."""
import asyncio
from asyncio import Task
from typing import List

import aiofiles
from aiohttp import ClientError, ClientSession, InvalidURL

from config import HTML_EXPORT_DIR, HTML_HEADERS
from log import LOGGER


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


async def create_tasks(session: ClientSession, urls: List[str]) -> List[Task]:
    """
    Create asyncio tasks to be executed.

    :param ClientSession session: Async HTTP requests session.
    :param List[str] urls: Resource URLs to fetch.

    :returns: List[Task]
    """
    tasks = []
    for i, url in enumerate(urls):
        task = asyncio.create_task(fetch_and_save_url(session, url, i, len(urls)))
        tasks.append(task)
    return tasks


async def fetch_and_save_url(session, url: str, count: int, total_count: int):
    """
    Save URL's HTML as page in local folder.

    :param ClientSession session: Async HTTP requests session.
    :param str url: Single resource to fetch.
    :param int count: Current URL count.
    :param int total_count: Total URL count.
    """
    try:
        async with session.get(url) as resp:
            text = await resp.read()
            LOGGER.info(
                f"Response code {resp.status} for URL {count + 1} of {total_count}: {url}"
            )
            filename = f"{HTML_EXPORT_DIR}/{url.split('/')[-2]}.html"
            async with aiofiles.open(filename, mode="wb+") as f:
                await f.write(text)
                await f.close()
    except InvalidURL as e:
        LOGGER.error(f"Unable to fetch invalid URL `{url}`: {e}")
    except ClientError as e:
        LOGGER.error(f"ClientError while fetching URL `{url}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while fetching URL `{url}`: {e}")
