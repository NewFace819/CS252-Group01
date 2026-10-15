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

## Layout

```
python-bootcamp/
├── README.md            # this file (Hải, T-W1)
├── PROGRESS.md          # one row per member per week (Thông, T-W1)
├── ruff.toml            # lint settings (Đức Huy, T-W1)
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
