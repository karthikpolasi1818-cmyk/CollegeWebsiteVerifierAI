from crawler.crawler import SmartCrawler

crawler = SmartCrawler()

data = crawler.crawl(
    "https://www.iith.ac.in/"
)

print("\nTITLE")
print(data["title"])

print("\nIMPORTANT PAGES")

for key, value in data["important_pages"].items():
    print(f"{key:15} {value}")

print("\nSOCIAL")

for key, value in data["social"].items():
    print(f"{key:12} {value}")