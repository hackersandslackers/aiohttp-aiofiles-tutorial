"""Create task from provided coroutine."""
import asyncio
from asyncio import Task

from asyncio_tutorial.logger import LOGGER


async def create_task(coroutine) -> Task:
    """
    Create asyncio tasks to be executed.

    :param coroutine: Coroutine to create async task from.

    :returns: Task
    """
    LOGGER.info(type(coroutine))
    return asyncio.create_task(coroutine)
