# Git Lab - Pull Requests, Cherry-Picking and CI

This repository contains the practical work for the GitHub lab sheet. It demonstrates a collaboration workflow using Git branches, Pull Requests, cherry-picking, and GitHub Actions.

## Project

A small Python student grade calculator is used as the sample application. It calculates averages, assigns letter grades, and determines Pass/Fail status.

## Requirements

- Git
- Python 3.12 recommended
- pytest

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Repository structure

```text
git-lab/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── grade_calculator.py
├── tests/
│   └── test_grade_calculator.py
├── docs/
│   └── LAB_TASKS.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Lab task 1: Pull Request workflow

1. Update local `main` from `origin`.
2. Create a feature branch from `main`.
3. Make a change, commit it, and push the feature branch.
4. Open a Pull Request with `main` as the base branch.
5. Review the proposed changes and verify the GitHub Actions checks.
6. Merge after checks pass and clean up the feature branch.

Suggested branch: `feature/grade-status`.

## Lab task 2: Cherry-picking

Cherry-picking applies one selected commit from another branch without merging the entire branch.

1. Identify the required commit hash on the source branch.
2. Switch to the target branch and update it.
3. Run `git cherry-pick <commit-hash>`.
4. Resolve conflicts if Git reports any.
5. Push the updated target branch.

Use the separate `cherry-pick-source` branch and its commit for this exercise.

## Lab task 3: GitHub Actions CI

The workflow at `.github/workflows/ci.yml` runs on pushes to `main` and on Pull Requests targeting `main`. It checks out the repository, sets up Python 3.12, installs pytest, and executes the test suite.

Open the **Actions** tab to inspect each run:
- Green check: all configured steps and tests passed.
- Red X: a step failed; open the run and inspect its logs.
- Pull Request checks: CI results appear on the PR before merging.

## Grade calculator functions

- `calculate_average(marks)`: validates marks and returns their arithmetic mean.
- `calculate_grade(average)`: returns A, B, C, D, or F.
- `get_status(average)`: returns Pass for averages of 40 or above, otherwise Fail.
- `calculate_result(marks)`: returns the average, grade, status, and boolean pass result.

## Submission evidence

Capture the following from GitHub:
1. Feature branch and its commit.
2. Pull Request showing base and compare branches.
3. Pull Request checks and successful merge.
4. Cherry-pick commit visible in the target branch history.
5. GitHub Actions run with a green check.
6. Local pytest output showing all tests passed.
