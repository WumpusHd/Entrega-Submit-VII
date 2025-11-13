# Entrega-Submit-VII

This repository contains implementations of two advanced parallel algorithms:

1. **Shearsort Algorithm** - A parallel sorting algorithm for 2D matrices
2. **Parallel Binary Search Algorithm** - A parallel implementation of binary search

## Table of Contents

- [Shearsort Algorithm](#shearsort-algorithm)
- [Parallel Binary Search Algorithm](#parallel-binary-search-algorithm)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Algorithm Details](#algorithm-details)

---

## Shearsort Algorithm

### Overview

Shearsort is a parallel sorting algorithm that operates on a 2D matrix (rectangular array). It alternates between sorting rows and columns until the entire matrix is sorted in snake-order (row-major with alternating row directions).

### Features

- Works on rectangular matrices (not just square matrices)
- In-place sorting with O(1) auxiliary space
- Time complexity: O(n × log²(n))
- Handles negative numbers, duplicates, and various matrix sizes

### Algorithm Steps

1. **Row Sort Phase**: 
   - Even-indexed rows (0, 2, 4...) are sorted in ascending order (left to right)
   - Odd-indexed rows (1, 3, 5...) are sorted in descending order (right to left)

2. **Column Sort Phase**: 
   - All columns are sorted in ascending order (top to bottom)

3. **Iteration**: 
   - Repeat steps 1-2 for ⌈log₂(rows)⌉ + 1 iterations

### Usage Example

```python
from shearsort import shearsort, Shearsort

# Simple usage with function
matrix = [
    [9, 2, 7],
    [4, 5, 6],
    [3, 8, 1]
]
sorted_matrix = shearsort(matrix)
print(sorted_matrix)
# Output: [[1, 2, 3], [6, 5, 4], [7, 8, 9]]

# Using the class for more control
sorter = Shearsort(matrix)
result = sorter.sort()
sorter.print_matrix()
```

### Files

- `shearsort.py` - Main implementation
- `test_shearsort.py` - Comprehensive unit tests

---

## Parallel Binary Search Algorithm

### Overview

Parallel Binary Search divides the search problem across multiple threads to leverage multi-core processors. It provides two main approaches:

1. **Multi-Element Search**: Search for multiple target values simultaneously
2. **Segmented Search**: Divide array into segments and search in parallel

### Features

- Maintains O(log n) complexity per search operation
- Utilizes multiple CPU cores for improved performance
- Supports both single and multiple target searches
- Thread-safe implementation using locks
- Optimized for large datasets

### Search Strategies

1. **Standard Binary Search**: Traditional sequential binary search
2. **Parallel Multi-Search**: Search for multiple targets in parallel threads
3. **Parallel Segmented Search**: Divide array into segments, search relevant segment
4. **Optimized Parallel Search**: Automatically chooses best strategy based on array size

### Usage Example

```python
from parallel_binary_search import (
    parallel_binary_search, 
    parallel_multi_search,
    ParallelBinarySearch
)

# Single target search
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
index = parallel_binary_search(arr, 13, num_threads=4)
print(f"Found at index: {index}")  # Output: Found at index: 6

# Multiple targets search
targets = [5, 13, 20]
results = parallel_multi_search(arr, targets, num_threads=4)
print(results)  # Output: {5: 2, 13: 6, 20: -1}

# Using the class for advanced features
searcher = ParallelBinarySearch(arr)
# Segmented search
index = searcher.parallel_segmented_search(13, num_segments=4)
# Multi-search
results = searcher.parallel_multi_search([3, 7, 15], num_threads=4)
```

### Files

- `parallel_binary_search.py` - Main implementation
- `test_parallel_binary_search.py` - Comprehensive unit tests

---

## Installation

### Prerequisites

- Python 3.6 or higher
- Standard library only (no external dependencies required)

### Setup

```bash
# Clone the repository
git clone https://github.com/WumpusHd/Entrega-Submit-VII.git
cd Entrega-Submit-VII

# Run examples
python3 shearsort.py
python3 parallel_binary_search.py
```

---

## Testing

Both implementations include comprehensive unit tests.

### Run All Tests

```bash
# Test Shearsort
python3 -m unittest test_shearsort.py -v

# Test Parallel Binary Search
python3 -m unittest test_parallel_binary_search.py -v

# Run all tests
python3 -m unittest discover -v
```

### Test Coverage

**Shearsort Tests (21 tests)**:
- Empty and invalid matrices
- Single element/row/column matrices
- Square matrices (2×2, 3×3, 4×4, 5×5)
- Non-square matrices (2×4, 4×2)
- Matrices with negative numbers
- Matrices with duplicates
- Already sorted and reverse sorted matrices
- Helper method tests

**Parallel Binary Search Tests (30 tests)**:
- Empty and single-element arrays
- Finding elements at different positions
- Elements not found
- Arrays with duplicates and negative numbers
- Large array performance tests
- Parallel multi-search tests
- Segmented search tests
- Different thread count configurations

---

## Algorithm Details

### Shearsort Algorithm

**Time Complexity**: O(n × log²(n))
- Where n is the number of rows in the matrix
- Each iteration performs O(n) row sorts and O(n) column sorts
- Requires ⌈log₂(n)⌉ + 1 iterations

**Space Complexity**: O(1) auxiliary space
- Sorts in-place, only uses constant extra space

**Best Use Cases**:
- When you need to sort data in a 2D structure
- Parallel processing environments
- FPGA or GPU implementations
- Data arranged in matrix form for memory optimization

### Parallel Binary Search Algorithm

**Time Complexity**: 
- Single search: O(log n) per thread
- Multi-search with k targets: O(k × log n / p) where p is number of threads
- Speedup is linear with number of cores for multi-search

**Space Complexity**: O(1) for single search, O(k) for multi-search

**Performance Characteristics**:
- Small arrays (< 100 elements): Sequential search is faster due to threading overhead
- Large arrays (> 1000 elements): Parallel search shows significant improvements
- Multi-search: Linear speedup with number of targets and threads

**Best Use Cases**:
- Searching for multiple values in the same array
- Very large sorted datasets
- Multi-core CPU environments
- Real-time search requirements with large datasets

---

## Example Outputs

### Shearsort Example

```
Original matrix:
   9    2    7
   4    5    6
   3    8    1

Sorted matrix (snake-order):
   1    2    3
   6    5    4
   7    8    9
```

### Parallel Binary Search Example

```
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Searching for multiple targets: [5, 13, 20]
Results: {5: 2, 13: 6, 20: -1}
```

---

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Please ensure all tests pass before submitting pull requests.

## References

- Shearsort: Scherson, I. D., Sen, S., & Shamir, A. (1986). "Shear Sort: A True Two-Dimensional Sorting Technique for VLSI Networks"
- Parallel Algorithms: Introduction to Parallel Computing, Ananth Grama et al.