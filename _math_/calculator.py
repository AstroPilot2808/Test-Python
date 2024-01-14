# w = float(input("What is X? "))
# y = float(input("What is Y? "))

# z = round(w/y)

# # This is how you format a number, AND add necessary commas. 
# print(f"{z:.3f}")

def main():
    x = input("What's x? ")
    print("x squared is", square(x))

def square(x):
    return x*x

if __name__ == "__main__":
    main()