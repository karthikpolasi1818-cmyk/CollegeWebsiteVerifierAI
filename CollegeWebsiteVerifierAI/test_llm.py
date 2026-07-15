from verifier.llm_verifier import LLMVerifier

candidate = {
    "website": "https://www.iith.ac.in/",
    "title": "Home | IIT Hyderabad",
    "social": {
        "linkedin": "https://www.linkedin.com/school/iithyderabad/",
        "instagram": "https://www.instagram.com/iithyderabad/",
        "facebook": "https://www.facebook.com/iithyderabad/",
        "twitter": "https://twitter.com/IITHyderabad",
        "youtube": "https://www.youtube.com/@IITHyderabad"
    },
    "emails": [
        "office.registrar@iith.ac.in",
        "dean.acad@iith.ac.in"
    ],
    "phones": [
        "+91-40-23016999"
    ]
}

verifier = LLMVerifier()

result = verifier.verify(
    "IIT Hyderabad",
    candidate
)

print(result)