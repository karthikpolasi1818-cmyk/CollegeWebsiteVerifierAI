"""
search/google_provider.py

Google Custom Search Provider
"""

import requests

from config import GOOGLE_API_KEY, GOOGLE_CSE_ID
from search.models.search_result import SearchResult


class GoogleProvider:

    SEARCH_URL = "https://www.googleapis.com/customsearch/v1"

    def search(self, query):

        if not GOOGLE_API_KEY:
            print("Google API Key Missing")
            return []

        if not GOOGLE_CSE_ID:
            print("Google CSE ID Missing")
            return []

        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CSE_ID,
            "q": query,
            "num": 10,
        }

        try:

            response = requests.get(
                self.SEARCH_URL,
                params=params,
                timeout=20
            )

            print("=" * 70)
            print("GOOGLE SEARCH")
            print("=" * 70)
            print(f"Query : {query}")
            print(f"Status: {response.status_code}")

            # Print Google error body if request failed
            if response.status_code != 200:
                print("\nGoogle Response:")
                print(response.text)
                response.raise_for_status()

            data = response.json()

        except requests.exceptions.HTTPError as e:

            print(f"\nHTTP Error : {e}")

            return []

        except requests.exceptions.Timeout:

            print("\nGoogle Search Timeout")

            return []

        except requests.exceptions.ConnectionError:

            print("\nInternet Connection Error")

            return []

        except Exception as e:

            print(f"\nGoogle Search Error : {e}")

            return []

        results = []

        for item in data.get("items", []):

            results.append(

                SearchResult(

                    title=item.get("title", "").strip(),

                    url=item.get("link", "").strip(),

                    snippet=item.get("snippet", "").strip(),

                    provider="Google"

                )

            )

        print(f"Google Results : {len(results)}")

        return results