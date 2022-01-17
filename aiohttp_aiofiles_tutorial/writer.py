"""Parse data from fetched URL and write to file asynchronously."""
from aiofiles.threadpool.text import AsyncTextIOWrapper as AsyncIOFile
from logger import LOGGER

from .parser import parse_html_page_metadata


async def write_to_outfile(
    html: str, url: str, outfile: AsyncIOFile, total_count: int, i: int
):
    """
    Write contents of fetched URL to new file in local directory.

    :param str html: Source HTML of a single fetched URL.
    :param str url: Target URL to be fetched.
    :param AsyncIOFile outfile: Path of local file to write to.
    :param int total_count: Total number of URLs to be fetched.
    :param int i: Current iteration of URL out of total URLs.
    """
    try:
        page_metadata = await parse_html_page_metadata(html, url)
        await outfile.write(f"{page_metadata}\n")
        LOGGER.info(f"Fetched URL {i} of {total_count}: {page_metadata}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while writing page title: {e}")
