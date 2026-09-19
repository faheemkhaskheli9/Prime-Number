# Evaluation Notes: Prime-Number

## Metrics

This project is evaluated on two axes:

- **Correctness** -- `tests/test_checker.py` checks both `is_prime_by_odd_divisors`
  and `is_prime_by_known_primes` against known primes, known non-primes, and a
  full agreement sweep against a trusted trial-division reference for every
  integer in `[-5, 300)`. A green `pytest` run is the pass/fail bar; there is
  no accuracy threshold below 100% for either method.
- **Loop-count / runtime characterization** -- the root `README.md` documents
  empirical trial-division-call counts for `is_prime_by_known_primes` at a few
  input sizes (e.g. up to 3,362 divisions for `n < 1000`). These are recorded
  here as they're re-measured, so regressions in the sieve or trial-division
  loop are visible over time.

## Reproducing Results

```bash
pip install -r requirements.txt
pytest tests/ -v
```

To re-measure loop counts for the runtime table below, instrument
`is_prime_by_known_primes`/`is_prime_by_odd_divisors` locally (e.g. wrap the
trial-division loop with a counter) and run it across the same `n` ranges
noted in the README.

## Result Log

| Date       | Config                          | Metric                  | Value      | Notes |
|------------|----------------------------------|--------------------------|------------|-------|
| 2026-09-19 | `pytest tests/` (Python 3.x)     | tests passed             | 58 / 58    | Full suite green after Phase 1 scaffold work (both methods, all parametrized cases) |
