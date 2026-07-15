from search.google_provider import GoogleProvider

provider = GoogleProvider()

results = provider.search("IIT Hyderabad official website")

print(len(results))

for r in results[:5]:
    print(r.title)
    print(r.url)
    print("-" * 50)