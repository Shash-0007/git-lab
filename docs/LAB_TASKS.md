# Lab Task Checklist

Based on LabSheet_Part2.pdf. Status reflects the remote GitHub repository as checked on 5 November 2026. Local workstation steps are marked pending because they must be run in your clone.

## Pull Request

- [ ] Sync your local repository with remote main.
- [x] Create the feature branch: `feature/grade-status`.
- [x] Commit and push a change on the feature branch.
- [x] Open a PR into `main`: [PR #8](https://github.com/Shash-0007/git-lab/pull/8).
- [ ] Obtain a review from a teammate. PR #8 has no formal review submission recorded.
- [x] Verify CI checks. The PR workflow completed successfully.
- [x] Merge after checks pass. PR #8 is merged into `main`.

## Cherry-picking

- [x] Identify the source commit: `98cbb95d1abb47671a3ad1eb46c6c3f7b83ea5a7`.
- [x] Prepare the remote source branch: `cherry-pick-source`.
- [x] Prepare the remote target branch: `cherry-pick-target`.
- [ ] Switch to the target branch in your local clone.
- [ ] Run `git cherry-pick 98cbb95d1abb47671a3ad1eb46c6c3f7b83ea5a7`.
- [ ] Push the updated target branch.

## GitHub Actions CI

- [x] Create `.github/workflows/ci.yml`.
- [x] Configure `push` and `pull_request` triggers for `main`.
- [x] Set up Python 3.12.
- [x] Install requirements from `requirements.txt`.
- [x] Run pytest.
- [x] Add tests for `get_status()`.
- [x] Push changes and inspect the Actions tab.
- [x] Confirm successful workflow runs:
  - [PR check](https://github.com/Shash-0007/git-lab/actions/runs/41979412592)
  - [main push check](https://github.com/Shash-0007/git-lab/actions/runs/41979483658)
- [ ] Save a screenshot of the green run for submission, if your instructor requires image evidence.

## Expected CI behaviour

A green check indicates that the workflow passed. A red X indicates a failing step; inspect its log. Pull Request checks should appear on PRs targeting `main`.
