#!/usr/bin/python3
"""
Minimum operations to archieve a certain number of characters.
"""


def minOperations(n):
    """Returns the minimum operations required to achieve n characters."""
    if n <= 1:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            return minOperations(n // i) + i
        i += 1
    return n

if __name__ == "__main__":
    test_cases = [4, 12]
    for n in test_cases:
        print(
        "Min # of operations to reach {} char: {}".format(n, minOperations(n))
            )

