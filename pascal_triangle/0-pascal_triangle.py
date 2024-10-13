#!/usr/bin/python3
"""
Module: 0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n levels.

    Args:
        n (int): Number of levels in Pascal's triangle.

    Returns:
        List[List[int]]: Pascal's triangle as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle