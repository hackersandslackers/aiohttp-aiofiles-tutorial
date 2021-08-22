"""Fetch and save HTML pages asynchronously."""
import aiofiles
from aiohttp import ClientError, ClientSession, InvalidURL

from asyncio_tutorial.logger import LOGGER
from config import HTML_EXPORT_DIR


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
