class PromptBuilder:

    @staticmethod
    def build(college, candidate):

        return f"""
You are verifying official college information.

College:
{college}

Candidate Website:
{candidate["website"]}

Page Title:
{candidate["title"]}

Social Links:
{candidate["social"]}

Emails:
{candidate["emails"]}

Phones:
{candidate["phones"]}

Task:

Return ONLY JSON.

{{
    "official": true,
    "confidence": 98,
    "reason": "...",
    "official_website": "...",
    "linkedin": "...",
    "facebook": "...",
    "instagram": "...",
    "twitter": "...",
    "youtube": "...",
    "official_email": "...",
    "official_phone": "..."
}}
"""