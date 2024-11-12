weight = float(input("Indtast din vægt i kg: "))
height = float(input("Indtast din højde i meter: "))
bmi = weight / (height**2)

if bmi < 18.5:
    print("Din BMI er: undervægtig.")
elif bmi < 25:
    print("Din BMI er: normalvægtig.")
elif bmi < 30:
    print("Din BMI er: overvægtig.")
else:
    print("Din BMI er: svært overvægtig.")
