"""Correctness tests for both README primality-check methods.

Covers known primes, known non-primes (including negatives, 0, 1, and
perfect squares like 9/49), the boundary case n=2, and rejection of
non-integer input.
"""

import pytest

from prime_checker.checker import is_prime_by_known_primes, is_prime_by_odd_divisors

CHECKS = pytest.mark.parametrize(
    "check", [is_prime_by_odd_divisors, is_prime_by_known_primes]
)

KNOWN_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 97, 101, 997, 7919]
KNOWN_NON_PRIMES = [-13, -1, 0, 1, 4, 6, 8, 9, 15, 49, 100, 999, 1024]


@CHECKS
@pytest.mark.parametrize("n", KNOWN_PRIMES)
def test_known_primes_are_reported_prime(check, n):
    assert check(n) is True


@CHECKS
@pytest.mark.parametrize("n", KNOWN_NON_PRIMES)
def test_known_non_primes_are_reported_not_prime(check, n):
    assert check(n) is False


@CHECKS
def test_rejects_non_integer_input(check):
    with pytest.raises(TypeError):
        check(3.5)
    with pytest.raises(TypeError):
        check("7")
    with pytest.raises(TypeError):
        check(None)


@CHECKS
def test_agrees_across_a_range(check):
    # Both methods must agree with a trusted reference (trial division up to
    # sqrt(n)) across a contiguous range, not just the hand-picked lists above.
    for n in range(-5, 300):
        expected = n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))
        assert check(n) is expected, f"mismatch at n={n}"
