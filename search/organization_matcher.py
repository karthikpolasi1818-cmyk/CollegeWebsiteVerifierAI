"""
search/organization_matcher.py

Production Organization Matcher
"""

import re

from rapidfuzz import fuzz


class OrganizationMatcher:

    LOCATION_WORDS = {
        "hyderabad", "warangal", "bilaspur", "marwahi",
        "pathariya", "raipur", "durg", "bhilai",
        "nagpur", "pune", "mumbai", "delhi",
        "chennai", "kolkata", "jaipur", "bhopal",
        "indore", "vizag", "vijayawada", "tirupati",
        "kakinada", "anantapur", "kadapa",
        "guntur", "nellore", "sangareddy"
    }

    @staticmethod
    def normalize(text):

        text = text.lower()

        text = re.sub(r"[^a-z0-9 ]", " ", text)

        text = " ".join(text.split())

        return text

    @classmethod
    def score(cls, college, title):

        college = cls.normalize(college)
        title = cls.normalize(title)

        # ---------------------------------
        # IIT vs IIIT
        # ---------------------------------

        if "iit" in college.split() and "iiit" in title.split():
            return 0

        if "iiit" in college.split() and "iit" in title.split():
            return 0

        # ---------------------------------
        # Compare city/location words
        # ---------------------------------

        college_locations = {
            word for word in college.split()
            if word in cls.LOCATION_WORDS
        }

        title_locations = {
            word for word in title.split()
            if word in cls.LOCATION_WORDS
        }

        if college_locations and title_locations:

            if college_locations != title_locations:
                return 20

        # ---------------------------------
        # Fuzzy Scores
        # ---------------------------------

        token = fuzz.token_set_ratio(
            college,
            title
        )

        partial = fuzz.partial_ratio(
            college,
            title
        )

        ratio = fuzz.ratio(
            college,
            title
        )

        score = (
            token * 0.5 +
            partial * 0.3 +
            ratio * 0.2
        )

        return round(score, 2)