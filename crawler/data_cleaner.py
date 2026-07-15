"""
crawler/data_cleaner.py

Production Data Cleaner
"""

import re


class DataCleaner:

    PERSONAL_DOMAINS = {
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com",
        "live.com",
        "icloud.com",
        "proton.me",
        "protonmail.com",
        "rediffmail.com",
    }

    INVALID_EMAIL_WORDS = {
        "noreply",
        "no-reply",
        "donotreply",
        "test",
        "example",
    }

    @classmethod
    def clean_emails(cls, emails):

        cleaned = []
        seen = set()

        for email in emails:

            if not email:
                continue

            email = email.strip().lower()

            if any(word in email for word in cls.INVALID_EMAIL_WORDS):
                continue

            if any(email.endswith(domain) for domain in cls.PERSONAL_DOMAINS):
                continue

            if email not in seen:
                seen.add(email)
                cleaned.append(email)

        return cleaned

    @staticmethod
    def clean_phones(phones):

        cleaned = []
        seen = set()

        for phone in phones:

            digits = re.sub(r"\D", "", phone)

            # Remove country code
            if digits.startswith("91") and len(digits) == 12:
                digits = digits[2:]

            # Accept only valid 10-digit Indian mobile numbers
            if len(digits) != 10:
                continue

            if digits[0] not in "6789":
                continue

            if digits not in seen:
                seen.add(digits)
                cleaned.append(digits)

        return cleaned

    @staticmethod
    def clean_addresses(addresses):

        cleaned = []
        seen = set()

        for addr in addresses:

            if not addr:
                continue

            addr = " ".join(addr.split())

            if len(addr) < 20:
                continue

            if len(addr) > 250:
                continue

            key = addr.lower()

            if key not in seen:
                seen.add(key)
                cleaned.append(addr)

        return cleaned