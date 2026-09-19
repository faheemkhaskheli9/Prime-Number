# Architecture Notes: Prime-Number

## Pipeline

```text
CLI args (n, --method) -> argparse -> checker function -> bool result -> stdout
                                        ^
                            (odd-divisors | known-primes)
```

There is no service, no persistence, and no network I/O: the whole project is
a single-process, pure-stdlib computation that takes one integer in and
prints one boolean-derived line out.

## Components

- **`src/prime_checker/checker.py`** -- the two primality-check
  implementations described in the root `README.md`:
  - `is_prime_by_odd_divisors(n)` -- rejects negatives/0/1 and even numbers
    (2 is the sole even prime), then trial-divides `n` by every odd
    candidate up to `n // 2`. This is method 1 from the README.
  - `is_prime_by_known_primes(n)` -- trial-divides `n` only by the primes up
    to `sqrt(n)`, generated on demand by a small internal sieve of
    Eratosthenes (`_sieve_primes_up_to`). This is method 2 from the README
    (checking against "the first N known primes" instead of every odd
    number) and is the asymptotically faster of the two.
  - Both functions share `_validate_int`, which raises `TypeError` on any
    non-`int` input (including `bool`, since `bool` is a subclass of `int`
    in Python) rather than silently coercing or misreporting.
- **`src/prime_checker/cli.py`** -- `argparse`-based entry point. Takes a
  required integer `n` and an optional `--method {known-primes,odd-divisors}`
  (default `known-primes`), calls the matching checker function, and prints
  `"<n> is prime|not prime (<method>)"`. Exposed as the `prime-check` console
  script (see `pyproject.toml`'s `[project.scripts]`).
- **`src/prime_checker/__main__.py`** -- lets the package run as
  `python -m prime_checker ...` without requiring installation.
- **`src/prime_checker/__init__.py`** -- re-exports both checker functions as
  the package's public API (`from prime_checker import is_prime_by_known_primes`).
- **`tests/test_checker.py`** -- parametrized correctness tests run against
  both methods: known primes, known non-primes (negatives, 0, 1, perfect
  squares), non-integer rejection, and a full agreement check against a
  trusted trial-division reference across `n` in `[-5, 300)`.
- **Legacy scripts** (`Prime Number Best Method.py`, `primenumbers.py` at the
  repo root) -- the original exploratory implementations that `src/prime_checker`
  was distilled from. Kept for history; not imported by the package or tests.

## Design Notes

- No configuration, no external services, no persistence layer -- `configs/`,
  `assets/`, and `docker/` exist for scaffold consistency with the rest of the
  portfolio, not because this project currently needs them.
- The package has zero runtime dependencies (stdlib only); `numpy`/`pandas`/
  `matplotlib` in `requirements.txt` are only used by the legacy root scripts.
