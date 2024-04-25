#!/usr/bin/python3
"""
Minimum operations to archieve a certain number of characters.
"""


def minOperations(n):
    """Returns the minimum operations to archieve n characters."""
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(n // i) + i
        return n


if __name__ == "__main__":
    test_cases = [4, 12]
    for n in test_cases:
    	print(
    	    "Min # of operations to reach {} char: {}".format(n, minOperations(n))
    	        )
