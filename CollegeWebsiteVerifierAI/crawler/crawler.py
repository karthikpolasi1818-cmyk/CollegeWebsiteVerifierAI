"""
crawler/crawler.py

Production Smart Crawler
"""

from crawler.page_loader import PageLoader
from crawler.parsers.html_parser import HTMLParser
from crawler.link_extractor import LinkExtractor
from crawler.social_extractor import SocialExtractor


class SmartCrawler:

    IMPORTANT_KEYWORDS = {
        "contact": [
            "contact",
            "contact-us",
            "contacts"
        ],
        "about": [
            "about",
            "about-us",
            "overview"
        ],
        "admission": [
            "admission",
            "admissions",
            "apply"
        ],
        "career": [
            "career",
            "careers",
            "recruitment",
            "jobs"
        ],
        "directory": [
            "directory",
            "staff-directory"
        ],
        "faculty": [
            "faculty",
            "faculties",
            "people"
        ],
        "administration": [
            "administration",
            "governance",
            "administrative"
        ],
        "office": [
            "office",
            "registrar"
        ],
        "placement": [
            "placement",
            "placements",
            "training-placement",
            "career-development"
        ]
    }

    def __init__(self):

        self.loader = PageLoader()

    def crawl(self, url):

        title, html = self.loader.load(url)

        # Page failed
        if not html:

            return {
                "title": "",
                "homepage": url,
                "social": {},
                "links": [],
                "important_pages": {}
            }

        soup = HTMLParser.parse(html)

        links = LinkExtractor.extract(url, soup)

        # Remove duplicates while preserving order
        links = list(dict.fromkeys(links))

        social = SocialExtractor.extract(links)

        important_pages = {}

        for link in links:

            lower = link.lower()

            for page_name, keywords in self.IMPORTANT_KEYWORDS.items():

                if page_name in important_pages:
                    continue

                if any(keyword in lower for keyword in keywords):

                    important_pages[page_name] = link

        return {

            "title": title,

            "homepage": url,

            "social": social,

            "links": links,

            "important_pages": important_pages

        }