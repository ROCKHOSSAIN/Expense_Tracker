# 💰 Expense Tracker

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![JSON](https://img.shields.io/badge/Storage-JSON-orange.svg)](https://www.json.org/)
[![CLI](https://img.shields.io/badge/Interface-CLI-green.svg)](https://en.wikipedia.org/wiki/Command-line_interface)

A clean, modular, and efficient Command Line Interface (CLI) application built in Python to manage daily expenses, track transaction histories, and ensure data persistence using local JSON storage.

---

## 📸 Application Preview

```text
==============================
      💰 EXPENSE TRACKER      
==============================
1. Add Expense
2. View All Expenses
3. Filter by Category
4. View Summary
5. Delete Expense
6. Exit
==============================





👤 User
                │
                ▼
           ┌─────────┐
           │ main.py │
           └────┬────┘
                │
                ▼
        ┌───────────────┐
        │  tracker.py   │
        └───────┬───────┘
                │
        ┌───────┴────────┐
        ▼                ▼
   load_expense()   save_expense()
        │                │
        └───────┬────────┘
                ▼
        ┌─────────────┐
        │ expense.json│
        └─────────────┘
