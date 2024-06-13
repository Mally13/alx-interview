#!/usr/bin/python3
"""
Contains function makeChange
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to
    meet a given amount
    """
    total_coins = 0
    val_calc = 0
    org_total = total
    if total <= 0:
        return total_coins
    while total > 0 and len(coins) > 0:
        coins_got = total // max(coins)
        total_coins = total_coins + coins_got
        val_calc += coins_got * max(coins)
        total = total % max(coins)
        coins.remove(max(coins))
    if val_calc == org_total:
        return total_coins
    return -1
