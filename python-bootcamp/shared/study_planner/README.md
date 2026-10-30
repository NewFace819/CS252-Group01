# study_planner

The team's study planner (T-W2, T-W3). It reads a CSV of tasks and prints how to spend tonight's
free hours, most urgent task first.

## Run it

From `python-bootcamp/`:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2
```

```
Tonight (2.0 h):
  1. Assignment ................... 1.5 h
  2. DS exam ...................... 0.5 h
```

| Argument | Meaning |
|----------|---------|
| `csv` | CSV file with the header `title,importance,effort_h,deadline` (deadline as `YYYY-MM-DD`, importance 1–5) |
| `--hours H` | hours free tonight (required) |
| `--today YYYY-MM-DD` | date to plan from; default is today. Pass it to get the same plan every day |
| `--strict` | fail instead of cutting the plan short when the tasks need more than `--hours` |

A walkthrough with every case is in [`docs/study-planner-demo.md`](../../../docs/study-planner-demo.md).

## How it works

`__main__.py` chains four modules. Each one only depends on `Task` and `Block` from
[`shared/contract.py`](../contract.py), which also states the exact behaviour of each step.

```
CSV file ──parse_csv──▶ list[Task] ──prioritise──▶ list[Task] ──allocate──▶ list[Block] ──render──▶ str
```

| Module | Function | What it does | Owner |
|--------|----------|--------------|-------|
| `parse.py` | `parse_csv(path)` | reads the CSV; a bad row raises `ValueError("line N: ...")`, header = line 1 | Đỗ Huy |
| `prioritise.py` | `prioritise(tasks, today)` | sorts by `importance / max(days_left, 1)`, highest first; ties go to the earlier deadline | Đức Huy |
| `allocate.py` | `allocate(tasks, hours)` | greedy in that order: each task gets `min(effort_h, hours left)` | Thông |
| `render.py` | `render(blocks)` | the `Tonight (H h):` plan, or `Nothing planned.` | THA Anh |
| `errors.py` | `check_feasible(tasks, hours)` | raises `InfeasiblePlan` for `--strict` | THA Anh |
| `__main__.py` | `main(argv)` | the command line above | Hải |

With `samples/tasks.csv` on 2026-10-26, the Assignment (importance 4, due in 1 day) scores 4.0 and
the DS exam (importance 5, due in 4 days) scores 1.25, so the Assignment goes first and the exam gets
the 0.5 h that is left.

## Errors and exit codes

Errors go to stderr as one `error: ...` line, never a traceback.

| Exit code | When | Example message |
|-----------|------|-----------------|
| 0 | a plan was printed (also `Nothing planned.` for `--hours 0`) | |
| 1 | missing or unreadable file | `error: file not found: missing.csv` |
| 1 | empty file, or a header with no tasks | `error: file is empty: ...`, `error: no tasks in ...` |
| 1 | bad row | `error: invalid CSV: line 3: invalid literal for int() with base 10: 'high'` |
| 1 | `--strict` and the tasks do not fit | `error: Plan requires 7.5 h but only 2.0 h are available (5.5 h short).` |
| 2 | bad arguments (argparse), e.g. no `--hours` or a bad `--today` | `study_planner: error: the following arguments are required: --hours` |

## Tests

```bash
pytest -q shared
```

Each module has its own `test_<module>.py`, which builds `Task` and `Block` objects directly instead
of calling another member's module. `test_errors.py` and `test_e2e.py` run the real
`python -m shared.study_planner` command.
