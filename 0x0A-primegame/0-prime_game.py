#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i, prime in enumerate(is_prime) if prime]


def calculate_wins(nums):
    """Precompute the number of primes up to each number."""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_count = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes else 0)

    return prime_count


def isWinner(x, nums):
    """
    Determine the winner of the game.

    :param x: Number of rounds
    :param nums: Array of n for each round
    :return: Name of the player that won the most rounds or None
    """
    if not nums or x < 1:
        return None

    prime_count = calculate_wins(nums)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the count of primes up to n is odd,
        # Maria wins; otherwise, Ben wins.
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
