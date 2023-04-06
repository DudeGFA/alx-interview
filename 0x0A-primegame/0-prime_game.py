#!/usr/bin/python3
"""`
    Contains functions:
        isPrime: Returns true if a number is prime
                otherwise, false
        isWinner: Determines the winner in A prime game
"""


def isPrime(num):
    """
        Args:
            num (int): checks if this number is prime
        Returns:
            True if num is prime
            otherwise false
    """
    if num > 1:
        # Iterate from 2 to n / 2
        if num < 4:
            return True
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        return True
    return False


def isWinner(x, nums):
    """
        Args:
            x (int): no of rounds
                    prime game is
                    played
            num (list(int)): max value of
                            each series of numbers
                            in each round
        Returns:
            Winner of prime game if one exists
            otherwise None
    """
    if x is None or x == 0 or nums is None or nums == []:
        return None

    Ben = 0
    Maria = 0
    for idx in range(x):
        winner = 0
        num_range = [i for i in range(1, nums[idx] + 1)]
        num_copy = list(num_range)
        for j in num_range:
            if j in num_copy:
                if isPrime(j):
                    # print(str(j) + ' is prime!')
                    winner += 1
                    for no in list(num_copy):
                        if (no % j == 0):
                            # print(j, no)
                            # print(num_copy)
                            num_copy.remove(no)
                            # print(num_copy)
                # else:
                    # print(str(j) + ' is not prime!')
        if (winner % 2) == 0:
            Ben += 1
            # print('ben won round ', nums[idx])
        else:
            Maria += 1
            # print('maria won round ', nums[idx])
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
