# Opt Backend Lab

## Overview

**Opt Modeling Lab** is an experimental optimization modeling framework designed to explore how mixed-integer programming (MIP) problems can be expressed, solved, and compared across different solver backends.

The project focuses on:

- Classical MIP formulations (knapsack, facility location, set covering, TSP, etc.)
- A unified modeling interface inspired by Gurobi-style syntax
- Backend experimentation using:
  - Python-MIP (`mip`)
  - HiGHS (`highspy`)
- A lightweight alias layer (`aliases.py`) to standardize solver usage
- Notebook-driven exploration of optimization models
- A Sphinx-based “textbook-style” documentation system

The long-term goal is to better understand what abstractions are necessary for building a custom optimization backend interface.

---

# Setup (Windows)

## 1. Create virtual environment

From the project root:

```cmd
python -m venv .venv
```

Activate it:

```cmd
.venv\Scripts\activate
```

---

## 2. Install project in editable mode

```cmd
pip install -e .
```

---

## 3. For development tools:

```cmd
pip install -e .[dev]
```

---

## 4. For documentation tools:

```cmd
pip install -e .[docs]
```

## 5. Register .venv Kernel with Name:

```cmd
python -m ipykernel install --user --name opt-modeling-lab --display-name "Opt Modeling Lab"
```

## 6. Launch Jupyter-lab:

```cmd
jupyter-lab
```

---

# What each piece means

## `## 2. Install project in editable mode`
- Markdown heading (H2)
- just organizes the README visually

---

## ```cmd
- code block
- `cmd` is optional syntax hint (Windows command prompt style)
- you could also use:
  - ```bash (more universal)
  - or no label at all

---

## `pip install -e .`
This is the key idea:

> install your project in **editable mode**

Meaning:
- your `src/` code is linked directly
- changes in code immediately reflect in imports
- no reinstall needed after edits

---

## `pip install -e .[dev]`
Installs:

- your project
- plus `[project.optional-dependencies].dev` from `pyproject.toml`

---

## `pip install -e .[docs]`
Installs:

- Sphinx + MyST + theme tools
- only needed for documentation builds

---

# Important subtle point (Windows-specific)

On Windows CMD, all of these are valid:

```cmd
pip install -e .
pip install -e .[dev]
pip install -e .[docs]
```

