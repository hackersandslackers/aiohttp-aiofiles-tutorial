"""Create and execute asynchronous tasks in a loop."""
import asyncio
import time

from asyncio_tutorial.logger import LOGGER

from .coroutines import simple_coroutine
from .futures import register_future
from .loops import inspect_event_loop
from .tasks import create_task


async def asyncio_intro_tutorial(start_time: float):
    """
    Demo of an asynchronous script's lifecycle.

    :param float start_time: Counter representing the time the script was initialized.
    """
    LOGGER.info(f"Asyncio tutorial Part I: Intro to Asyncio.")
    future = register_future()
    task_list = []
    for i in range(3):
        task = await create_task(simple_coroutine(i, delay=1))
        task_list.append(task)
    inspect_event_loop()
    await asyncio.gather(*task_list)
    future.set_result(
        f"Executed {__name__} in {time.perf_counter() - start_time:0.2f} seconds."
    )
