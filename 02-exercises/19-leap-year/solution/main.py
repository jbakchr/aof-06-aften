year = int(input("Indtast et årstal: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} er et skud år.")
else:
    print(f"{year} er ikke et skudår.")
