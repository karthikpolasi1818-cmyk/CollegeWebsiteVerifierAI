"""
pipeline.py

Complete College Website Verification Pipeline
"""

import time

from search.search_manager import SearchManager
from search.website_ranker import WebsiteRanker
from search.organization_matcher import OrganizationMatcher

from crawler.crawler import SmartCrawler
from crawler.multi_page_crawler import MultiPageCrawler
from crawler.extractor_manager import ExtractorManager

from verifier.rule_verifier import RuleVerifier


class Pipeline:

    def __init__(self):
        self.search = SearchManager()
        self.crawler = SmartCrawler()
        self.multi = MultiPageCrawler()
        self.extractor = ExtractorManager()
        self.verifier = RuleVerifier()

    def empty_result(self):
        return {
            "website": "",
            "title": "",
            "social": {},
            "emails": [],
            "phones": [],
            "addresses": [],
            "pages": {},
            "verified": False,
            "confidence": 0,
        }

    def process(self, college):

        print("\n" + "=" * 80)
        print(f"Searching : {college}")
        print("=" * 80)

        try:
            print("STEP 1 : Searching...")
            results = self.search.search(college)
        except Exception as e:
            print(f"Search Failed : {e}")
            return self.empty_result()

        if not results:
            print("No Search Results")
            return self.empty_result()

        print(f"Found {len(results)} search results")

        print("STEP 2 : Ranking Results")
        ranked = WebsiteRanker.rank(results, college)

        if not ranked:
            print("No Ranked Results")
            return self.empty_result()

        for candidate_no, (score, result) in enumerate(ranked[:5], start=1):

            print("\n" + "-" * 60)
            print(f"Candidate {candidate_no}")
            print(f"Score    : {score:.2f}")
            print(f"Title    : {result.title}")
            print(f"Website  : {result.url}")
            print("-" * 60)

            if score <= 0:
                print("Rejected (score <= 0)")
                continue

            try:
                org_score = OrganizationMatcher.score(college, result.title)
                print(f"Organization Match : {org_score:.2f}")

                if org_score < 80:
                    print("Rejected (organization mismatch)")
                    continue

                print("STEP 3 : Crawling Homepage")
                t = time.time()
                homepage = self.crawler.crawl(result.url)
                print(f"Homepage Loaded ({time.time()-t:.2f}s)")

                if not homepage.get("title"):
                    print("Homepage Empty")
                    continue

                print("STEP 4 : Crawling Important Pages")
                t = time.time()
                pages = self.multi.crawl(homepage["important_pages"])
                print(f"{len(pages)} Pages Crawled ({time.time()-t:.2f}s)")

                print("STEP 5 : Extracting Data")
                t = time.time()
                extracted = self.extractor.extract(pages)
                print(f"Extraction Finished ({time.time()-t:.2f}s)")

                data = {
                    "website": result.url,
                    "title": homepage["title"],
                    "social": homepage["social"],
                    "emails": extracted.get("emails", []),
                    "phones": extracted.get("phones", []),
                    "addresses": extracted.get("addresses", []),
                    "pages": homepage["important_pages"],
                }

                print("STEP 6 : Verifying")
                verification = self.verifier.verify(college, data)
                data.update(verification)

                print(f"Verified   : {data['verified']}")
                print(f"Confidence : {data['confidence']}")

                if data["verified"]:
                    print("✓ Candidate Accepted")
                    return data

                print("✗ Candidate Rejected. Trying next candidate...")

            except Exception as e:
                print(f"Candidate Failed : {e}")
                continue

        print("No verified website found.")
        return self.empty_result()
