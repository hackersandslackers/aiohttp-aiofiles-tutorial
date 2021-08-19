"""Script entry point."""
from asyncio_tutorial import bulk_task_runner
from asyncio_tutorial.reader import parse_urls

urls = parse_urls()

if __name__ == "__main__":
    bulk_task_runner(urls)
