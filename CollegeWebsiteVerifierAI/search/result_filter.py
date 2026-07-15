from urllib.parse import urlparse


BLOCKED_DOMAINS = {
    "wikipedia.org",
    "facebook.com",
    "instagram.com",
    "youtube.com",
    "linkedin.com",
    "careers360.com",
    "shiksha.com",
    "collegedunia.com",
    "getmyuni.com",
    "collegebatch.com",
}


class ResultFilter:

    @staticmethod
    def filter(results):

        filtered = []

        for result in results:

            domain = urlparse(result.url).netloc.lower()

            blocked = False

            for item in BLOCKED_DOMAINS:

                if item in domain:

                    blocked = True
                    break

            if not blocked:

                filtered.append(result)

        return filtered