"""
verifier/rule_verifier.py

Production Rule Verifier
"""

from urllib.parse import urlparse
from rapidfuzz import fuzz


class RuleVerifier:

    BAD_DOMAINS = {
        "wikipedia.org",
        "shiksha.com",
        "collegedunia.com",
        "careers360.com",
        "collegepravesh.com",
        "grokipedia.com",
        "reddit.com",
        "quora.com",
        "facebook.com",
    }

    GOOD_SUFFIXES = (
        ".ac.in",
        ".edu",
        ".edu.in",
        ".gov.in",
        ".nic.in",
    )

    def verify(self, college, data):

        score = 0

        website = data.get("website", "")
        title = data.get("title", "")
        socials = data.get("social", {})
        emails = data.get("emails", [])
        phones = data.get("phones", [])
        pages = data.get("pages", {})

        parsed = urlparse(website)

        domain = parsed.netloc.lower().replace("www.", "")

        # -------------------------------------------------
        # Reject known non-official domains
        # -------------------------------------------------

        if any(bad in domain for bad in self.BAD_DOMAINS):
            return {
                "verified": False,
                "confidence": 0
            }

        # -------------------------------------------------
        # HTTPS
        # -------------------------------------------------

        if website.startswith("https://"):
            score += 10

        # -------------------------------------------------
        # Official domain suffix
        # -------------------------------------------------

        if any(domain.endswith(s) for s in self.GOOD_SUFFIXES):
            score += 35

        # -------------------------------------------------
        # College name similarity
        # -------------------------------------------------

        similarity = fuzz.token_set_ratio(
            college.lower(),
            title.lower()
        )

        if similarity >= 95:
            score += 30

        elif similarity >= 85:
            score += 20

        elif similarity >= 70:
            score += 10

        # -------------------------------------------------
        # Important Pages
        # -------------------------------------------------

        important = [
            "contact",
            "about",
            "admission",
            "faculty",
            "office",
            "directory",
            "administration",
        ]

        count = 0

        for page in important:

            if pages.get(page):
                count += 1

        score += min(count * 4, 20)

        # -------------------------------------------------
        # Official Emails
        # -------------------------------------------------

        official = 0

        for email in emails:

            email = email.lower()

            if domain in email:
                official += 1

        score += min(official * 3, 12)

        # -------------------------------------------------
        # Phones
        # -------------------------------------------------

        if len(phones) >= 1:
            score += 5

        if len(phones) >= 3:
            score += 3

        # -------------------------------------------------
        # Social Media
        # -------------------------------------------------

        social_count = sum(
            bool(socials.get(key))
            for key in [
                "linkedin",
                "instagram",
                "facebook",
                "twitter",
                "youtube",
            ]
        )

        score += min(social_count * 2, 10)

        # -------------------------------------------------
        # Final Score
        # -------------------------------------------------

        score = max(0, min(score, 100))

        return {
            "verified": score >= 75,
            "confidence": score,
        }