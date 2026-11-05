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
│   ├── LAB_TASKS.md
│   ├── PR_WORKFLOW_DEMO.md
│   └── CHERRY_PICK_SOURCE_NOTE.md (on cherry-pick-source)
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
6. Merge after checks pass.

Completed demonstration: [PR #8](https://github.com/Shash-0007/git-lab/pull/8), from `feature/grade-status` into `main`. PR CI passed and the PR is merged. A formal teammate review has not been recorded; see `docs/LAB_TASKS.md`.

## Lab task 2: Cherry-picking

Cherry-picking applies one selected commit from another branch without merging the entire branch.

- Source branch: `cherry-pick-source`
- Target branch: `cherry-pick-target`
- Source commit to apply: `98cbb95d1abb47671a3ad1eb46c6c3f7b83ea5a7`

In your local clone, fetch the branches, switch to `cherry-pick-target`, run `git cherry-pick 98cbb95d1abb47671a3ad1eb46c6c3f7b83ea5a7`, and push the target branch. The target branch is prepared remotely; the local cherry-pick and push remain to be performed.

## Lab task 3: GitHub Actions CI

The workflow at `.github/workflows/ci.yml` runs on pushes to `main` and on Pull Requests targeting `main`. It checks out the repository, sets up Python 3.12, installs dependencies from `requirements.txt`, and runs pytest.

Verified successful workflow runs:
- [Pull Request CI](https://github.com/Shash-0007/git-lab/actions/runs/41979412592)
- [main push CI](https://github.com/Shash-0007/git-lab/actions/runs/41979483658)

A green check means the configured workflow and tests passed. A red X indicates a failing step; open the run and inspect its logs. Pull Request checks appear on PRs targeting `main`.

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

See `docs/LAB_TASKS.md` for the current completion checklist and remaining local actions.
