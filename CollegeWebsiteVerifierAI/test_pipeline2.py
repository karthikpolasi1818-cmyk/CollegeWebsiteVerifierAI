from pipeline import Pipeline

pipeline = Pipeline()

result = pipeline.process(
    "IIT Hyderabad"
)

print()

print("=" * 80)

for key, value in result.items():

    print(key)

    print(value)

    print()