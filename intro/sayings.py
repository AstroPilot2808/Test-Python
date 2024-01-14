def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

def main():
    hello("ajay")
    goodbye("aja")


# This condition checks from where this program is run. If sayings.py is run directly from command line, main() will be called.
# However, if sayings.py is imported elsewhere, main() does NOT run because __name__ != __main__
if __name__ == "__main__":
    main()