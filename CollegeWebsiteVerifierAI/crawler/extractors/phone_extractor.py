"""
crawler/extractors/phone_extractor.py

Fast Phone Extractor
"""

import re


class PhoneExtractor:

    PHONE_REGEX = re.compile(
        r"(?:\+91[-\s]?)?[6-9]\d{9}"
    )

    @classmethod
    def extract(cls, html):

        if not html:
            return []

        phones = set()

        for phone in cls.PHONE_REGEX.findall(html):

            digits = "".join(filter(str.isdigit, phone))

            if len(digits) >= 10:
                phones.add(phone)

        return sorted(phones)