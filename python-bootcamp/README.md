# Python Bootcamp (W1–W3)

Three weeks of Python homework, learned by comparison with C++ and submitted through this
repository (Section 18 of *Git & GitHub for Team Projects*).

| Week | Topics | Individual | Team | Milestone | Tag |
|------|--------|------------|------|-----------|-----|
| 1 | syntax, types, control flow, functions, lists, dicts, strings | W1-1 … W1-5 | T-W1: bootcamp folder + CI | `PY-W1` | `py-w1-done` |
| 2 | modules, files, CSV/JSON, exceptions, classes, dataclasses, pytest | W2-1 … W2-5 | T-W2: shared `Task` contract | `PY-W2` | `py-w2-done` |
| 3 | datetime, collections, typing, argparse, ruff, packaging | W3-1 … W3-4 | T-W3: `study_planner` CLI | `PY-W3` | `py-w3-done` |

## Layout

```
python-bootcamp/
├── README.md          # this file
├── PROGRESS.md        # one row per member per week (links to PRs)
├── members/
│   └── <your_folder>/ # one folder per member
│       ├── w1/  w2/  w3/
├── shared/            # team code (T-W2, T-W3)
│   ├── contract.py
│   └── study_planner/
└── tests/             # tests provided by the instructor
    ├── conftest.py
    └── test_w1.py  test_w2.py  test_w3.py
```

## Team

| No. | GitHub | Folder | W1-4 variant | Reviewer (rotation) |
|-----|--------|--------|--------------|---------------------|
| 1 | @NewFace819 | `newface819` | binary search | Member 2 |
| 2 | @… | `…` | insertion sort | Member 3 |
| 3 | @… | `…` | matrix transpose | Member 4 |
| 4 | @… | `…` | sieve of Eratosthenes | Member 1 |

## Rules

1. **Your folder only.** Individual work goes in `members/<your_folder>/wN/`. The folder name is
   your GitHub username in lower case, with hyphens replaced by underscores (`minh-nv` → `minh_nv`),
   because Python cannot import a module whose name contains a hyphen.
2. **One issue per week.** Open it with the *Python homework* template, label `python-hw` + `wN`,
   milestone `PY-WN`, and assign it to yourself.
3. **One branch per week:** `py/wN-<github-username>`, created from an up-to-date `main`.
4. **Commit after each exercise** — at least 5 commits per week, spread over several days:
   `feat(py-w1): W1-2 word counter`.
5. **Pull request** titled `py-wN: <username>`, with `Closes #<issue>` in the description, requesting
   your rotation reviewer. Merge only after approval and a green CI run.
6. **Update `PROGRESS.md`** with your row, in the same PR or a follow-up.
7. **Integrity and AI use.** Write the individual exercises yourself. AI may explain a concept or an
   error message; if you keep any AI-generated code, say so in the PR's "AI use" section and in
   `docs/ai-use-log.md`. You must be able to explain every line.

## How to run the tests

Install the tools once:

```bash
pip install pytest ruff
```

Test your own folder while you work (`--variant` is your member number, used by W1-4):

```bash
pytest -q python-bootcamp/tests/test_w1.py --member <your_folder> --variant <your_number>
```

Run what CI runs before you push:

```bash
ruff check python-bootcamp
pytest -q python-bootcamp
```

## Reviewing a teammate's PR

- Do the instructor's tests pass in CI?
- Is the code Pythonic (loops over items, comprehensions, f-strings), or C++ written in Python syntax?
- Are edge cases handled (empty input, wrong types, zero)?
- Are names clear, and are there docstrings?
- Leave at least **one Question, one Suggestion and one Praise**. Approve only when the tests pass
  and you understand the code.
