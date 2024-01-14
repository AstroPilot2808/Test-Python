from calculator import square

def main():
    test_square()

def test_square():
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")
    try:
        assert square(2) == 4
        assert square(3) == 9
    except AssertionError:
        print("Something went wrong bozo")
    # Will result in AssertionError if boolean expression is wrong
if __name__ == "__main__":
    main()