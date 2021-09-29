"""Create task from coroutine which displays a value after a delay."""
import asyncio
from asyncio import Task


async def create_task(coroutine) -> Task:
    """
    Create asyncio tasks to be executed.

    :param coroutine: Coroutine to create async task from.

    :returns: Task
    """
    return asyncio.create_task(coroutine)
