# Python Bootcamp (W1–W3)

Three weeks of Python homework, learned by comparison with C++ and submitted through this
repository (Section 18 of *Git & GitHub for Team Projects*).

| Week | Topics | Individual | Team | Milestone | Tag |
|------|--------|------------|------|-----------|-----|
| 1 | syntax, types, control flow, functions, lists, dicts, strings | W1-1 … W1-5 | T-W1: bootcamp folder + CI | `PY-W1` | `py-w1-done` |
| 2 | modules, files, CSV/JSON, exceptions, classes, dataclasses, pytest | W2-1 … W2-5 | T-W2: shared `Task` contract | `PY-W2` | `py-w2-done` |
| 3 | datetime, collections, typing, argparse, ruff, packaging | W3-1 … W3-4 | T-W3: `study_planner` CLI | `PY-W3` | `py-w3-done` |

## Team and Week 1 assignments

The team leader assigns the T-W1 tasks and the W1-4 variants (Section 18.5). Every PR is reviewed by
the next member in the rotation.

| No. | Member | T-W1 team task (one PR) | W1-4 variant | Your PRs are reviewed by | You review |
|-----|--------|-------------------------|--------------|--------------------------|------------|
| 1 | Hải (leader) | `python-bootcamp/` structure + this README | `binary_search` | Đỗ Huy | THA Anh |
| 2 | Đỗ Huy | milestones `PY-W1/W2/W3`, labels, issue template | `insertion_sort` | Đức Huy | Hải |
| 3 | Đức Huy | CI: `.github/workflows/ci.yml` + `ruff.toml` | `transpose` | Thông | Đỗ Huy |
| 4 | Thông | `PROGRESS.md` + the instructor's `tests/` and `samples/` | `primes_up_to` | THA Anh | Đức Huy |
| 5 | THA Anh | PR template + `docs/ai-use-log.md` | `gcd` (Euclid) | Hải | Thông |

**T-W1 merge order:** Hải → Thông → Đỗ Huy and THA Anh (any order) → Đức Huy last, because CI needs the
instructor's tests to be in `main` first.

We have five members, so Member 5 gets an extra W1-4 variant (allowed for teams with more than four
members). The instructor's tests only cover variants 1–4, so THA Anh also writes at least three tests
for `gcd` in `members/<folder>/w1/test_translate.py`.

### GitHub usernames

Fill in your own line in your first PR. Keep the blank lines between entries: they let everyone edit
this list at the same time without merge conflicts.

- **1 · Hải:** @NewFace819 → `members/newface819/`

- **2 · Đỗ Huy:** @wiih0521 → `members/wiih0521/`

- **3 · Đức Huy:** @npdwuy → `members/npdwuy/`

- **4 · Thông:** @vbthg → `members/vbthg/`

- **5 · THA Anh:** @hoanganhtu0922 → `members/hoanganhtu0922/`

## Week 1 to-do (every member)

1. Accept the collaborator invite, and set `git config --global user.name` / `user.email` to your
   GitHub account so your commits count for you.
2. Do your **T-W1 team task** from the table above: one PR, reviewed by the member in your
   "reviewed by" column.
3. Open your homework issue: **New issue → Python homework**, labels `python-hw` + `w1`, milestone
   `PY-W1`, assigned to yourself.
4. From an up-to-date `main`, create your branch `py/w1-<github-username>`.
5. **Create your own folder** `members/<your_folder>/w1/` (add `w2/` and `w3/` in those weeks) and fill
   in your line under *GitHub usernames*.
6. Write W1-1 … W1-5 **yourself** in that folder. Commit after each exercise — at least 5 commits,
   spread over several days.
7. Run the tests (see below), push, and open the PR `py-w1: <username>` with `Closes #<issue>`.
8. Review the PR in your "You review" column.
9. After approval: merge, then add your row to `PROGRESS.md`.

Week 1 is done when all five `py-w1` PRs are merged with approval, CI is green, `PROGRESS.md` has five
rows, and Hải has pushed the tag `py-w1-done` (p. 61).

## Team and Week 2 assignments

Hải assigns the W2-4 testers and the T-W2 tasks (Section 18.6). Your tester writes the W2-4 tests for
your W1-4 function and also reviews your `py-w2` PR. No pair repeats a Week 1 review pair.

| No. | Member | W2-4: tests the W1-4 of | Your `py-w2` PR is reviewed by | T-W2 team task (own PR) | Your T-W2 PR is reviewed by |
|-----|--------|-------------------------|--------------------------------|-------------------------|-----------------------------|
| 1 | Hải (leader) | Thông — `primes_up_to` | Đức Huy | `shared/contract.py`; setup (this section, `pytest.ini`, CI) | all four (contract), Đỗ Huy (setup) |
| 2 | Đỗ Huy | THA Anh — `gcd` | Thông | `study_planner/parse.py` | Đức Huy |
| 3 | Đức Huy | Hải — `binary_search` | THA Anh | `study_planner/prioritise.py` | Thông |
| 4 | Thông | Đỗ Huy — `insertion_sort` | Hải | `study_planner/allocate.py` | THA Anh |
| 5 | THA Anh | Đức Huy — `transpose` | Đỗ Huy | `study_planner/render.py` | Hải |

