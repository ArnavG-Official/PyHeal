# PyHeal 🩹

Self-healing Python execution with automatic error recovery and safe execution blocks.

---

## ⚡ Features

- Safe execution blocks that prevent crashes
- Skip mode (ignore errors)
- Strict mode (normal Python behavior)
- Lightweight MVP core

---

## Installation

```python
pip install pyheal
```

---

## ⚙️ Modes

### skip()
Suppresses runtime errors inside the block.

### strict()
Normal Python behavior (no suppression).

---

## 🧠 Concept

PyHeal wraps execution blocks and controls error behavior:
- catch exceptions
- optionally suppress them
- continue execution safely

---

## ⚠️ Warning

Skipping errors may hide bugs. Use carefully.
