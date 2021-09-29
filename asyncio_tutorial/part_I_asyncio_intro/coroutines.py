"""Create a coroutine containing the business logic of our task."""
import asyncio

from asyncio_tutorial.logger import LOGGER


async def simple_coroutine(number: int, delay=1):
    """
    Wait for a time delay, log number associated with the coroutine.

    :param int number: Number to identify the current coroutine.
    :param int delay: Time delay to simulate a function which takes time to complete.
    """
    await asyncio.sleep(delay)
    LOGGER.info(f"This is Coroutine {number} being executed.")