Each module is reviewed by the member whose module uses its output; Hải reviews `render.py` because
Hải wires the modules together in T-W3.

**T-W2 merge order:** the setup PR first (CI needs `pytest.ini`), then the contract PR, approved by all
four other members, then the four module PRs in any order. The individual exercises do not need the
contract, so start them right away.

## Week 2 to-do (every member)

1. Open your homework issue: **New issue → Python homework**, title `py-w2: <username>`, labels
   `python-hw` + `w2`, milestone `PY-W2`, assigned to yourself.
2. Review and approve the contract PR as soon as it is open.
3. From an up-to-date `main`, create `py/w2-<github-username>` and write W2-1, W2-2, W2-3, W2-5 and
   W2-4 **yourself** in `members/<your_folder>/w2/`. Commit after each exercise — at least 5 commits,
   spread over several days.
4. Run the tests, push, and open the PR `py-w2: <username>` with `Closes #<issue>`, requesting the
   reviewer in your row. If your tester's W2-4 tests fail on your W1-4 code, answer in their PR: fix
   your code, or explain why the test is wrong.
5. After the contract is merged: from an up-to-date `main`, create `team/w2-<module>` (for example
   `team/w2-parse`), write your module and `shared/study_planner/test_<module>.py`, and open the PR
   `T-W2: <module>.py`. Build `Task` and `Block` objects directly in your tests; do not import a
   teammate's module.
6. Review the PRs assigned to you (at least one Question, one Suggestion and one Praise).
7. After your PRs are merged: pull `main`, then add your W2 row to `PROGRESS.md` (and any AI use to
   `docs/ai-use-log.md`) in a small follow-up PR. Keep these two files out of your `py-w2` PR: five
   people adding rows at the same time conflict.

Week 2 is done when all five `py-w2` PRs are merged with approval, the contract PR shows approvals from
all four other members, the four module PRs are merged with tests, CI is green, and Hải has pushed the
tag `py-w2-done` (p. 63). Deadline: Friday 22:00 (milestone `PY-W2`).

## Team and Week 3 assignments

Week 3 follows Section 18.7. The reviewer rotation is "Week C"; with five members we continue the
offsets used before (W1 = +1, W2 = +2, W3 = +3), so no pair repeats a Week 1 or Week 2 review pair.

| No. | Member | Your `py-w3` PR is reviewed by | You review |
|-----|--------|--------------------------------|------------|
| 1 | Hải (leader) | Thông | Đức Huy |
| 2 | Đỗ Huy | THA Anh | Thông |
| 3 | Đức Huy | Hải | THA Anh |
| 4 | Thông | Đỗ Huy | Hải |
| 5 | THA Anh | Đức Huy | Đỗ Huy |

### T-W3: integrate the study planner

Section 18.7 gives Member 1 the `__main__.py` task; the other tasks were drawn at random. Member 5 has
no task in the book (it lists four), so the render rounding fix is an extra. Each T-W3 PR is reviewed
by the next member in the rotation and titled `T-W3: <task>`.

| Task | Owner |
|------|-------|
| `shared/study_planner/__main__.py` calls `parse_csv → prioritise → allocate → render` | Hải |
| End-to-end test with a sample CSV | Thông |
| Error handling: missing file, empty file, infeasible plan (reuse `InfeasiblePlan`) | THA Anh |
| `shared/study_planner/README.md` and a short demo in `docs/` | Đức Huy |
| Extra: fix the `:.1f` rounding in `render.py` and remove the `xfail` | Đỗ Huy |

Merge order: `__main__.py` first, then the end-to-end test and error handling, then the README/demo and
the rounding fix. The CLI must run from a fresh clone:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2
```

## Week 3 to-do (every member)

1. Open your homework issue: **New issue → Python homework**, title `py-w3: <username>`, labels
   `python-hw` + `w3`, milestone `PY-W3`, assigned to yourself.
2. From an up-to-date `main`, create `py/w3-<github-username>` and write W3-1 … W3-4 **yourself** in
   `members/<your_folder>/w3/`. Commit after each exercise — at least 5 commits, spread over several days.
3. Run the tests, push, and open the PR `py-w3: <username>` with `Closes #<issue>`, requesting the
   reviewer in your row.
4. Do your T-W3 task from `main` on a branch `team/w3-<task>`, and review the PRs assigned to you (at
   least one Question, one Suggestion and one Praise).
5. After your PRs are merged: add your W3 row to `PROGRESS.md` (and any AI use to `docs/ai-use-log.md`)
   in a small follow-up PR, not in your `py-w3` PR.

