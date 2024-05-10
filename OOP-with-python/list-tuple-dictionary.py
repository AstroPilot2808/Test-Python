def main(): 
    student = get_student()
    if student[0] == "Padma":
        print("wrong info dumbo")
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")

    # This is a list (mutable)
    return [name, house]

    # This is a tuple (immutable)
    return (name, house)

    # This is a dictionary (mutable)
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()