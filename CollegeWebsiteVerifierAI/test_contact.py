from crawler.page_loader import PageLoader
from crawler.extractors.email_extractor import EmailExtractor
from crawler.extractors.phone_extractor import PhoneExtractor
from crawler.extractors.address_extractor import AddressExtractor

loader = PageLoader()

title, html = loader.load("https://www.iith.ac.in/")

emails = EmailExtractor.extract(html)
phones = PhoneExtractor.extract(html)
addresses = AddressExtractor.extract(html)

print("\nEMAILS")
print("-" * 50)

for email in emails:
    print(email)

print("\nPHONES")
print("-" * 50)

for phone in phones:
    print(phone)

print("\nADDRESSES")
print("-" * 50)

for address in addresses[:10]:
    print(address)