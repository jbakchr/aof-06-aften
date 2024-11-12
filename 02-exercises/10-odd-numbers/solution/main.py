numbers = [15, 49, 42, 1, 13, 55, 82, 94, 71, 85, 2, 15, 37, 38, 46, 35, 12, 66, 25, 17]

odds = 0

for number in numbers:
    if number % 2 != 0:
        odds += 1

print(f"Antallet af ulige tal er: {odds}")
