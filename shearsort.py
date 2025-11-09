"""
Shearsort Algorithm Implementation

Shearsort is a parallel sorting algorithm that operates on a 2D matrix.
It alternates between sorting rows and columns until the entire matrix is sorted.

Algorithm Steps:
1. Sort odd rows in ascending order (left to right)
2. Sort even rows in descending order (right to left)
3. Sort all columns in ascending order (top to bottom)
4. Repeat steps 1-3 for ceil(log2(n)) + 1 iterations, where n is the number of rows

Time Complexity: O(n * log^2(n))
Space Complexity: O(1) auxiliary space (in-place sorting)
"""

import math
from typing import List


class Shearsort:
    """Shearsort algorithm implementation for sorting 2D matrices."""
    
    def __init__(self, matrix: List[List[int]]):
        """
        Initialize Shearsort with a matrix.
        
        Args:
            matrix: A 2D list (matrix) to be sorted
            
        Raises:
            ValueError: If matrix is empty or not rectangular
        """
        if not matrix or not matrix[0]:
            raise ValueError("Matrix cannot be empty")
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Verify matrix is rectangular
        for row in matrix:
            if len(row) != cols:
                raise ValueError("Matrix must be rectangular")
        
        self.matrix = [row[:] for row in matrix]  # Deep copy
        self.rows = rows
        self.cols = cols
    
    def sort_row(self, row_idx: int, ascending: bool = True):
        """
        Sort a specific row in the matrix.
        
        Args:
            row_idx: Index of the row to sort
            ascending: True for ascending order, False for descending
        """
        self.matrix[row_idx].sort(reverse=not ascending)
    
    def sort_column(self, col_idx: int, ascending: bool = True):
        """
        Sort a specific column in the matrix.
        
        Args:
            col_idx: Index of the column to sort
            ascending: True for ascending order, False for descending
        """
        column = [self.matrix[i][col_idx] for i in range(self.rows)]
        column.sort(reverse=not ascending)
        for i in range(self.rows):
            self.matrix[i][col_idx] = column[i]
    
    def sort_rows_phase(self):
        """
        Sort all rows: odd rows ascending, even rows descending.
        Row numbering starts from 0 (0-indexed).
        """
        for i in range(self.rows):
            if i % 2 == 0:
                # Even index (0, 2, 4...) - sort ascending
                self.sort_row(i, ascending=True)
            else:
                # Odd index (1, 3, 5...) - sort descending
                self.sort_row(i, ascending=False)
    
    def sort_columns_phase(self):
        """Sort all columns in ascending order."""
        for j in range(self.cols):
            self.sort_column(j, ascending=True)
    
    def sort(self) -> List[List[int]]:
        """
        Perform Shearsort on the matrix.
        
        Returns:
            The sorted matrix
        """
        # Calculate number of iterations needed
        # Formula: ceil(log2(rows)) + 1
        iterations = math.ceil(math.log2(self.rows)) + 1 if self.rows > 1 else 1
        
        for iteration in range(iterations):
            # Phase 1: Sort rows (alternating direction)
            self.sort_rows_phase()
            
            # Phase 2: Sort columns (all ascending)
            self.sort_columns_phase()
        
        return self.matrix
    
    def get_matrix(self) -> List[List[int]]:
        """Return the current state of the matrix."""
        return [row[:] for row in self.matrix]
    
    def print_matrix(self):
        """Print the matrix in a readable format."""
        for row in self.matrix:
            print(" ".join(f"{val:4}" for val in row))
        print()


def shearsort(matrix: List[List[int]]) -> List[List[int]]:
    """
    Convenience function to sort a matrix using Shearsort algorithm.
    
    Args:
        matrix: A 2D list (matrix) to be sorted
        
    Returns:
        The sorted matrix (row-major order)
        
    Example:
        >>> matrix = [[9, 2, 7], [4, 5, 6], [3, 8, 1]]
        >>> sorted_matrix = shearsort(matrix)
        >>> print(sorted_matrix)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    sorter = Shearsort(matrix)
    return sorter.sort()


if __name__ == "__main__":
    # Example usage
    print("Shearsort Algorithm Demo")
    print("=" * 50)
    
    # Example 1: 3x3 matrix
    print("\nExample 1: 3x3 Matrix")
    matrix1 = [
        [9, 2, 7],
        [4, 5, 6],
        [3, 8, 1]
    ]
    print("Original matrix:")
    sorter1 = Shearsort(matrix1)
    sorter1.print_matrix()
    
    result1 = sorter1.sort()
    print("Sorted matrix:")
    sorter1.print_matrix()
    
    # Example 2: 4x4 matrix
    print("\nExample 2: 4x4 Matrix")
    matrix2 = [
        [15, 3, 11, 7],
        [9, 14, 2, 10],
        [5, 12, 8, 1],
        [6, 4, 13, 16]
    ]
    print("Original matrix:")
    sorter2 = Shearsort(matrix2)
    sorter2.print_matrix()
    
    result2 = sorter2.sort()
    print("Sorted matrix:")
    sorter2.print_matrix()
    
    # Example 3: 2x4 matrix (non-square)
    print("\nExample 3: 2x4 Matrix (non-square)")
    matrix3 = [
        [8, 3, 7, 1],
        [6, 2, 5, 4]
    ]
    print("Original matrix:")
    sorter3 = Shearsort(matrix3)
    sorter3.print_matrix()
    
    result3 = sorter3.sort()
    print("Sorted matrix:")
    sorter3.print_matrix()
