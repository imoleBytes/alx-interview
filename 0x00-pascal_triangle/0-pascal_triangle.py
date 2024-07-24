#!/usr/bin/python3
"""Module contains pascal_triangle fnction"""


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


def comb(n, k):
    """return the combination of n,k"""
    c = fact(n) // (fact(n-k) * fact(k))
    return c


def fact(n):
    """return n factorial"""
    if n <= 1:
        return 1
    return n * fact(n-1)
