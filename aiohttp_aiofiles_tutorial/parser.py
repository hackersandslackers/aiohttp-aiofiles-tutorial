"""Parse metadata from raw HTML."""
from bs4 import BeautifulSoup
from bs4.builder import ParserRejectedMarkup
from logger import LOGGER


async def parse_html_page_metadata(html: str, url: str) -> str:
    """
    Extract page metadata from raw HTML into a CSV row.

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
        primary_tag = (
            soup.head
            .select_one("meta[property='article:tag']")
            .get("content")
        )
        published_at = (
            soup.head
            .select_one("meta[property='article:published_time']")
            .get("content")
            .split("T")[0]
        )
        if primary_tag is None:
            primary_tag = ""
        return f"{title}, {description}, {primary_tag}, {url}, {published_at}"
    except ParserRejectedMarkup as e:
        LOGGER.error(f"Failed to parse invalid html for {url}: {e}")
    except ValueError as e:
        LOGGER.error(f"ValueError occurred when parsing html for {url}: {e}")
    except Exception as e:
        LOGGER.error(f"Parsing failed when parsing html for {url}: {e}")
