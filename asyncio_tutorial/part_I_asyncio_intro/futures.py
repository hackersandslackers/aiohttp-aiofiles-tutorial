import asyncio
from asyncio import Future

from asyncio_tutorial.logger import LOGGER


async def register_future() -> Future:
    """"""
    loop = asyncio.get_event_loop()
    future = Future(loop=loop)
    future.add_done_callback(loop_completed)
    return future


def loop_completed(result: str):
    """
    Callback to be called when loop is complete.

    :param str result:
    """
    LOGGER.success(f"Loop completed with result: {result} \
    \n-------------------------------------------------")
