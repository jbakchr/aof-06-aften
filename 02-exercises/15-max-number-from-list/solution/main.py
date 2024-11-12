numbers = [
    51,
    88,
    66,
    11,
    39,
    54,
    36,
    28,
    21,
    84,
    75,
    20,
    55,
    47,
    42,
    92,
    73,
    14,
    50,
    25,
]

max_number = 0

for number in numbers:
    if number > max_number:
        max_number = number

print(f"Det største tal i listen er: {max_number}")
