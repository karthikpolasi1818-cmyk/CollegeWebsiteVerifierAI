from exporter.excel_writer import ExcelWriter

writer = ExcelWriter(
    "data/input.xlsx",
    "output/output.xlsx"
)

writer.create_columns()

writer.update(0, {
    "website": "https://www.iith.ac.in/",
    "confidence": 100,
    "verified": True,
    "social": {},
    "emails": ["office@iith.ac.in"],
    "phones": ["04012345678"],
    "addresses": ["Hyderabad"],
    "pages": {
        "contact": "https://www.iith.ac.in/contact_us/"
    }
})

writer.save()

print("Done")