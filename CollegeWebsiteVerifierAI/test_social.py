from crawler.page_loader import PageLoader
from crawler.parsers.html_parser import HTMLParser
from crawler.link_extractor import LinkExtractor
from crawler.social_extractor import SocialExtractor


loader = PageLoader()

title, html = loader.load("https://www.iith.ac.in/")

soup = HTMLParser.parse(html)

links = LinkExtractor.extract(
    "https://www.iith.ac.in/",
    soup
)

social = SocialExtractor.extract(links)

print("\nSOCIAL LINKS\n")

for key, value in social.items():
    print(f"{key:12}: {value}")