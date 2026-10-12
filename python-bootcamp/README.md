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
├── samples/           # sample data provided by the instructor
│   └── tasks.csv  tasks_bad.csv
└── tests/             # tests provided by the instructor
    ├── conftest.py
    └── test_w1.py  test_w2.py  test_w3.py
```

`tests/` and `samples/` are copied unchanged from the instructor's
[public_materials/python-bootcamp](https://github.com/CSC10014-at-fit-hcmus/public_materials/tree/main/python-bootcamp).
Do not edit them.

## Team

| No. | GitHub | Folder | W1-4 variant | Reviewer (rotation) |
|-----|--------|--------|--------------|---------------------|
| 1 | @NewFace819 | `newface819` | binary search | Member 2 |
| 2 | @… | `…` | insertion sort | Member 3 |
| 3 | @… | `…` | matrix transpose | Member 4 |
| 4 | @… | `…` | sieve of Eratosthenes | Member 5 |
| 5 | @… | `…` | greatest common divisor (Euclid) | Member 1 |

We have five members, so Member 5 gets an extra W1-4 variant (allowed for teams with more than four
members). The instructor's tests only cover variants 1–4, so Member 5 also writes at least three tests
for `gcd` in `members/<folder>/w1/test_translate.py`.

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

## Week 1 file and function names

The tests import `members.<your_folder>.w1.<module>`, so these names must match exactly.

| Exercise | File in `members/<your_folder>/w1/` | Functions |
|----------|-------------------------------------|-----------|
| W1-1 | `grades.py` | `summary(scores)` |
| W1-2 | `text_tools.py` | `word_count(text)`, `top_k(text, k)` |
| W1-3 | `rules.py` | `can_register_thesis(credits, gpa)`, `missing(credits, gpa)` |
| W1-4 | `translate.py` | Member 1 `binary_search(a, key)`, 2 `insertion_sort(xs)`, 3 `transpose(m)`, 4 `primes_up_to(n)`, 5 `gcd(a, b)` — plus a docstring |
| W1-5 | `timetable.py` | `by_day(pairs)` |

## How to run the tests

Install the tools once:

```bash
pip install pytest ruff
```

Test your own folder while you work. Without `--member` every test is skipped, and `--variant`
(your member number, used by W1-4) defaults to 1:

```bash
pytest -q python-bootcamp/tests/test_w1.py --member <your_folder> --variant <your_number>
```

Member 5: the instructor's W1-4 test has no variant 5, so skip it and run your own tests instead:

```bash
pytest -q python-bootcamp/tests/test_w1.py --member <your_folder> --variant 5 -k "not test_w1_4"
pytest -q python-bootcamp/members/<your_folder>/w1
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
