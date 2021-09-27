"""Demonstrate Parts 1 and 2 of Hackersandslackers Asyncio tutorial series"""
import asyncio

from asyncio_tutorial.logger import LOGGER

from .part_I_asyncio_intro import intro_tutorial
from .part_II_aiohttp_aiofiles import aiohttp_aiofiles_tutorial


def init_script():
    asyncio.run(intro_tutorial())
    asyncio.run(aiohttp_aiofiles_tutorial())
