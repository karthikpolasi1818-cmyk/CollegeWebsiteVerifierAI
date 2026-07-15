from verifier.rule_verifier import RuleVerifier

sample = {
    "website": "https://www.iith.ac.in/",
    "title": "Home | IIT Hyderabad",
    "social": {
        "linkedin": "https://linkedin.com/school/iithyderabad",
        "instagram": "https://instagram.com/iithyderabad",
        "facebook": "https://facebook.com/iithyderabad",
        "twitter": "https://twitter.com/IITHyderabad",
        "youtube": "https://youtube.com/@IITHyderabad",
    },
    "emails": [
        "office.registrar@iith.ac.in"
    ],
    "phones": [
        "+91-40-23016999"
    ],
    "pages": {
        "admission": "https://www.iith.ac.in/academics/",
        "contact": "https://www.iith.ac.in/emergency_contacts/",
        "faculty": "https://www.iith.ac.in/people/faculty/",
        "career": "https://www.iith.ac.in/careers/",
        "directory": "https://www.iith.ac.in/about/directory/",
        "about": "https://www.iith.ac.in/about/",
    }
}

verifier = RuleVerifier()

print(verifier.verify("IIT Hyderabad", sample))