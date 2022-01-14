"""Test metadata parser accuracy with local HTML file."""
import aiofiles
import pytest
import pytest_asyncio
from config import BASE_DIR

from aiohttp_aiofiles_tutorial.parser import parse_html_page_data


@pytest_asyncio.fixture
async def sample_page_metadata():
    """Expected metadata to be returned from parsing `intro_to_asyncio.html`"""
    title = "Intro to Asynchronous Python with Asyncio"
    description = "Execute multiple tasks concurrently in Python with Asyncio: Python`s built-in async library."
    tag = "Python"
    url = "https://hackersandslackers.com/intro-to-asyncio-concurrency/"
    published_at = "2022-01-04"
    return ", ".join([title, description, tag, url, published_at])


@pytest.mark.asyncio
async def test_parse_html_page_data(sample_page_metadata):
    """Verify HTML parser outputs expected values"""
    test_file = f"{BASE_DIR}/aiohttp_aiofiles_tutorial/tests/resources/intro_to_asyncio.html"
    async with aiofiles.open(test_file, mode="r") as file:
        html = await file.read()
        url = "https://hackersandslackers.com/intro-to-asyncio-concurrency/"
        metadata = await parse_html_page_data(html, url)
        assert metadata == sample_page_metadata
        await file.close()
