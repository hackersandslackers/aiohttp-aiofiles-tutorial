"""Simple script to create and execute tasks in a loop"""
import asyncio

from asyncio_tutorial.logger import LOGGER

from .coroutines import simple_coroutine
from .tasks import create_task


async def intro_tutorial():
    """Simple demonstration of a async script lifecycle"""
    LOGGER.info(f"Asyncio tutorial Part I: Intro to Asyncio.")
    tasks = []
    for i in range(3):
        task = await create_task(simple_coroutine(i, delay=1))
        tasks.append(task)
        LOGGER.info(type(task))
    await asyncio.gather(*tasks)
    LOGGER.info("-------------------------------------------")
