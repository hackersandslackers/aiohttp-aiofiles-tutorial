"""Write to disk asynchronously."""
import aiofiles

from .logger import LOGGER


async def write_fetched_file_locally(
    url: str, body: bytes, filetype: str, directory: str
):
    """
    Write contents of fetched URL to new file in local directory.

    :param str url: URL which was fetched.
    :param bytes body: Source HTML of a single fetched URL.
    :param str filetype: File extension to save fetched data as.
    :param str directory: Local directory to save exports to.
    """
    try:
        filename = f"{directory}/{url.split('/')[-2]}.{filetype}"
        async with aiofiles.open(filename, mode="wb+") as f:
            await f.write(body)
            await f.close()
    except Exception as e:
        LOGGER.error(f"Unexpected error while writing from `{url}`: {e}")
