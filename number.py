def get_int(message):
    while True:
        try:
            return int(input(message))
        except:
            pass


def main():
    x = get_int("Type a number ")
    print(f"x is {x}")

main() 