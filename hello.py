# Ask user for their name and remove whitespace from str and capitalize
name = input("What is your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")

# Without 'f' {name} will be printed as a literal. 'f' tells the print function to format the string.