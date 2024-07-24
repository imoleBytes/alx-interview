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
        pascal.append(coeficients(i))

    return pascal


def coeficients(num: int) -> list:
    coefs = []

    for k in range(0, num + 1):
        coefs.append(comb(num, k))
    return coefs


if __name__ == "__main__":
    print(pascal_triangle(5))
