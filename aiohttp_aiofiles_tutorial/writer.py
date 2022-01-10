"""Parse data from fetched URL and write to file asynchronously."""
from aiofiles.threadpool.text import AsyncTextIOWrapper as AsyncIOFile
from bs4 import BeautifulSoup
from logger import LOGGER


async def write_to_outfile(html: str, url: str, outfile: AsyncIOFile, total_count: int, i: int):
    """
    Write contents of fetched URL to new file in local directory.

    :param str html: Source HTML of a single fetched URL.
    :param str url: Target URL to be fetched.
    :param AsyncIOFile outfile: Path of local file to write to.
    :param int total_count: Total number of URLs to be fetched.
    :param int i: Current iteration of URL out of total URLs.
    """
    try:
        page_title = await get_html_page_title(html, url)
        await outfile.write(f"{page_title}\n")
        LOGGER.info(f"Fetched URL {i} of {total_count}: {page_title}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while writing page title: {e}")


async def get_html_page_title(html: str, url: str) -> str:
    """
    Extract page title from raw HTML of fetched URL; return a title/url pair.

    :param str html: Raw HTML source of a given fetched URL.
    :param str url: URL associated with the extracted HTML.

    :returns: str
    """
    soup = BeautifulSoup(html, "html.parser")
    return f"{soup.title.string.replace(',', '')}, {url},"
