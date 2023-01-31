#!/usr/bin/python3
"""
Contains function pascal_triangle
"""


def pascal_triangle(n):
    """returns pascal's triangle with
        height n"""
    new_list = []
    list_of_list = []
    if n <= 0:
        return []
    for i in range(0, n):
        new_list.clear()
        if i == 0:
            new_list = [1]
        else:
            new_list.append(1)
            for j in range(1, i):
                new_list.append(list_of_list[i - 1]
                                [j - 1] + list_of_list[i - 1][j])
            new_list.append(1)
        list_of_list.append(list(new_list))
    return list_of_list
