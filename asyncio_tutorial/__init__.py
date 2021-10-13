"""Demonstrate Parts 1 and 2 of Hackersandslackers Asyncio tutorial series"""
import asyncio
import time

from asyncio_tutorial.logger import LOGGER

from .part_I_asyncio_intro import asyncio_intro_tutorial
from .part_II_aiohttp_aiofiles import aiohttp_aiofiles_tutorial


def init_script():
    """
    Run source code found in Hackersandslackers asyncio tutorials.

    1. Intro to Async Python: https://hackersandslackers.com/python-concurrency-asyncio/
    2. Async HTTP Requests with Aiohttp & Aiofiles: https://hackersandslackers.com/async-requests-with-aiohttp/
    """
    tutorial_part_one()
    time.sleep(3)
    tutorial_part_two()


def tutorial_part_one():
    """Run `Intro to Async Python` script."""
    start_time = time.perf_counter()
    asyncio.run(asyncio_intro_tutorial(start_time))
    LOGGER.warning(
        f"Tutorial Part I completed. Starting part II in 3 seconds... \
        \n--------------------------------------"
    )


def tutorial_part_two():
    """Run `Async HTTP Requests with Aiohttp & Aiofiles` script."""
    start_time = time.perf_counter()
    asyncio.run(aiohttp_aiofiles_tutorial(start_time))
    LOGGER.warning(f"Tutorial Part II completed. Thanks for playing!")
