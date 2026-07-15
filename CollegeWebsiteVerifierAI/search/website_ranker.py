"""
search/website_ranker.py

Production Website Ranker
"""

from urllib.parse import urlparse

from rapidfuzz import fuzz


class WebsiteRanker:

    BLOCKED = {

        "wikipedia",

        "collegedunia",

        "collegepravesh",

        "careers360",

        "shiksha",

        "getmyuni",

        "facebook",

        "instagram",

        "linkedin",

        "youtube",

        "reddit",

        "quora",

        "x.com",

        "twitter.com",

        "grokipedia"

    }

    GOOD_SUFFIXES = (

        ".ac.in",

        ".edu",

        ".edu.in",

        ".gov.in",

        ".nic.in"

    )

    IMPORTANT_WORDS = {

        "iit",

        "iiit",

        "nit",

        "iim",

        "government",

        "polytechnic",

        "engineering",

        "technology",

        "university",

        "college"

    }

    @classmethod
    def score(cls, result, college):

        score = 0

        url = result.url.lower()

        title = result.title.lower()

        snippet = result.snippet.lower()

        college = college.lower()

        parsed = urlparse(url)

        domain = parsed.netloc.replace("www.", "")

        path = parsed.path.lower()

        # ---------------------------------
        # Reject Aggregators
        # ---------------------------------

        if any(site in domain for site in cls.BLOCKED):

            return 0

        # ---------------------------------
        # HTTPS
        # ---------------------------------

        if url.startswith("https://"):

            score += 10

        # ---------------------------------
        # Homepage
        # ---------------------------------

        if path in ("", "/"):

            score += 25

        else:

            score -= 5

        # ---------------------------------
        # Official Domain
        # ---------------------------------

        if any(domain.endswith(s) for s in cls.GOOD_SUFFIXES):

            score += 35

        # ---------------------------------
        # Fuzzy Matching
        # ---------------------------------

        title_score = fuzz.token_set_ratio(
            college,
            title
        )

        snippet_score = fuzz.token_set_ratio(
            college,
            snippet
        )

        url_score = fuzz.partial_ratio(
            college,
            url
        )

        score += title_score * 0.45

        score += snippet_score * 0.20

        score += url_score * 0.20

        # ---------------------------------
        # Exact Important Words
        # ---------------------------------

        college_words = set(college.split())

        title_words = set(title.split())

        common = college_words & title_words

        score += len(common & cls.IMPORTANT_WORDS) * 3

        # ---------------------------------
        # Internal Pages Penalty
        # ---------------------------------

        for bad in [

            "/admission",

            "/faculty",

            "/career",

            "/careers",

            "/news",

            "/gallery",

            "/event",

            "/notification",

            "/academics",

            "/research",

            "/placement"

        ]:

            if bad in path:

                score -= 15

        # ---------------------------------
        # Missing College Name Penalty
        # ---------------------------------

        if fuzz.token_set_ratio(college, title) < 60:

            score -= 30

        return round(max(score, 0), 2)

    @classmethod
    def rank(cls, results, college):

        ranked = []

        for result in results:

            ranked.append(

                (

                    cls.score(result, college),

                    result

                )

            )

        ranked.sort(

            key=lambda x: x[0],

            reverse=True

        )

        return ranked