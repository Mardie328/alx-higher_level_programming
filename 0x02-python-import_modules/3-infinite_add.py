#!/usr/bin/python3
import sys

argc = len(sys.argv)
total_sum = 0

# Calculate the sum of all arguments
for i in range(1, argc):
    total_sum += int(sys.argv[i])

# Print the result
print(total_sum)
