"""Fetch URLs, extract their contents, and write parsed data to file."""
from aiofiles.threadpool.text import AsyncTextIOWrapper as AsyncIOFile
from aiohttp import ClientError, ClientSession, InvalidURL
from logger import LOGGER

from .parser import parse_html_page_metadata


async def fetch_url_and_save_data(
    session: ClientSession,
    url: str,
    outfile: AsyncIOFile,
    total_count: int,
    i: int,
):
    """
    Fetch raw HTML from a URL prior to parsing.

    :param ClientSession session: Async HTTP requests session.
    :param str url: Target URL to be fetched.
    :param AsyncIOFile outfile: Path of local file to write to.
    :param int total_count: Total number of URLs to be fetched.
    :param int i: Current iteration of URL out of total URLs.
    """
    try:
        async with session.get(url) as resp:
            if resp.status != 200:
                pass
            html = await resp.text()
            page_metadata = await parse_html_page_metadata(html, url)
            await outfile.write(f"{page_metadata}\n")
            LOGGER.info(f"Fetched URL {i} of {total_count}: {page_metadata}")
    except InvalidURL as e:
        LOGGER.error(f"Unable to fetch invalid URL `{url}`: {e}")
    except ClientError as e:
        LOGGER.error(f"ClientError while fetching URL `{url}`: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while fetching URL `{url}`: {e}")
