# Lists (equivalent to Array in Java)

students = ["Hermione", "Harry", "Ron", "Draco"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])

houses = ["Gryffindor" , "Gryffindor" , "Gryffindor" , "Slytherin"]

student

# Dicts (equivalent to HashMap in Java)

dict_students = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
                 }

for student in dict_students:
    print(student, dict_students[student], sep=", ")

# Dictionaries within List

big_students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}

]

# Nested for loop

for person in big_students:
    for key in person:
        print(key, person[key])