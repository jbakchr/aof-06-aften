num = int(input("Indtast et tal: "))

if num % 2 == 0 and num % 3 == 0:
    print("Tallet er deleligt med både 2 og 3.")
elif num % 2 == 0:
    print("Tallet er kun deleligt med 2.")
elif num % 3 == 0:
    print("Tallet er kun deleligt med 3.")
else:
    print("Tallet er hverken deleligt med 2 eller 3")
