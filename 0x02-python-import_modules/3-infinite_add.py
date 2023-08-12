#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    total_sum = 0

    # Calculate the sum of all arguments
    for i in range(1, argc):
        total_sum += int(sys.argv[i])

    print(total_sum)
