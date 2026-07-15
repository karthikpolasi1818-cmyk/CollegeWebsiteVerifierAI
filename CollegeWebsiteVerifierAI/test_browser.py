from crawler.page_loader import PageLoader


loader = PageLoader()

title, html = loader.load(
    "https://www.iith.ac.in/"
)

print()

print(title)

print()

print(len(html))