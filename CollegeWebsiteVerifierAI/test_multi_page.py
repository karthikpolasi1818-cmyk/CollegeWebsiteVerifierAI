from crawler.crawler import SmartCrawler
from crawler.multi_page_crawler import MultiPageCrawler

crawler = SmartCrawler()

data = crawler.crawl(
    "https://www.iith.ac.in/"
)

multi = MultiPageCrawler()

pages = multi.crawl(
    data["important_pages"]
)

print()

print("TOTAL PAGES")

print(len(pages))

print()

for page in pages:

    print(page)

    print(pages[page]["title"])

    print("-" * 60)