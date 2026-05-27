# PyHeal

A self-healing execution library for Python with automatic error recovery, intelligent debugging, and runtime repair.

---

## Features

PyHeal wraps Python execution in a recovery layer:
- Execute code
- Detect errors
- Analyze traceback
- Apply fixes (if available)
- Retry execution
- Recover or restart

---

## Installation

```bash
pip install pyheal
```

---

## Configuration

### `configure(autofix=False, debug_ai=False, retries=1)`

Updates the global configuration settings.

| Parameter  | Type | Description                        |
| ---------- | ---- | ---------------------------------- |
| `autofix`  | bool | Enables automatic fixing mode      |
| `debug_ai` | bool | Enables AI-style debug suggestions |
| `retries`  | int  | Default retry count for healing    |

```python
configure(
    autofix=True,
    debug_ai=True,
    retries=3
)
```

---

## Context Managers

### `skip()`

Suppresses all exceptions inside the block.

Useful when you want code to continue even if errors occur.

```python
with skip():
    x = 1 / 0

print("Program continues")
```

```text
[pyheal] Ignored error: division by zero
Program continues
```

---

### `strict()`

Normal Python behavior.

Exceptions are NOT suppressed.

```python
with strict():
    x = 1 / 0
```

Program crashes normally with traceback.

---

### `heal(retries=1)`

Attempts to "heal" after an exception occurs.

Currently acts as a retry placeholder system.

| Parameter | Type | Description                |
| --------- | ---- | -------------------------- |
| `retries` | int  | Number of healing attempts |

```python
with heal(retries=3):
    raise ValueError("Something broke")
```

```text
[PyHeal] healing attempt 1
```

If healing fails:

```text
[PyHeal] failed to heal
```

---

### `engine`

High-level runtime protection context manager.

Suppresses crashes and logs recovery messages.

```python
with engine():
    x = 1 / 0
```

```text
[PyHeal ENGINE] started
[PyHeal ENGINE] crash recovered: division by zero
```

If no error occurs:

```text
[PyHeal ENGINE] finished cleanly
```

---

### `debug_ai()`

Provides debugging hints based on exception types.

| Error Type          | Suggestion             |
| ------------------- | ---------------------- |
| `ZeroDivisionError` | Avoid division by zero |
| `IndexError`        | Check list bounds      |
| `FileNotFoundError` | Ensure file exists     |

```python
with debug_ai():
    x = 1 / 0
```

```text
[PyHeal DEBUG AI]
Error: division by zero
Suggestion: Avoid division by zero (add validation)
```

---

## Decorators

### `@safe(default=None)`

Wraps a function safely.

If the function crashes, the error is caught and a default value is returned instead.

| Parameter | Description                          |
| --------- | ------------------------------------ |
| `default` | Value returned when exception occurs |

```python
@safe(default=0)
def divide(a, b):
    return a / b

print(divide(10, 0))
```

```text
[PyHeal SAFE] Caught: division by zero
0
```

---

## Patch System

### `apply_patch(error_type, fix)`

Registers a runtime patch for an error type.

| Parameter    | Description                   |
| ------------ | ----------------------------- |
| `error_type` | Exception class or identifier |
| `fix`        | Patch function or description |

```python
apply_patch(
    ZeroDivisionError,
    "Add denominator validation"
)
```

```text
[PyHeal PATCH] <class 'ZeroDivisionError'> -> Add denominator validation
```

---

### `watch_and_restart(file)`

Runs a Python script and automatically restarts it if it crashes.

| Parameter | Description            |
| --------- | ---------------------- |
| `file`    | Python file to monitor |

```python
watch_and_restart("app.py")
```

* Runs the script
* Detects non-zero exit codes
* Waits 2 seconds
* Restarts automatically

```text
[PyHeal] Watching: app.py
[PyHeal] Crash detected. Restarting in 2s...
```

---

## Internal Classes

### `Config`

Stores global runtime configuration.

| Attribute  | Default |
| ---------- | ------- |
| `autofix`  | `False` |
| `debug_ai` | `False` |
| `retries`  | `1`     |

---

## `PATCHES`

Global dictionary storing registered patches.

```python
PATCHES = {
    ZeroDivisionError: "Add validation"
}
```

---

## Notes

* `heal()` currently contains placeholder healing logic.
* `skip()` and `strict()` are implemented twice in the source; the later definitions override the earlier class-based versions.
* Exceptions inside `engine()` are always suppressed.
* `debug_ai()` provides simple rule-based suggestions rather than real AI debugging.

---
