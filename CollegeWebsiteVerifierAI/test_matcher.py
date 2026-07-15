from search.organization_matcher import OrganizationMatcher

tests = [
    ("IIT Hyderabad", "Home | IIT Hyderabad"),
    ("IIT Hyderabad", "Home | IIIT Hyderabad"),
    ("NIT Warangal", "National Institute of Technology Warangal"),
    ("MIT Pune", "MIT-WPU"),
]

for college, title in tests:
    print(college)
    print(title)
    print("Score:", OrganizationMatcher.score(college, title))
    print("-" * 60)