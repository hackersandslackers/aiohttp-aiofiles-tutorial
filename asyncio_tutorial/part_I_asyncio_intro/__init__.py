"""Simple script to create and execute tasks in a loop"""
import asyncio
from asyncio import Future

from asyncio_tutorial.logger import LOGGER

from .tasks import create_tasks


async def asyncio_intro_tutorial():
    """Simple demonstration of a async script lifecycle"""
    LOGGER.info(f"Asyncio tutorial Part I: Intro to Asyncio.")
    future = register_future()
    tasks = await create_tasks()
    inspect_event_loop()
    await asyncio.gather(*tasks)
    future.set_result("Done")


def inspect_event_loop():
    """Get event loop info."""
    loop = asyncio.get_event_loop()
    thread_id = loop.__dict__.get('_thread_id')
    if loop.is_running():
        LOGGER.info(f"Loop has been running {loop.time()} seconds. (Thread ID #{thread_id})")


def register_future() -> Future:
    """"""
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    future.add_done_callback(loop_completed)
    return future


def loop_completed(result: str):
    """
    Callback to be called when loop is complete.

    :param str result:
    """
    LOGGER.success(f"Loop completed with result: {result} \
    \n-------------------------------------------------")
