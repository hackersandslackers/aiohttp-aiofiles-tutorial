"""Custom logger."""
from os import path
from sys import stdout

from loguru import logger as custom_logger

from config import ENVIRONMENT


def formatter(log: dict) -> str:
    """
    Format log colors based on level.

    :param dict log: Dictionary containing log level, details, etc.

    :returns: str
    """
    if log["level"].name == "SUCCESS":
        return (
            "<fg #aad1f7>{time:HH:mm:ss A}</fg #aad1f7> | "
            "<light-green>{level}</light-green>: "
            "<light-white>{message}</light-white> \n"
        )
    if log["level"].name == "WARNING":
        return (
            "<fg #aad1f7>{time:HH:mm:ss A}</fg #aad1f7> | "
            "<light-yellow>{level}</light-yellow>: "
            "<light-white>{message}</light-white> \n"
        )
    elif log["level"].name == "ERROR":
        return (
            "<fg #aad1f7>{time:HH:mm:ss A}</fg #aad1f7> | "
            "<light-red>{level}</light-red>: "
            "<light-white>{message}</light-white> \n"
        )
    else:
        return (
            "<fg #aad1f7>{time:HH:mm:ss A}</fg #aad1f7> | "
            "<fg #67c9c4>{level}</fg #67c9c4>: "
            "<light-white>{message}</light-white> \n"
        )


def create_logger() -> custom_logger:
    """
    Create custom logger.

    :returns: custom_logger
    """
    custom_logger.remove()
    custom_logger.add(stdout, colorize=True, format=formatter)
    if ENVIRONMENT == "production":
        # Datadog JSON logs
        custom_logger.add(
            "/var/log/asyncio_tutorial/info.json",
            format=formatter,
            rotation="500 MB",
            compression="zip",
        )
    return custom_logger


LOGGER = create_logger()
