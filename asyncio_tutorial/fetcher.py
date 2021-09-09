"""Fetch and save HTML pages asynchronously."""
from aiohttp import ClientError, ClientSession, InvalidURL

from asyncio_tutorial.logger import LOGGER
from asyncio_tutorial.writer import write_html_file


async def fetch_and_save_url(session, url: str, count: int, total_count: int):
    """
    Save HTML at target URL in local folder.

    :param ClientSession session: Async HTTP requests session.
    :param str url: Target URL to be fetched.
    :param int count: Current URL count.
    :param int total_count: Total URL count.
    """
    try:
        async with session.get(url) as resp:
            text = await resp.read()
            LOGGER.info(
                f"Response code {resp.status} for URL {count + 1} of {total_count}: {url}"
            )
            write_html_file(url, text)
    except InvalidURL as e:
        LOGGER.error(f"Unable to fetch invalid URL `{url}`: {e}")
    except ClientError as e:
        LOGGER.error(f"ClientError while fetching URL `{url}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while fetching URL `{url}`: {e}")
