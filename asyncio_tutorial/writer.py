"""Write to disk asynchronously."""
import aiofiles

from .logger import LOGGER


async def write_html_file(url: str, text: bytes, directory: str):
    """
    Write contents of fetched URL to new file in local directory.

    :param str url: URL which was fetched.
    :param bytes text: Source HTML of a single fetched URL.
    :param str directory: Local directory to save exports to.
    """
    try:
        filename = f"{directory}/{url.split('/')[-2]}.html"
        async with aiofiles.open(filename, mode="wb+") as f:
            await f.write(text)
            await f.close()
    except Exception as e:
        LOGGER.error(f"Unexpected error while writing file from `{url}`: {e}")
