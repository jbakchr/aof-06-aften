"""
Recap fra 5. aften
"""

# Eksempel 1 - datastrukturen 'list'
likes = ["lasagna", "cabonara", "beer", "chips", "coca cola"]

beer = likes[2]

likes[4] = "wine"

likes.append("red steak")
likes.insert(1, "cheese")


# Eksempel 2 - datastrukturen 'tuple'
fruits = ("apples", "bananas", "pears", "grapes", "strawberries", "bananas")

pears = fruits[2]

num_of_bananas = fruits.count("bananas")
index_of_grapes = fruits.index("grapes")


# Eksempel 3 - datastrukturen 'set'
bands = {
    "The Beatles",
    "The Rolling Stones",
    "The Beatles",
    "Pink Floyd",
    "The Beatles",
}

bands.add("The Who")

same_bands = bands.intersection({"The Beatles", "Korn", "Aqua"})
print(same_bands)
