people = [
    {"name": "Ahmed", "house": "South"},
    {"name": "Hussain", "house": "North"},
    {"name": "Mohammed", "house": "West"}
]

# def f(person):
#    return person["name"]

people.sort(key=lambda person: person["name"])

print(people)
