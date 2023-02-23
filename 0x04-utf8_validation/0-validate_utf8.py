#!/usr/bin/python3
"""
    Contains function validUTF8
"""


def validUTF8(data):
    """
         determines if a given data set
         represents a valid UTF-8 encoding.
    """
    n_byte = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        mask = 1 << 7
        if n_byte == 0:
            while mask & num:
                n_byte += 1
                mask = mask >> 1
            if n_byte == 0:
                continue
            if n_byte == 1 or n_byte > 4:
                return False
        else:
            if not (num & mask1 and not(num & mask2)):
                return False
        n_byte -= 1
    return n_byte == 0
