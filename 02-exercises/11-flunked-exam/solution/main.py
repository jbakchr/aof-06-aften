students = [
    {"name": "Mikkel", "result": "passed"},
    {"name": "Jonas", "result": "flunked"},
    {"name": "Emma", "result": "passed"},
    {"name": "Johanne", "result": "passed"},
    {"name": "Amalie", "result": "flUnKEd"},
    {"name": "Peter", "result": "pased"},
    {"name": "Søren", "result": "pased"},
    {"name": "Morten", "result": "flUnked"},
    {"name": "Gitte", "result": "passed"},
    {"name": "Henrik", "result": "passed"},
]

flunked_students = 0

for student in students:
    if student["result"].lower() == "flunked":
        flunked_students += 1

print(
    f"{flunked_students / len(students) * 100} % af studenterne bestod ikke deres tyskeksamen"
)
