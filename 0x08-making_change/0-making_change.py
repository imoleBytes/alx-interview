#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number
 of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of
 coin in the list
Your solution’s runtime will be evaluated in this task

"""
import sys


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1

    ####### tabili is table ########
    """
    if total <= 0:
        return 0
    tabili = [sys.maxsize for i in range(total + 1)]
    tabili[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = tabili[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < tabili[i]:
                    tabili[i] = subres + 1

    if tabili[total] == sys.maxsize:
        return -1
    return tabili[total]
