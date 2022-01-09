"""Parse data from fetched URL and write to file asynchronously."""
from aiofiles.threadpool.text import AsyncTextIOWrapper
from bs4 import BeautifulSoup
from logger import LOGGER


async def write_to_output_file(html_body: str, url: str, output_file: AsyncTextIOWrapper, total_count: int, i: int):
    """
    Write contents of fetched URL to new file in local directory.

    :param AsyncTextIOWrapper html_body: Source HTML of a single fetched URL.
    :param str url: Target URL to be fetched.
    :param str output_file: Filepath to local .json file to write output to.
    :param int total_count: Total number of URLs to be fetched.
    :param int i: Current iteration of URL out of total URLs.
    """
    try:
        page_title = await get_html_page_title(html_body, url)
        await output_file.write(f"{page_title}\n")
        LOGGER.info(f"Fetched URL {i} of {total_count}: {page_title}")
    except Exception as e:
        LOGGER.error(f"Unexpected error while writing page title: {e}")


async def get_html_page_title(html_body: str, url: str) -> str:
    """
    Extract page title from raw HTML of fetched URL; return a title/url pair.

    :param str html_body: Raw HTML source of a given fetched URL.
    :param str url: URL associated with the extracted HTML.
    """
    soup = BeautifulSoup(html_body, "html.parser")
    return f"{soup.title.string.replace(',', '')}, {url},"
