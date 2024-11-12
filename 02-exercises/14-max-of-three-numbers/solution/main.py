num1 = float(input("Indtast første nummer: "))
num2 = float(input("Indtast andet nummer: "))
num3 = float(input("Indtast tredje nummer: "))

if num1 >= num2 and num1 >= num3:
    print(f"Det første indtastede tal, {num1}, er størst")
elif num2 >= num1 and num2 >= num3:
    print(f"Det andet indtastede tal, {num2}, er størst")
else:
    print(f"Det tredje indtastede tal, {num3}, er størst")
