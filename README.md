# MSCS532\_Assignment1

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

### 2. Run the Program

```bash
python3 insertion_sort/main.py
```

Example Output:

```
Original array: [5, 2, 9, 1, 5, 6]
Sorted in decreasing order: [9, 6, 5, 5, 2, 1]
```

### 3. Run the Tests

```bash
python3 -m unittest discover -s tests
```