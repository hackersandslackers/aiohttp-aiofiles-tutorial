"""Demonstrate Parts 1 and 2 of Hackersandslackers Asyncio tutorial series"""
import asyncio
from asyncio import Future

from asyncio_tutorial.logger import LOGGER

from .part_I_asyncio_intro import asyncio_intro_tutorial
from .part_II_aiohttp_aiofiles import aiohttp_aiofiles_tutorial


def init_script():
    """
    Run source code found in Hackersandslackers asyncio tutorials.

    1. Intro to Async Python: https://hackersandslackers.com/python-concurrency-asyncio/
    2. Intro to Async Python: https://hackersandslackers.com/async-requests-with-aiohttp/
    """
    asyncio.run(asyncio_intro_tutorial())
    asyncio.run(aiohttp_aiofiles_tutorial())


def loop_completed(tutorial_1):
    loop = asyncio.get_event_loop()
    future = Future(loop=loop)
    future.add_done_callback(loop_completed)
