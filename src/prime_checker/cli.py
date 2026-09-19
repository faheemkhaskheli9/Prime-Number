"""Command-line entry point.

Usage::

    python -m prime_checker 97
    python -m prime_checker 97 --method odd-divisors
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from .checker import is_prime_by_known_primes, is_prime_by_odd_divisors

_METHODS = {
    "known-primes": is_prime_by_known_primes,
    "odd-divisors": is_prime_by_odd_divisors,
}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="prime_checker",
        description="Check whether a number is prime, using either of the "
        "two methods described in the README.",
    )
    parser.add_argument("n", type=int, help="the integer to check")
    parser.add_argument(
        "--method",
        choices=sorted(_METHODS),
        default="known-primes",
        help="which approach to use (default: known-primes)",
    )
    args = parser.parse_args(argv)

    check = _METHODS[args.method]
    result = check(args.n)
    print(f"{args.n} is {'prime' if result else 'not prime'} ({args.method})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
