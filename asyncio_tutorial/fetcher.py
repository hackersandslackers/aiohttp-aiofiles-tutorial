"""Fetch and save pages asynchronously."""
import asyncio
from typing import List

import aiofiles
from aiohttp import ClientError, ClientSession, InvalidURL

from config import HTML_EXPORT_DIR
from log import LOGGER


async def run(urls: List[str]):
    """
    Create async HTTP session to execute tasks.

    :param List[str] urls: URLs to fetch responses from.
    """
    headers = {
        "content-type": "text/html; charset=UTF-8",
        "connection": "keep-alive",
        "accept": "*/*",
    }
    async with ClientSession(headers=headers) as session:
        await queue_and_execute_tasks(session, urls)


async def queue_and_execute_tasks(session: ClientSession, urls: List[str]):
    """
    Create tasks to and execute them asynchronously.

    :param ClientSession session: Async HTTP requests session.
    :param List[str] urls: Resource URLs to fetch.
    """
    tasks = []
    for i, url in enumerate(urls):
        task = asyncio.create_task(fetch_url(session, url, i, len(urls)))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    return result


async def fetch_url(session, url: str, count: int, total_count: int):
    """
    Save URL's HTML as page in local folder.

    :param ClientSession session: Async HTTP requests session.
    :param str url: Single resource to fetch.
    :param int count: Current URL count.
    :param int total_count: Total URL count.
    """
    try:
        async with session.get(url) as response:
            if response.status == 200:
                text = await response.read()
                filename = f"{HTML_EXPORT_DIR}/{url.split('/')[-2]}.html"
                async with aiofiles.open(filename, mode="wb+") as f:
                    await f.write(text)
                    await f.close()
                    LOGGER.info(f"Fetching {count} of {total_count}: {url}")
    except InvalidURL as e:
        LOGGER.error(f"Unable to fetch invalid URL `{url}`: {e}")
    except ClientError as e:
        LOGGER.error(f"ClientError while fetching URL `{url}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while fetching URL `{url}`: {e}")
