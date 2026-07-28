# PayFlow (demo)

A minimal payments service used to demo CodeRabbit Post-Merge Actions.

## Setup

```bash
git init
git add .
git commit -m "Initial commit: charge/refund + post-merge actions"
gh repo create payflow-demo --public --source=. --push
```

Then install the CodeRabbit GitHub App on the new repo (or add it inside your
existing CodeRabbit org if it's already installed org-wide).

## Demo script

1. Open a PR that changes `payments/charge.py` in a way that's clearly
   user-facing (see `DEMO_CHANGE.md` for a ready-made diff).
2. Wait for the CodeRabbit review — the walkthrough will show a
   **🚀 Post-Merge Actions** section with both actions checked.
3. Merge the PR.
4. CodeRabbit posts a single result comment: a link to the changelog
   follow-up PR, plus the compliance report inline.
