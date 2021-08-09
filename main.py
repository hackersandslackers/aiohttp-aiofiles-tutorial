"""Script entry point."""
from asyncio_tutorial import bulk_http_fetcher
from config import URLS

if __name__ == '__main__':
    bulk_http_fetcher(URLS)

