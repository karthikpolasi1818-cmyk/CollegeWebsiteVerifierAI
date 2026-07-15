from search.search_manager import SearchManager

search = SearchManager()

results = search.search("IIT Hyderabad")

for i, r in enumerate(results, 1):
    print("=" * 80)
    print(i)
    print(r.title)
    print(r.url)