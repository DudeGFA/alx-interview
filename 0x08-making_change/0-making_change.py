#!/usr/bin/python3
"""
    Contains function makeChange
"""
import sys


def makeChange(coins, total):
    """
        Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given amount total.
        Arg:
            coins (int): list of the values of the coins
                            in your possession
            total (int): Amount to be changed
        Returns:
            fewest number of coins needed to meet total
    """
    if (total == 0):
        return 0
    table = [0 for i in range(total + 1)]

    table[0] = 0

    for i in range(1, total + 1):
        table[i] = sys.maxsize

    for i in range(1, total + 1):

        for j in range(len(coins)):
            if (coins[j] <= i):
                prev_count = table[i - coins[j]]
                if (prev_count != sys.maxsize and prev_count + 1 < table[i]):
                    table[i] = prev_count + 1
    if (table[total] == sys.maxsize):
        return -1
    return table[total]
