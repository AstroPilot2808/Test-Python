def main():
    hello()
    name = input("What is your name? ")
    print(hello(name))

def hello(to="world"): # Parameter with default value
    return f"hello, {to}"

if __name__ == "__main__":
    main()