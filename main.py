"""Script entry point."""
from asyncio_tutorial import bulk_task_runner, get_list_of_urls

urls = get_list_of_urls()

if __name__ == "__main__":
    bulk_task_runner(urls)
