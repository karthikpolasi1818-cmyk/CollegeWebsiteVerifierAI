"""
exporter/excel_writer.py

Production Excel Writer
"""

import os
import pandas as pd


class ExcelWriter:

    def __init__(self, input_file, output_file):

        self.input_file = input_file
        self.output_file = output_file

        self.df = pd.read_excel(input_file)

    def create_columns(self):

        columns = [
            "Official Website",
            "Confidence",
            "Verified",
            "LinkedIn",
            "Instagram",
            "Facebook",
            "Twitter",
            "YouTube",
            "Telegram",
            "WhatsApp",
            "Emails",
            "Phones",
            "Address",
            "Contact Page",
            "Admission Page",
            "About Page",
            "Faculty Page",
            "Directory Page",
            "Office Page",
            "Administration Page",
            "Status"
        ]

        for column in columns:

            if column not in self.df.columns:

                self.df[column] = ""

        # Convert all output columns to string
        for column in columns:
            self.df[column] = self.df[column].astype("string")

    def update(self, index, data):

        social = data.get("social", {})
        pages = data.get("pages", {})

        # -------------------------
        # Website
        # -------------------------

        self.df.at[index, "Official Website"] = str(
            data.get("website", "")
        )

        # -------------------------
        # Confidence
        # -------------------------

        self.df.at[index, "Confidence"] = str(
            data.get("confidence", "")
        )

        # -------------------------
        # Verified
        # -------------------------

        verified = bool(data.get("verified", False))

        self.df.at[index, "Verified"] = (
            "Yes" if verified else "No"
        )

        # -------------------------
        # Social Links
        # -------------------------

        self.df.at[index, "LinkedIn"] = str(
            social.get("linkedin", "")
        )

        self.df.at[index, "Instagram"] = str(
            social.get("instagram", "")
        )

        self.df.at[index, "Facebook"] = str(
            social.get("facebook", "")
        )

        self.df.at[index, "Twitter"] = str(
            social.get("twitter", "")
        )

        self.df.at[index, "YouTube"] = str(
            social.get("youtube", "")
        )

        self.df.at[index, "Telegram"] = str(
            social.get("telegram", "")
        )

        self.df.at[index, "WhatsApp"] = str(
            social.get("whatsapp", "")
        )

        # -------------------------
        # Emails
        # -------------------------

        emails = data.get("emails", [])

        if isinstance(emails, list):
            emails = sorted(set(emails))
            emails = ", ".join(emails)

        self.df.at[index, "Emails"] = str(emails)

        # -------------------------
        # Phones
        # -------------------------

        phones = data.get("phones", [])

        if isinstance(phones, list):
            phones = sorted(set(phones))
            phones = ", ".join(phones)

        self.df.at[index, "Phones"] = str(phones)

        # -------------------------
        # Addresses
        # -------------------------

        addresses = data.get("addresses", [])

        if isinstance(addresses, list):
            addresses = " | ".join(addresses)

        self.df.at[index, "Address"] = str(addresses)

        # -------------------------
        # Important Pages
        # -------------------------

        self.df.at[index, "Contact Page"] = str(
            pages.get("contact", "")
        )

        self.df.at[index, "Admission Page"] = str(
            pages.get("admission", "")
        )

        self.df.at[index, "About Page"] = str(
            pages.get("about", "")
        )

        self.df.at[index, "Faculty Page"] = str(
            pages.get("faculty", "")
        )

        self.df.at[index, "Directory Page"] = str(
            pages.get("directory", "")
        )

        self.df.at[index, "Office Page"] = str(
            pages.get("office", "")
        )

        self.df.at[index, "Administration Page"] = str(
            pages.get("administration", "")
        )

        # -------------------------
        # Status
        # -------------------------

        self.df.at[index, "Status"] = (
            "SUCCESS" if verified else "FAILED"
        )

    def save(self):

        os.makedirs(
            os.path.dirname(self.output_file),
            exist_ok=True
        )

        self.df.to_excel(
            self.output_file,
            index=False
        )

        print(f"\nSaved -> {self.output_file}")