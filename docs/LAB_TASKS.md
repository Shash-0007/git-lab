# Lab Task Checklist

Based on LabSheet_Part2.pdf.

## Pull Request
- [ ] Sync local repository with remote main.
- [ ] Create a feature branch.
- [ ] Commit and push a change on the feature branch.
- [ ] Open a PR into main.
- [ ] Review the PR and verify CI checks.
- [ ] Merge after checks pass.

## Cherry-picking
- [ ] Identify a source commit hash.
- [ ] Switch to the target branch.
- [ ] Cherry-pick the selected commit.
- [ ] Resolve conflicts if necessary.
- [ ] Push the target branch.

## GitHub Actions CI
- [ ] Create .github/workflows/ci.yml.
- [ ] Configure push and pull_request triggers.
- [ ] Set up Python.
- [ ] Install requirements.
- [ ] Run pytest.
- [ ] Add tests for get_status().
- [ ] Push changes and inspect the Actions tab.
- [ ] Capture a successful run as evidence.

## Expected CI behaviour
A green check indicates that the workflow passed. A red X indicates a failing step; inspect its log. Pull Request checks should appear on PRs targeting main.
