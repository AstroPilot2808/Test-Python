import cowsay
import sys

# Importing custom functions that I made

from sayings import goodbye

if len(sys.argv) == 2:
    cowsay.trex  ("hello, "+sys.argv[1])

goodbye("universe")