"""Example: using prime_checker as a library, not just via the CLI.

Run from the repo root with the package importable (e.g. after
``pip install -e .`` or with ``PYTHONPATH=src``):

    python examples/check_number.py
"""

from __future__ import annotations

from prime_checker import is_prime_by_known_primes, is_prime_by_odd_divisors

if __name__ == "__main__":
    numbers = [2, 15, 17, 97, 100, 7919]

    for n in numbers:
        fast = is_prime_by_known_primes(n)
        slow = is_prime_by_odd_divisors(n)
        assert fast == slow, f"methods disagree on {n}"
        print(f"{n:>6} -> {'prime' if fast else 'not prime'}")
