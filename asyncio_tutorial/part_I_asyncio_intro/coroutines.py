"""Create a coroutine function to be executed as asyncio task."""
import asyncio

from asyncio_tutorial.logger import LOGGER


async def simple_coroutine(number: int, delay=1):
    """
    Wait for a time delay & display number associated with coroutine.

    :param int number: Number to identify the current coroutine.
    :param int delay: Time delay to simulate function delay.
    """
    await asyncio.sleep(delay)
    LOGGER.info(f"This is Coroutine {number} being executed.")
