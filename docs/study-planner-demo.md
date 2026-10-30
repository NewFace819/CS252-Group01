# Study planner demo

A short run of `python -m shared.study_planner` (T-W3) from a fresh clone. Every command is run from
`python-bootcamp/` with `--today 2026-10-26`, so the output below is what you get on any day.
How the planner works is in [`shared/study_planner/README.md`](../python-bootcamp/shared/study_planner/README.md).

```bash
git clone https://github.com/NewFace819/CS252-Group01.git
cd CS252-Group01/python-bootcamp
```

## The sample file

`samples/tasks.csv`:

```
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

7.5 h of work in total. The Assignment is due tomorrow, so it comes first even though the exam
is more important.

## 1. Two hours tonight

```
$ python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26
Tonight (2.0 h):
  1. Assignment ................... 1.5 h
  2. DS exam ...................... 0.5 h
```

The Assignment gets all 1.5 h it needs and the exam gets the 0.5 h that is left. The plan is cut at
2 h and the command still succeeds (exit code 0).

## 2. Enough time for everything

```
$ python -m shared.study_planner samples/tasks.csv --hours 8 --today 2026-10-26
Tonight (7.5 h):
  1. Assignment ................... 1.5 h
  2. DS exam ...................... 6.0 h
```

The header shows the 7.5 h actually planned, not the 8 h available.

## 3. No time

```
$ python -m shared.study_planner samples/tasks.csv --hours 0 --today 2026-10-26
Nothing planned.
```

## 4. `--strict`: fail when it does not fit

```
$ python -m shared.study_planner samples/tasks.csv --hours 2 --today 2026-10-26 --strict
error: Plan requires 7.5 h but only 2.0 h are available (5.5 h short).
$ echo $?
1
```

## 5. Bad input

```
$ python -m shared.study_planner missing.csv --hours 2
error: file not found: missing.csv

$ python -m shared.study_planner samples/tasks_bad.csv --hours 2
error: invalid CSV: line 3: invalid literal for int() with base 10: 'high'

$ python -m shared.study_planner samples/tasks.csv
usage: study_planner [-h] --hours HOURS [--today TODAY] [--strict] csv
study_planner: error: the following arguments are required: --hours
```

The first two exit with code 1, the last with code 2 (argparse). `tasks_bad.csv` has `high` as the
importance on line 3 (the header is line 1).
