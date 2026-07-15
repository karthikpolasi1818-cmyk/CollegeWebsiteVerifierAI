"""
search/search_manager.py

DuckDuckGo Search Manager
"""

from search.duckduckgo_provider import DuckDuckGoProvider
from search.result_filter import ResultFilter


class SearchManager:

    def __init__(self):

        self.provider = DuckDuckGoProvider()

    def search(self, college):

        queries = [

            f"{college} official website",

            f"{college} contact",

            f"{college} admission",

            f'"{college}"',

            college

        ]

        all_results = []
        seen = set()

        for query in queries:

            print(f"Searching DuckDuckGo : {query}")

            try:

                results = self.provider.search(query)

                for result in results:

                    if result.url not in seen:

                        seen.add(result.url)

                        all_results.append(result)

            except Exception as e:

                print(f"DuckDuckGo Error : {e}")

        all_results = ResultFilter.filter(all_results)

        print(f"\nTotal Results : {len(all_results)}")

        return all_results