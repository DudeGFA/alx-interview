#!/usr/bin/python3
"""
    Contains function minOperations
"""


def minOperations(n: int) -> int:
    """
        calculates the fewest number of operations
        needed to result in exactly n H characters
        in a file
    """
    if (n <= 1):
        return 0
    res = 0
    i = 2
    while (i <= n):
        while(n % i == 0):
            res += i
            n = n / i
        i += 1
    return res
