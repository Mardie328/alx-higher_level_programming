#!/usr/bin/python3
import sys

# Get the number of arguments
argc = len(sys.argv) - 1

# Get the list of arguments
argv = sys.argv[1:]

# Print the header
print("{} argument{}:".format(argc, "s" if argc != 1 else ""))

# Print each argument and its position
for i in range(argc):
    position = i + 1
    argument = argv[i]
    print("{}: {}".format(position, argument))
