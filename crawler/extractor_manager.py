"""
crawler/extractor_manager.py

Production Extractor Manager
"""

from crawler.extractors.email_extractor import EmailExtractor
from crawler.extractors.phone_extractor import PhoneExtractor
from crawler.extractors.address_extractor import AddressExtractor

from crawler.data_cleaner import DataCleaner


class ExtractorManager:

    def __init__(self):
        pass

    def extract(self, html_pages):

        all_emails = set()
        all_phones = set()
        all_addresses = []

        for page_name, page in html_pages.items():

            html = page.get("html", "")

            if not html:
                continue

            # -----------------------------
            # Emails
            # -----------------------------
            try:

                emails = EmailExtractor.extract(html)

                for email in emails:

                    email = email.strip().lower()

                    if (
                        not email
                        or "example.com" in email
                        or "noreply" in email
                        or "no-reply" in email
                    ):
                        continue

                    all_emails.add(email)

            except Exception:
                pass

            # -----------------------------
            # Phones
            # -----------------------------
            try:

                phones = PhoneExtractor.extract(html)

                for phone in phones:

                    phone = phone.strip()

                    digits = "".join(filter(str.isdigit, phone))

                    # Keep only reasonable phone numbers
                    if 10 <= len(digits) <= 15:
                        all_phones.add(phone)

            except Exception:
                pass

            # -----------------------------
            # Addresses
            # -----------------------------
            try:

                addresses = AddressExtractor.extract(html)

                for address in addresses:

                    address = address.strip()

                    if len(address) < 20:
                        continue

                    all_addresses.append(address)

            except Exception:
                pass

        # ---------------------------------
        # Clean Data
        # ---------------------------------

        cleaned_emails = DataCleaner.clean_emails(
            sorted(all_emails)
        )

        cleaned_phones = DataCleaner.clean_phones(
            sorted(all_phones)
        )

        cleaned_addresses = DataCleaner.clean_addresses(
            all_addresses
        )

        return {

            "emails": cleaned_emails,

            "phones": cleaned_phones,

            "addresses": cleaned_addresses

        }