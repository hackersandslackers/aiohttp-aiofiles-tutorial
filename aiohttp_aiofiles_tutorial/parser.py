"""Parse metadata from raw HTML."""
from bs4 import BeautifulSoup
from logger import LOGGER


async def parse_html_page_data(html: str, url: str) -> str:
    """
    Extract page title from raw HTML of fetched URL; return a title

    :param str html: Raw HTML source of a given fetched URL.
    :param str url: URL associated with the extracted HTML.

    :returns: str
    """
    try:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string.replace(",", ";")
        description = (
            soup.head.select_one("meta[name=description]")
            .get("content")
            .replace(",", ";")
            .replace('"', "`")
            .replace("'", "`")
        )
        primary_tag = soup.head.select_one("meta[property='article:tag']").get("content")
        published_at = soup.head.select_one("meta[property='article:published_time']").get(
            "content"
        ).split("T")[0]
        if primary_tag is None:
            primary_tag = ""
        return f"{title}, {description}, {primary_tag}, {url}, {published_at}"
    except ValueError as e:
        LOGGER.error(f"Parsing failed for {url}: {e}")
    except Exception as e:
        LOGGER.error(f"Parsing failed for {url}: {e}")
