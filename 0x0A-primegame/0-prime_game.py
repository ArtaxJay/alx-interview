#!/usr/bin/python3
"""
Prime Game Module

This module contains the implementation of a prime number-based game
between two players: Maria and Ben. The game involves removing prime numbers
and their multiples from a set of integers.

The winner of each round is determined based on who cannot make a move.
This module includes a function to determine the overall winner after
multiple rounds.

Functions:
    isWinner(x, nums): Determines the winner of the game based on rounds.
"""


def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


def calculate_wins(nums):
    """
    Precompute the number of prime numbers up to each number in nums.

    Args:
        nums (list): List of integers representing the rounds.

    Returns:
        list: Cumulative count of primes up to the largest number in nums.
    """
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_count = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes:
            prime_count[i] += 1

    return prime_count


def isWinner(x, nums):
    """
    Determine the overall winner of the game after x rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (list): List of integers representing the rounds.

    Returns:
        str: The name of the player who won the most rounds ("Maria" or "Ben"),
             or None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None

    prime_count = calculate_wins(nums)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
