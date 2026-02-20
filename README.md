# FastAPI "Broke It, Fix It" Challenge

Hands-on debugging with FastAPI. Each branch has intentionally buggy code. Your job is to run it, find the bug, and fix it.

## How it works

- **One bug per branch.** Switch to a branch, run the app, fix the bug, then move to the next.
- **Branches:** `bug-1` through `bug-6` (main challenges), plus `bonus-1` and `bonus-2` (extra).
- **Git practice:** Use `git checkout <branch-name>` to switch branches (e.g. `git checkout bug-1`).

## Run the app

From the repo root (on any bug or bonus branch):

```bash
uvicorn main:app --reload
```

Then open **http://127.0.0.1:8000/docs** for interactive API docs.

## Setup

```bash
pip install -r requirements.txt
```