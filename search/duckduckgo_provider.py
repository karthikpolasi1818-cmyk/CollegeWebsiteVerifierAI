from ddgs import DDGS

from search.models.search_result import SearchResult


class DuckDuckGoProvider:

    def search(self, query: str):

        results = []

        with DDGS() as ddgs:
            for item in ddgs.text(query, max_results=10):

                results.append(
                    SearchResult(
                        title=item.get("title", ""),
                        url=item.get("href", ""),
                        snippet=item.get("body", ""),
                        provider="DDGS",
                    )
                )

        return results