| Exercise | File in `members/<your_folder>/w3/` | Contents |
|----------|-------------------------------------|----------|
| W3-1 | `dates.py` | `parse_due(text, today) -> date`: `2026-10-30`, `tomorrow`, `in 3 days`, weekday names like `Fri` (next occurrence); otherwise `ValueError` |
| W3-2 | `log_stats.py` | `analyse(pairs) -> dict` over `(route, latency_ms)`: `counts` (`Counter`), `p95` per route, `slowest` route |
| W3-3 | `cli.py` | `python -m members.<your_folder>.w3.cli tasks.csv --hours 2 [--today YYYY-MM-DD]`; exit code 1 with a clear message if the file is missing |
| W3-4 | all your bootcamp files | type hints on every function, `ruff check` clean, docstrings; three lines in the PR on the Python feature most different from C++ |

```bash
pytest -q python-bootcamp/tests/test_w3.py --member <your_folder>
```

Week 3 is done when all five `py-w3` PRs are merged with approval, the T-W3 PRs are merged, the CLI runs
from a fresh clone, the end-to-end test passes in CI, and Hải has pushed the tag `py-w3-done`
(p. 63).

## Layout

```
python-bootcamp/
├── README.md            # this file (Hải, T-W1)
├── PROGRESS.md          # one row per member per week (Thông, T-W1)
├── ruff.toml            # lint settings (Đức Huy, T-W1)
├── pytest.ini           # also collects W2-4 tests_for_*.py files (Hải, T-W2)
├── members/             # one folder per member: GitHub username, lower case, - → _
│   ├── newface819/      # Hải
│   │   └── w1/  w2/  w3/
│   └── <your_folder>/   # every other member creates their own in their W1 PR
├── shared/              # team code
│   ├── contract.py      # T-W2: agreed by everyone in one PR
│   └── study_planner/   # T-W2, T-W3: one module per member
├── samples/             # instructor's sample data (Thông, T-W1)
└── tests/               # instructor's tests (Thông, T-W1)
```

`tests/` and `samples/` are copied unchanged from the instructor's
[public_materials/python-bootcamp](https://github.com/CSC10014-at-fit-hcmus/public_materials/tree/main/python-bootcamp).
Do not edit them. Git does not store empty folders, so a folder with nothing in it yet holds an empty
`.gitkeep` file.

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
| W1-4 | `translate.py` | your variant from the team table — plus a docstring |
| W1-5 | `timetable.py` | `by_day(pairs)` |

## Week 2 file and function names

The tests import `members.<your_folder>.w2.<module>`, so these names must match exactly.

| Exercise | File in `members/<your_folder>/w2/` | Contents |
|----------|-------------------------------------|----------|
| W2-1 | `models.py` | `Task` dataclass: `title`, `importance` (1–5, else `ValueError`), `effort_h`, `deadline: date`; `days_left(today)`, never below 0 |
| W2-2 | `io_utils.py` | `load_tasks(path)`, `save_json(tasks, path)`; an invalid row raises `ValueError` naming its line (the header is line 1) |
| W2-3 | `errors.py` | `InfeasiblePlan(Exception)` with `needed_h`, `available_h` and a clear `__str__`; `check_feasible(tasks, available_h)` |
| W2-4 | `tests_for_<reviewee_folder>.py` | at least five pytest tests for your reviewee's W1-4, including one edge case the instructor's tests miss |
| W2-5 | `__init__.py`, `__main__.py` | `python -m members.<your_folder>.w2`, run from `python-bootcamp/`, loads `samples/tasks.csv` and prints the tasks |

`pytest.ini` runs the tests in importlib mode, so a test file imports what it tests by its full path,
for example `from members.vbthg.w1.translate import primes_up_to`. `python -m` runs a package's
`__main__.py`; `__init__.py` alone is not enough.

The T-W2 modules go in `shared/study_planner/`. `shared/contract.py` defines `Task` and `Block` and
describes what each function must do.

| Module | Function | Tests |
|--------|----------|-------|
| `parse.py` | `parse_csv(path) -> list[Task]` | `test_parse.py` |
| `prioritise.py` | `prioritise(tasks, today) -> list[Task]` | `test_prioritise.py` |
| `allocate.py` | `allocate(tasks, hours) -> list[Block]` | `test_allocate.py` |
| `render.py` | `render(blocks) -> str` | `test_render.py` |

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

THA Anh (Member 5): the instructor's W1-4 test has no variant 5, so skip it and run your own tests:

```bash
pytest -q python-bootcamp/tests/test_w1.py --member <your_folder> --variant 5 -k "not test_w1_4"
pytest -q python-bootcamp/members/<your_folder>/w1
```

Week 2 has no `--variant`. The second command runs your W2-4 tests, the third your W2-5 package:

```bash
pytest -q python-bootcamp/tests/test_w2.py --member <your_folder>
pytest -q python-bootcamp/members/<your_folder>/w2
cd python-bootcamp && python -m members.<your_folder>.w2
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
