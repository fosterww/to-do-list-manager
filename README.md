# to-do-list-manager
---

# CLI To-Do List Manager

A simple command-line tool to manage your to-do tasks using Python and JSON. Built with `Click`, this project demonstrates CLI app design, persistent storage, and clean modular code.

## Features

* ✅ **Add Tasks**: Add new to-dos with a single command.
* 📋 **List Tasks**: Display all tasks with status indicators.
* ✔️ **Mark as Done**: Mark tasks as completed.
* 🗑️ **Delete Tasks**: Remove tasks by ID.
* 💾 **Persistent Storage**: Tasks are saved in a local `tasks.json` file.
* 💻 **User-Friendly CLI**: Built with the `Click` library.

## Requirements

* Python 3.10 or higher
* Click

Install with:

```bash
pip install click
```

## Installation

Clone the repository:

```bash
git clone https://github.com/fosterww/todo-cli.git
cd todo-cli
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install click
```

## Usage

Run the CLI tool with the following commands:

### Add a Task

```bash
python todo.py add "Buy groceries"
```

### List All Tasks

```bash
python todo.py list
```

Example output:

```
1: [✖] Buy groceries
2: [✔] Complete project report
```

### Mark Task as Done

```bash
python todo.py done 1
```

### Delete a Task

```bash
python todo.py delete 2
```

## Data Storage

All tasks are stored in a local file called `tasks.json` in the same directory. Example content:

```json
[
    {
        "id": 1,
        "task": "Buy groceries",
        "done": false
    }
]
```


## About

This project was created to learn CLI app development using Python and to practice managing persistent data. It’s part of a portfolio showcasing backend and utility scripting skills.

## Contact

* **GitHub**: [fosterww](https://github.com/fosterww)


