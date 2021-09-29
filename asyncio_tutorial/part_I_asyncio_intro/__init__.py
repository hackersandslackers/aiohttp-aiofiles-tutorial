"""Simple script to create and execute tasks in a loop"""
import asyncio

from asyncio_tutorial.logger import LOGGER

from .coroutines import simple_coroutine
from .futures import register_future
from .loops import inspect_event_loop
from .tasks import create_task


async def asyncio_intro_tutorial():
    """Simple demonstration of a async script lifecycle"""
    LOGGER.info(f"Asyncio tutorial Part I: Intro to Asyncio.")
    tasks = []
    future = register_future()
    for i in range(3):
        task = await create_task(simple_coroutine(i, delay=1))
        tasks.append(task)
    inspect_event_loop()
    await asyncio.gather(*tasks)
    future.set_result("Done")
