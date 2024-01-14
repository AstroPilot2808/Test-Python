def main():
    print_column(3)
    print_row(4)
    print_rectangle(4,3)
    print_square(7)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_rectangle(height, width):
    for _ in range(height):
            print("*" * width)

def print_square(length):
    print_rectangle(length, length)

main()