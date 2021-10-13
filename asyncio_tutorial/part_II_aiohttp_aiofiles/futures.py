"""Create a Future (callback): an action to be taken when loop is completed."""
import asyncio
from asyncio import Future

from asyncio_tutorial.logger import LOGGER


def register_future() -> Future:
    """
    Create a Future to log when loop is completed.

    :returns: Future
    """
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    future.add_done_callback(loop_completed)
    return future


def loop_completed(result: str):
    """
    Callback to be executed when loop is complete.

    :param str result: Result of the loop & its execution time.
    """
    LOGGER.success(result)
