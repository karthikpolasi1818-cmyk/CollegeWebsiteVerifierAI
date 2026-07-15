"""
crawler/multi_page_crawler.py

Production Multi Page Crawler
"""

from crawler.page_loader import PageLoader


class MultiPageCrawler:

    MAX_RETRIES = 2

    def __init__(self):

        self.loader = PageLoader()

    def crawl(self, pages):

        html_pages = {}

        visited = set()

        for name, url in pages.items():

            # Skip invalid URLs
            if not url:
                continue

            # Skip duplicates
            if url in visited:
                continue

            visited.add(url)

            success = False

            for attempt in range(1, self.MAX_RETRIES + 1):

                try:

                    title, html = self.loader.load(url)

                    # Skip empty pages
                    if not html:
                        raise Exception("Empty HTML")

                    html_pages[name] = {
                        "title": title,
                        "url": url,
                        "html": html,
                    }

                    print(f"✓ {name}")

                    success = True

                    break

                except Exception as e:

                    print(
                        f"Retry {attempt}/{self.MAX_RETRIES} "
                        f"for {name}: {e}"
                    )

            if not success:

                print(f"✗ {name} (Skipped)")

        return html_pages