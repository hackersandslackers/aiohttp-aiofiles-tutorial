"""Fetch URLs, extract their contents, and write output to file."""
from aiofiles.threadpool.text import AsyncTextIOWrapper
from aiohttp import ClientError, ClientSession, InvalidURL
from logger import LOGGER

from .writer import write_to_output_file


async def fetch_url_and_save_title(
    session: ClientSession, url: str, output_file: AsyncTextIOWrapper, total_count: int, i: int
):
    """
    Fetch raw HTML from a URL prior to extracting output.

    :param ClientSession session: Async HTTP requests session.
    :param str url: Target URL to be fetched.
    :param AsyncTextIOWrapper output_file: Filepath to local .json file to write output to.
    :param int total_count: Total number of URLs to be fetched.
    :param int i: Current iteration of URL out of total URLs.
    """
    try:
        async with session.get(url) as resp:
            html_body = await resp.text()
            await write_to_output_file(html_body, url, output_file, total_count, i)
    except InvalidURL as e:
        LOGGER.error(f"Unable to fetch invalid URL `{url}`: {e}")
    except ClientError as e:
        LOGGER.error(f"ClientError while fetching URL `{url}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while fetching URL `{url}`: {e}")
