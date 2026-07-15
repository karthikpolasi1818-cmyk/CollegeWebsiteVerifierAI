from ddgs import DDGS

with DDGS() as ddgs:
    results = ddgs.text("IIT Hyderabad official website", max_results=5)

    for r in results:
        print(r)
        print("-" * 80)