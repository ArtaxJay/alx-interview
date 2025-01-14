#!/usr/bin/python3
"""
0x08. Making Change
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total.
    If the total cannot be met, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins
    # needed to make change for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make 0 total

    # For each coin,
    # update the minimum coins needed for each amount up to total
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the value for the total is still inf,
    # return -1 as it's impossible to make change
    return dp[total] if dp[total] != float('inf') else -1
