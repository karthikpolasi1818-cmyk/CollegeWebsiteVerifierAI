"""
crawler/extractors/email_extractor.py

Fast Email Extractor
"""

import re


class EmailExtractor:

    EMAIL_REGEX = re.compile(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    )

    INVALID = {
        "example.com",
        "test.com",
        "email.com",
        "domain.com",
    }

    @classmethod
    def extract(cls, html):

        if not html:
            return []

        emails = set()

        for email in cls.EMAIL_REGEX.findall(html):

            email = email.strip().lower()

            if any(domain in email for domain in cls.INVALID):
                continue

            if "noreply" in email or "no-reply" in email:
                continue

            emails.add(email)

        return sorted(emails)