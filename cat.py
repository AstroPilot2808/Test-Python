# i = 0
# while i < 3:
#     print("meow")
#     i+=1

# for _ in range(3):
#     print("meow") # range(3) returns a list 0,1,2. _ is an unecessary variable (so we use "_" as Python convention)

# print("meow\n" * 3, end="") # String Concatenation through multiplication
# # end = "" to stop from going to next line

# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break

# # OR ...

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

def main():
    meow(get_number())

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    
    while True:
        n = int(input("Pick any number "))
        if n > 0:
            return n

main()