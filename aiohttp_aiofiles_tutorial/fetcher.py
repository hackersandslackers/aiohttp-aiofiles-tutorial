"""Fetch URLs, extract their contents, and write parsed data to file."""
from aiofiles.threadpool.text import AsyncTextIOWrapper
from aiohttp import ClientError, ClientSession, InvalidURL
from logger import LOGGER

from .writer import write_to_outfile


async def fetch_url_and_save_title(
    session: ClientSession, url: str, outfile: AsyncTextIOWrapper, total_count: int, i: int
):
    """
    Fetch raw HTML from a URL prior to parsing.

    :param ClientSession session: Async HTTP requests session.
    :param str url: Target URL to be fetched.
    :param AsyncTextIOWrapper outfile: Filepath of local .csv file to write to.
    :param int total_count: Total number of URLs to be fetched.
    :param int i: Current iteration of URL out of total URLs.
    """
    try:
        async with session.get(url) as resp:
            html = await resp.text()
            await write_to_outfile(html, url, outfile, total_count, i)
    except InvalidURL as e:
        LOGGER.error(f"Unable to fetch invalid URL `{url}`: {e}")
    except ClientError as e:
        LOGGER.error(f"ClientError while fetching URL `{url}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while fetching URL `{url}`: {e}")
