# PyHeal

Self-healing Python execution with automatic error recovery and safe execution blocks.

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

Set global behavior for PyHeal.
Suppress all errors inside a block.
Normal Python behavior (no suppression).
Retries failed execution blocks automatically.
Catches exceptions
Retries execution
Applies future patch hooks (if enabled)
Analyzes errors and suggests fixes.
Decorator that prevents crashes in functions.
Catches exceptions
Returns fallback value instead of crashing
Registers automatic fix rules for known errors.
Stores fix rules
Used by future healing system
Automatically restarts a crashed Python script.
Runs script
Detects crash
Restarts automatically after delay
Self-healing execution runtime context.
Wraps execution lifecycle
Handles runtime crashes
Attempts recovery instead of full exit

---
