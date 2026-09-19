"""Primality checks for the two methods described in the README.

Method 1 (``is_prime_by_odd_divisors``): reject 0/1/negatives and even
numbers outright (only 2 is an even prime), then trial-divide by every odd
candidate up to ``n // 2``.

Method 2 (``is_prime_by_known_primes``): trial-divide only by the primes up
to ``sqrt(n)`` -- the README's observation that you only need "the first N
known primes" rather than every odd number. The needed primes are generated
on the fly with a small sieve.

Both functions raise ``TypeError`` on non-integer input rather than failing
silently or coercing -- an explicit input either is or isn't a whole number,
and treating e.g. ``3.5`` as prime/not-prime would be a silent wrong answer.
"""

from __future__ import annotations

import math


def _validate_int(n: object) -> int:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"n must be an int, got {type(n).__name__}: {n!r}")
    return n


def is_prime_by_odd_divisors(n: int) -> bool:
    """README method 1: odd/even check, then trial division by odds <= n/2."""
    n = _validate_int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for candidate in range(3, n // 2 + 1, 2):
        if n % candidate == 0:
            return False
    return True


def _sieve_primes_up_to(limit: int) -> list[int]:
    """Primes in ``[2, limit]`` via a simple sieve of Eratosthenes."""
    if limit < 2:
        return []
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for candidate in range(2, math.isqrt(limit) + 1):
        if is_prime[candidate]:
            for multiple in range(candidate * candidate, limit + 1, candidate):
                is_prime[multiple] = 0
    return [i for i, flag in enumerate(is_prime) if flag]


def is_prime_by_known_primes(n: int) -> bool:
    """README method 2: divide only by already-known primes up to sqrt(n)."""
    n = _validate_int(n)
    if n < 2:
        return False
    for prime in _sieve_primes_up_to(math.isqrt(n)):
        if n % prime == 0:
            return False
    return True
