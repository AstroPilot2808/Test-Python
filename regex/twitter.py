import re

url = input("What's your Twitter Username? ").strip()

if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(3)}")

# ":=" is a relatively new operator in Python. It is iff (if and only if)
# It assigns a value to "matches" if re.search() returns true. It checks for boolean value and assignment
# in a single line.