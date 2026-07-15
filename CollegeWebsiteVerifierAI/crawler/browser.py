"""
crawler/browser.py

Production Singleton Browser Manager
"""

from playwright.sync_api import sync_playwright


class Browser:

    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.playwright = None
            cls._instance.browser = None
            cls._instance.headless = True

        return cls._instance

    def start(self):

        # Already running
        if self.browser is not None:
            return

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=self.headless
        )

    def stop(self):

        # Close browser safely
        try:

            if self.browser is not None:

                self.browser.close()

        except Exception as e:

            print(f"Browser Close Warning: {e}")

        finally:

            self.browser = None

        # Stop Playwright safely
        try:

            if self.playwright is not None:

                self.playwright.stop()

        except Exception as e:

            print(f"Playwright Stop Warning: {e}")

        finally:

            self.playwright = None

    def new_page(self):

        self.start()

        page = self.browser.new_page()

        page.set_default_timeout(30000)
        page.set_default_navigation_timeout(30000)

        return page