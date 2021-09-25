"""Fetch and save files to disk asynchronously."""
from aiohttp import ClientError, ClientSession, InvalidURL

from asyncio_tutorial.logger import LOGGER
from asyncio_tutorial.writer import write_file


async def fetch_and_save_url(
    session: ClientSession, url: str, directory: str, i: int, total_count: int
):
    """
    Save HTML at target URL in local folder.

    :param ClientSession session: Async HTTP requests session.
    :param str url: Single resource to fetch.
    :param str directory: Target directory to save fetched data.
    :param str url: Target URL to be fetched.
    :param int i: Current URL count.
    :param int total_count: Total URL count.
    """
    try:
        async with session.get(url) as resp:
            body = await resp.read()
            filetype = (
                resp.headers.get("Content-Type")
                .replace("; charset=UTF-8", "")
                .replace("text/", "")
            )
            LOGGER.info(f"Successfully fetched URL {i + 1} of {total_count}: {url}")
            await write_file(url, body, filetype, directory)
    except InvalidURL as e:
        LOGGER.error(f"Unable to fetch invalid URL `{url}`: {e}")
    except ClientError as e:
        LOGGER.error(f"ClientError while fetching URL `{url}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while fetching URL `{url}`: {e}")
