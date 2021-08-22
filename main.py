"""Script entry point."""
import asyncio

from asyncio_tutorial import init_script, parse_urls

urls = parse_urls()

if __name__ == "__main__":
    asyncio.run(init_script(urls))
