"""
crawler/extractors/address_extractor.py

Fast Address Extractor
"""

import re

from bs4 import BeautifulSoup


class AddressExtractor:

    KEYWORDS = [
        "address",
        "campus",
        "location",
        "road",
        "street",
        "lane",
        "district",
        "city",
        "state",
        "india",
        "telangana",
        "andhra",
        "maharashtra",
        "karnataka",
        "chhattisgarh",
        "odisha",
        "tamil nadu",
        "kerala",
        "gujarat",
        "rajasthan",
        "punjab",
        "haryana",
        "west bengal",
        "uttar pradesh",
        "madhya pradesh",
        "pin",
        "pincode",
        "postal code"
    ]

    MAX_TEXT = 50000

    @classmethod
    def extract(cls, html):

        if not html:
            return []

        soup = BeautifulSoup(html, "lxml")

        # Remove unwanted tags
        for tag in soup([
            "script",
            "style",
            "noscript",
            "svg"
        ]):
            tag.decompose()

        text = soup.get_text(
            separator="\n",
            strip=True
        )

        # Limit processing
        text = text[:cls.MAX_TEXT]

        addresses = []

        for line in text.splitlines():

            line = line.strip()

            if len(line) < 20:
                continue

            lower = line.lower()

            if any(k in lower for k in cls.KEYWORDS):

                line = re.sub(r"\s+", " ", line)

                if line not in addresses:

                    addresses.append(line)

            if len(addresses) >= 10:
                break

        return addresses