#!/usr/bin/python3
"""
    contains function
    island_perimeter
"""


def island_perimeter(grid):
    """
        Args:
            grid (list of list of ints): describes an island
        returns: perimeter of the island described in grid
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 3
                try:
                    if grid[i - 1][j] == 1:
                        perimeter -= 1
                except IndexError:
                    pass
                try:
                    if grid[i][j - 1] == 1:
                        perimeter -= 1
                except IndexError:
                    pass
    return perimeter + 1
