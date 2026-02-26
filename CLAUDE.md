# CLAUDE.md

This file provides guidance for AI assistants working in this repository.

## Project Overview

This is a small Python utility project providing a random number generator module. It uses only Python's standard library (no external dependencies) and is intended as a demonstration/utility module.

## Repository Structure

```
Project/
├── CLAUDE.md                      # This file
└── random_number_generator.py     # Core utility module
```

> **Note:** `random_number_generator.py` was present in an earlier commit and may need to be restored or recreated. The git history contains its original implementation at commit `9005b90`.

## Architecture

The project is a single-file Python module with no framework, no database, and no external dependencies. All functions operate purely on inputs and return values — no global state, no I/O side effects (except the `__main__` block).

## Core Module: `random_number_generator.py`

### Functions

| Function | Signature | Description |
|---|---|---|
| `generate_random_number` | `(min_value=1, max_value=100) -> int` | Returns a single random integer in `[min_value, max_value]` (inclusive) |
| `generate_random_float` | `(min_value=0.0, max_value=1.0) -> float` | Returns a random float in `[min_value, max_value]` |
| `generate_random_numbers` | `(count, min_value=1, max_value=100) -> list[int]` | Returns a list of `count` random integers |

### Usage Example

```python
from random_number_generator import generate_random_number, generate_random_float, generate_random_numbers

# Single integer (default 1–100)
n = generate_random_number()

# Float with custom range
f = generate_random_float(0.0, 10.0)

# List of 5 integers
nums = generate_random_numbers(5, min_value=50, max_value=200)
```

Run the module directly to see a demonstration:

```bash
python random_number_generator.py
```

## Code Conventions

- **Language:** Python (standard library only, no `requirements.txt` needed)
- **Naming:** `snake_case` for all functions, variables, and file names
- **Docstrings:** All public functions must have a one-line docstring describing return value and range semantics
- **Default parameters:** Provide sensible defaults for `min_value`/`max_value` so callers can use functions with zero arguments
- **No side effects:** Functions should be pure (input → output); avoid modifying global state
- **`__main__` block:** Each runnable module should include a `if __name__ == "__main__":` block that demonstrates all public functions

## Development Workflow

### Running the module

```bash
python random_number_generator.py
```

### Adding a new function

1. Add the function to `random_number_generator.py` following the existing patterns (snake_case name, docstring, default args where appropriate)
2. Add a usage example to the `__main__` block
3. Update the function table in this file

### No build step required

There is no compilation, transpilation, or packaging step. Edit Python files and run them directly.

## Git Conventions

- Commit messages use imperative mood: `Add ...`, `Fix ...`, `Update ...`
- Commit messages include a short body describing the motivation when non-trivial
- Branch names follow the pattern `claude/<description>-<session-id>` for AI-generated branches

## Git History Reference

| Commit | Message | Notes |
|---|---|---|
| `9005b90` | Add random number generator | Original implementation of `random_number_generator.py` |
| `bba0e6c` | Delete random_number_generator.py | File was removed; restore from `9005b90` if needed |

To restore the original file:

```bash
git checkout 9005b90 -- random_number_generator.py
```
