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

> pip install pyheal

---

## Function Blocks

### with skip():
Suppresses runtime errors inside the block.

### with strict():
Normal Python behavior (no suppression).

---

## 🧠 Concept

PyHeal wraps execution blocks and controls error behavior:
- catch exceptions
- optionally suppress them
- continue execution safely

---
