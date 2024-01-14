import sys

# sys.argv is a list that takes in the elements passed while running python name.py

if len(sys.argv)<2:
    sys.exit("Too few argumenets")

for arg in sys.argv[1:]:
    print("MY name is", arg)
    