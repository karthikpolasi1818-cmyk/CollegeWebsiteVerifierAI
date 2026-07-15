import re
from bs4 import BeautifulSoup


class SmartEmailExtractor:

    EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    @staticmethod
    def extract(html):

        soup = BeautifulSoup(html, "lxml")

        results = []

        # Search tables
        for table in soup.find_all("table"):

            text = table.get_text(" ", strip=True)

            emails = re.findall(
                SmartEmailExtractor.EMAIL_REGEX,
                text
            )

            for email in emails:

                results.append({
                    "source": "table",
                    "email": email
                })

        # Search cards/divs

        for div in soup.find_all(["div", "section", "article"]):

            text = div.get_text(" ", strip=True)

            emails = re.findall(
                SmartEmailExtractor.EMAIL_REGEX,
                text
            )

            for email in emails:

                results.append({
                    "source": "section",
                    "email": email
                })

        return results