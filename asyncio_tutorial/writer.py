"""Write to disk asynchronously."""
import aiofiles

from config import HTML_EXPORT_DIR


async def write_html_file(url: str, html: str):
    """
    Write contents of fetched URL to new file in local directory.

    :param str url: Fetched URL.
    :param str html: Source HTML of a single fetched URL.
    """
    try:
        filename = f"{HTML_EXPORT_DIR}/{url.split('/')[-2]}.html"
        async with aiofiles.open(filename, mode="wb+") as f:
            await f.write(text)
            await f.close()
    except Exception as e:
        LOGGER.error(f"Unexpected error while writing file from `{url}`: {e}")
