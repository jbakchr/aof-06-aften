dictator = {"name": "Guido", "age": 68, "title": "dictator"}

inverted_dict = {}

for key, value in dictator.items():
    inverted_dict[value] = key

print(inverted_dict)
