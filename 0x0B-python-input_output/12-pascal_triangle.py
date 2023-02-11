#!/usr/bin/python3
"""implements the pascal triangle of n"""


def pascal_triangle(n):
    """Defines the Pascal's triangle
    Args:
        n (int): number of rows
    Return:
        Pascal's triangle or an empty list
    """
    if n <= 0:
        return []
    result = []
    current_row = [1]
    result.append(current_row)
    for i in range(1, n):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            current_row.append(previous_row[j-1] + previous_row[j])
        current_row.append(1)
        result.append(current_row)
    return result
