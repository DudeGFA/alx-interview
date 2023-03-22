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

    count = sys.maxsize

    for i in range(0, len(coins)):
        if (coins[i] <= total):
            prev_count = makeChange(coins, total - coins[i])
            if (prev_count + 1 < count and prev_count != sys.maxsize):
                count = prev_count + 1

    return count
