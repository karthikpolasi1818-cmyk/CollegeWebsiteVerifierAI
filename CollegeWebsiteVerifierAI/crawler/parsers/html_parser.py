from bs4 import BeautifulSoup


class HTMLParser:

    @staticmethod
    def parse(html):

        return BeautifulSoup(
            html,
            "lxml"
        )