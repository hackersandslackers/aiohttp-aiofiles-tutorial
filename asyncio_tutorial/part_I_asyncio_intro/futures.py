"""Future which executes an action when loop is completed."""
import asyncio
from asyncio import Future

from asyncio_tutorial.logger import LOGGER


def register_future() -> Future:
    """
    Create a Future which triggers a callback when loop is completed.

    :returns: Future
    """
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    future.add_done_callback(loop_completed)
    return future


def loop_completed(result: str):
    """
    Callback function fired when loop is complete.

    :param str result: String describing the state of the loop
    """
    LOGGER.success(
        f"Loop completed with result: {result} \
        \n--------------------------------------"
    )
