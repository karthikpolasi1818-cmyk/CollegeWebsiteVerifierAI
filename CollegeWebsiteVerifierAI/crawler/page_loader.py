"""
crawler/page_loader.py

Production Page Loader
"""

from playwright.sync_api import TimeoutError

from crawler.browser import Browser


class PageLoader:

    def __init__(self):

        self.browser = Browser(headless=True)

    def load(self, url):

        self.browser.start()

        page = None

        try:

            page = self.browser.new_page()

            page.goto(
                url,
                timeout=30000,
                wait_until="domcontentloaded"
            )

            try:
                page.wait_for_load_state(
                    "networkidle",
                    timeout=5000
                )
            except TimeoutError:
                pass

            title = page.title()

            html = page.content()

            return title, html

        except TimeoutError:

            print(f"Timeout: {url}")

            return "", ""

        except Exception as e:

            print(e)

            return "", ""

        finally:

            try:

                if page:
                    page.close()

            except Exception:
                pass