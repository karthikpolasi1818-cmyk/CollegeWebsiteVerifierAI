from crawler.page_loader import PageLoader
from crawler.parsers.html_parser import HTMLParser
from crawler.link_extractor import LinkExtractor


loader = PageLoader()

title, html = loader.load(
    "https://www.iith.ac.in/"
)

print("Title:", title)

soup = HTMLParser.parse(html)

links = LinkExtractor.extract(
    "https://www.iith.ac.in/",
    soup
)

print(f"\nTotal Links Found: {len(links)}\n")

for i, link in enumerate(links[:30], start=1):
    print(f"{i}. {link}")