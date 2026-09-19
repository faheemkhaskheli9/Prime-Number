"""Two from-scratch primality-check implementations.

Both approaches are the ones already described in the top-level README:

- :func:`is_prime_by_odd_divisors` -- reject even numbers, then trial-divide
  by every odd candidate up to ``n // 2``.
- :func:`is_prime_by_known_primes` -- trial-divide only by primes up to
  ``sqrt(n)``, generated on the fly with a small sieve.
"""

from .checker import is_prime_by_known_primes, is_prime_by_odd_divisors

__all__ = ["is_prime_by_known_primes", "is_prime_by_odd_divisors"]
