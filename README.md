# MSCS532_Assignment1

## Overview

This repository contains a Python implementation of the Insertion Sort algorithm that sorts a list in **monotonically decreasing order**.

## Learning Context

Insertion Sort is a key foundational algorithm that helps illustrate:

* Loop invariants
* In-place and stable sorting
* Time and space complexity analysis

## Time & Space Complexity

* **Time Complexity:** O(n^2) in worst and average cases, O(n) in the best case
* **Space Complexity:** O(1) (in-place sort)

## Repository Structure

```
MSCS532_Assignment1/
├── insertion_sort/
│   ├── __init__.py
│   ├── sorter.py        # Core algorithm
│   └── main.py          # Main method for demonstration
├── tests/
│   ├── __init__.py
│   └── test_sorter.py   # Unit tests using unittest
├── README.md            # Project documentation
└── .gitignore           # Ignore Python cache files
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Oishani/MSCS532_Assignment1.git
cd MSCS532_Assignment1
```

### 2. Install Python

Ensure Python 3.8 or higher is installed. You can download it from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Check your installation:

```bash
python3 --version
```

Be sure to select "Add Python to PATH" during installation.

### 3. Download and Set Up Visual Studio Code (Optional)

While any IDE may be used, Visual Studio Code is recommended:
[https://code.visualstudio.com/](https://code.visualstudio.com/)

Recommended extensions:

* [Python (by Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) (optional, for running code easily)

### 4. Set Up Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 5. Run the Program

```bash
python3 insertion_sort/main.py
```

Example Output:

```
Original array: [5, 2, 9, 1, 5, 6]
Sorted in decreasing order: [9, 6, 5, 5, 2, 1]
```

### 6. Run the Tests

```bash
python3 -m unittest discover -s tests
```