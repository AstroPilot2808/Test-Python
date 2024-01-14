# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names): # sorted returns a list alphabetically
#     print(f"hello, {name}")

# Now using File I/O ---------------------

# name = input("What's your name? ")

# with open("names.txt" , "a") as file: # "with" keyword is used to automatically open and close files
#     file.write(f"{name}\n")

with open("names.txt", "r") as file:
    for line in sorted(file, reverse=True):
        print(f"Welcome, {line.rstrip()}")