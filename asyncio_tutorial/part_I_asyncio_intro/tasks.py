"""Create task from provided coroutine."""
from typing import List
import asyncio
from asyncio import Task

from .coroutines import simple_coroutine


async def create_tasks() -> List[Task]:
    """
    Create asyncio tasks to be executed.

    :returns: List[Task]
    """
    tasks = []
    for i in range(3):
        task = await asyncio.create_task(simple_coroutine(i, delay=1))
        tasks.append(task)
    return tasks
