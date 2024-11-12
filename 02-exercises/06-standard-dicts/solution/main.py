new_employees = ["Mads", "Emma", "Mikkel"]
defaults = {"title": "Developer", "salary": 8000}

res = dict.fromkeys(new_employees, defaults)
print(res)
