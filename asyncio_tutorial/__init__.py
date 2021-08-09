"""Bulk fetch content from HTTP endpoints."""
from typing import List

import asyncio
import aiofiles
from aiohttp import ClientError, ClientSession, InvalidURL

from log import LOGGER


def bulk_http_fetcher(urls: List[str]):
    """
    Bulk fetch content from a high volume of URLs asynchronously.

    :param List[str] urls: URLs to fetch.
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(urls))
    loop.close()
    LOGGER.success(f"Fetched {len(urls)} URLs.")


async def run(urls: List[str]):
    """
    Create async HTTP session to execute tasks.

    :param List[str] urls: URLs to fetch responses from.
    """
    headers = {
        "content-type": "application/json",
        "connection": "keep-alive",
        "accept": "*/*",
    }
    async with ClientSession(headers=headers) as session:
        await queue_and_execute_tasks(session, urls)


async def queue_and_execute_tasks(session: ClientSession, urls: List[str]):
    """
    Create tasks to be executed asynchronously.

    :param ClientSession session: Async HTTP requests session.
    :param List[str] urls: Resource URLs to fetch.
    """
    tasks = []
    for i, url in enumerate(urls):
        task = asyncio.create_task(
            fetch_url(session, url, i, len(urls))
        )
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    return result


async def fetch_url(session, url: str, count: int, total_count: int):
    """
    Fetch URL and create a dictionary representing the resource.

    :param ClientSession session: Async HTTP requests session.
    :param str url: Single resource to fetch.
    :param int count: Current URL count.
    :param int total_count: Total URL count.
    """
    try:
        async with session.get(url) as response:
            LOGGER.info(f"Fetching {count} of {total_count}: {url}")
            if response.status == 200:
                data = await response.read()
                async with aiofiles.open("data.json", mode="wb+") as f:
                    await f.write(data)
                    await f.close()
    except InvalidURL as e:
        LOGGER.error(f"Unable to fetch invalid URL `{url}`: {e}")
    except ClientError as e:
        LOGGER.error(f"Error while fetching URL `{url}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error: {e}")
