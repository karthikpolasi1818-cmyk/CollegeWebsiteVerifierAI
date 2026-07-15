class SocialExtractor:

    SOCIAL_DOMAINS = {
        "linkedin": "linkedin.com",
        "instagram": "instagram.com",
        "facebook": "facebook.com",
        "twitter": "twitter.com",
        "x": "x.com",
        "youtube": "youtube.com",
        "t.me": "t.me",
        "telegram": "telegram.me",
        "whatsapp": "wa.me",
    }

    @staticmethod
    def extract(links):

        social = {
            "linkedin": "",
            "instagram": "",
            "facebook": "",
            "twitter": "",
            "youtube": "",
            "telegram": "",
            "whatsapp": ""
        }

        for link in links:

            url = link.lower()

            if "linkedin.com" in url:
                social["linkedin"] = link

            elif "instagram.com" in url:
                social["instagram"] = link

            elif "facebook.com" in url:
                social["facebook"] = link

            elif "twitter.com" in url or "x.com" in url:
                social["twitter"] = link

            elif "youtube.com" in url:
                social["youtube"] = link

            elif "t.me" in url or "telegram.me" in url:
                social["telegram"] = link

            elif "wa.me" in url:
                social["whatsapp"] = link

        return social