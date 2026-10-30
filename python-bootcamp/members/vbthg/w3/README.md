# Week 3 — vbthg

- `dates.py`: ISO dates, tomorrow, `in N days`, and the next Mon–Sun.
  A weekday equal to today means seven days later. Invalid input raises `ValueError`.
- `log_stats.py`: counts and nearest-rank p95 per route. The slowest route is the
  highest p95, with alphabetical tie-breaking. Empty input returns empty maps and
  `slowest=None`. Negative and nonfinite latencies are rejected.
- `cli.py`: reuses my W2 loader/model, orders tasks by importance divided by at
  least one day remaining, then allocates the available hours greedily. Partial
  tasks are allowed; missing or invalid files return exit code 1.

From the repository root:

```console
pytest -q python-bootcamp/tests/test_w3.py --member vbthg
pytest -q python-bootcamp/members/vbthg/w3
ruff check python-bootcamp
```

From `python-bootcamp/`:

```console
python -m members.vbthg.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
```

## W3-4: Python compared with C++

`Counter` and `defaultdict` express grouping without manually initializing each key.
Type hints document expected values, while validation still happens at runtime.
`argparse` converts command-line arguments and reports usage errors before planning.
