def main():
    hello()
    name = input("What is your name? ")
    hello(name)

def hello(to="world"): # Parameter with default value
    print("hello," , to)

main()