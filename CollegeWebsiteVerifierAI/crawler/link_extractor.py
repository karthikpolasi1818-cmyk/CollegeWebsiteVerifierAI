"""
crawler/link_extractor.py

Production Link Extractor
"""

from urllib.parse import urljoin, urldefrag


class LinkExtractor:

    @staticmethod
    def extract(base_url, soup):

        links = []
        seen = set()

        for tag in soup.find_all("a", href=True):

            href = tag["href"].strip()

            if not href:
                continue

            # Ignore unwanted links
            if href.startswith((
                "#",
                "javascript:",
                "mailto:",
                "tel:"
            )):
                continue

            absolute = urljoin(base_url, href)

            # Remove URL fragments (#section)
            absolute, _ = urldefrag(absolute)

            # Only crawl HTTP/HTTPS
            if not absolute.startswith(("http://", "https://")):
                continue

            if absolute not in seen:
                seen.add(absolute)
                links.append(absolute)

        return links