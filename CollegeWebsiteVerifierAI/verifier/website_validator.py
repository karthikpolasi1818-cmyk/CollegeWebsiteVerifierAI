"""
verifier/website_validator.py
"""

import re

from rapidfuzz import fuzz


class WebsiteValidator:

    @staticmethod
    def normalize(text):

        text = text.lower()

        text = re.sub(r"[^a-z0-9 ]", " ", text)

        text = " ".join(text.split())

        return text

    @classmethod
    def validate(
        cls,
        college,
        homepage_title,
        homepage_html
    ):

        college = cls.normalize(college)

        title = cls.normalize(homepage_title)

        html = cls.normalize(homepage_html[:3000])

        score = 0

        if college in title:
            score += 50

        elif fuzz.token_set_ratio(college, title) > 90:
            score += 40

        if college in html:
            score += 40

        elif fuzz.partial_ratio(college, html) > 90:
            score += 30

        verified = score >= 60

        return verified, score