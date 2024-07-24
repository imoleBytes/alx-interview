#!/usr/bin/python3
"""Module contains pascal_triangle fnction"""
from math import comb


def pascal_triangle(n: int) -> list:
    """
    Args:
      n: integer
    return:
      a list of list of pascal triangle
    """
    if n <= 0:
        return []
    pascal = []

    for i in range(0, n):
        pascal.append([comb(i, k) for k in range(0, i + 1)])

    return pascal
