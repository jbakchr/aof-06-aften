letter = input("Indtast et enkelt bogstav: ").lower()

if letter in "aeiou":
    print(f"{letter} er en vokal.")
else:
    print(f"{letter} er en konsonant.")
