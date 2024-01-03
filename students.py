with open("students.csv") as file:
    for line in file:
        name, house = line.split(",")
        print(f"Hi, My name is {name.rstrip()}. And, I live in {house.rstrip()}.")