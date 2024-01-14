import re

# -------Some symbols that "re" library takes-------
# .       any character except a newline
# *       0 or more repetitions
# +       1 or more repetitions
# ?       0 or 1 repetitions
# {m}     m repetitions
# {m,n}   m to n repetitions
# ^       matches the start of the string
# $       matches the end of the string or just before the newline at the end of the string
# []      set of characters
# [^]     complementing the set
# \d      decimal digit
# \D      not a decimal digit
# \s      whitespace characters
# \S      not a whitespace character
# \w      word character, as well as numbers and the underscore
# \W      not a word character
# A|B     either A or B
# (...)   a group
# (?:...) non-capturing version

email = input("What's your email? ").strip()

if re.search(r"^\w+@[a-zA-Z0-9_]+\.(edu|com|gov|net|org)$", email, re.IGNORECASE): # \ is used before a character to make sure that character is taken literally. 'r' is used to treat the pattern as "raw "
    # \w is the same this as the set of characters (alpha, numeric, and _)
    print("Valid")
else:
    print("Invalid")