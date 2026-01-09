import sys

def is_prime(n):
    """
    Determines if a number n is prime, composite, or neither using a
    deterministic Miller-Rabin primality test.
    """
    if n == 1:
        return "NEITHER"
    if n == 2 or n == 3:
        return "PRIME"
    if n % 2 == 0 or n % 3 == 0:
        return "COMPOSITE"
    if n < 25: # For 5, 7, 11, 13, 17, 19, 23
        return "PRIME"