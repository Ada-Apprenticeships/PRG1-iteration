colours = ["red", "green", "blue"]

for index, colour in enumerate(colours):
    print(f"{index}: {colour}")

print("---")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

print("---")

shortlist = ["Alice", "Bob"]

for name, age in zip(shortlist, ages):
    print(f"{name} is {age}")
