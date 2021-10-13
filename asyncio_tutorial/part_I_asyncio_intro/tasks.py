"""Create task from coroutine which displays a value after a delay."""
import asyncio
from asyncio import Task
from typing import Coroutine


async def create_task(coroutine: Coroutine) -> Task:
    """
    Create asyncio tasks to be executed.

    :param Callable coroutine: Coroutine to create async task from.

    :returns: Task
    """
    return asyncio.create_task(coroutine)
