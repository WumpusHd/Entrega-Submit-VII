"""
Unit tests for Shearsort algorithm implementation.
"""

import unittest
from shearsort import Shearsort, shearsort


class TestShearsort(unittest.TestCase):
    """Test cases for Shearsort algorithm."""
    
    def test_empty_matrix_raises_error(self):
        """Test that empty matrix raises ValueError."""
        with self.assertRaises(ValueError):
            Shearsort([])
        
        with self.assertRaises(ValueError):
            Shearsort([[]])
    
    def test_non_rectangular_matrix_raises_error(self):
        """Test that non-rectangular matrix raises ValueError."""
        matrix = [[1, 2, 3], [4, 5]]
        with self.assertRaises(ValueError):
            Shearsort(matrix)
    
    def test_single_element_matrix(self):
        """Test sorting a 1x1 matrix."""
        matrix = [[5]]
        result = shearsort(matrix)
        self.assertEqual(result, [[5]])
    
    def test_single_row_matrix(self):
        """Test sorting a single row."""
        matrix = [[5, 2, 8, 1, 9]]
        result = shearsort(matrix)
        self.assertEqual(result, [[1, 2, 5, 8, 9]])
    
    def test_single_column_matrix(self):
        """Test sorting a single column."""
        matrix = [[5], [2], [8], [1]]
        result = shearsort(matrix)
        self.assertEqual(result, [[1], [2], [5], [8]])
    
    def test_2x2_matrix(self):
        """Test sorting a 2x2 matrix."""
        matrix = [[4, 2], [3, 1]]
        result = shearsort(matrix)
        expected = [[1, 2], [4, 3]]
        self.assertEqual(result, expected)
    
    def test_3x3_matrix(self):
        """Test sorting a 3x3 matrix."""
        matrix = [[9, 2, 7], [4, 5, 6], [3, 8, 1]]
        result = shearsort(matrix)
        expected = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
        self.assertEqual(result, expected)
    
    def test_4x4_matrix(self):
        """Test sorting a 4x4 matrix."""
        matrix = [
            [15, 3, 11, 7],
            [9, 14, 2, 10],
            [5, 12, 8, 1],
            [6, 4, 13, 16]
        ]
        result = shearsort(matrix)
        expected = [
            [1, 2, 3, 4],
            [8, 7, 6, 5],
            [9, 10, 11, 12],
            [16, 15, 14, 13]
        ]
        self.assertEqual(result, expected)
    
    def test_non_square_matrix_2x4(self):
        """Test sorting a non-square 2x4 matrix."""
        matrix = [[8, 3, 7, 1], [6, 2, 5, 4]]
        result = shearsort(matrix)
        expected = [[1, 2, 3, 4], [8, 7, 6, 5]]
        self.assertEqual(result, expected)
    
    def test_non_square_matrix_4x2(self):
        """Test sorting a non-square 4x2 matrix."""
        matrix = [[8, 3], [7, 1], [6, 2], [5, 4]]
        result = shearsort(matrix)
        expected = [[1, 2], [4, 3], [5, 6], [8, 7]]
        self.assertEqual(result, expected)
    
    def test_already_sorted_matrix(self):
        """Test sorting an already sorted matrix."""
        matrix = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
        result = shearsort(matrix)
        expected = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
        self.assertEqual(result, expected)
    
    def test_reverse_sorted_matrix(self):
        """Test sorting a reverse sorted matrix."""
        matrix = [[9, 8, 7], [4, 5, 6], [3, 2, 1]]
        result = shearsort(matrix)
        expected = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
        self.assertEqual(result, expected)
    
    def test_matrix_with_duplicates(self):
        """Test sorting a matrix with duplicate values."""
        matrix = [[5, 2, 5], [2, 1, 3], [1, 3, 2]]
        result = shearsort(matrix)
        # Verify all elements are present
        flat_result = [val for row in result for val in row]
        flat_original = [5, 2, 5, 2, 1, 3, 1, 3, 2]
        self.assertEqual(sorted(flat_result), sorted(flat_original))
    
    def test_matrix_with_negative_numbers(self):
        """Test sorting a matrix with negative numbers."""
        matrix = [[-5, 3, -1], [2, -4, 0], [1, -2, 4]]
        result = shearsort(matrix)
        expected = [[-5, -4, -2], [1, 0, -1], [2, 3, 4]]
        self.assertEqual(result, expected)
    
    def test_large_matrix_5x5(self):
        """Test sorting a larger 5x5 matrix."""
        matrix = [
            [25, 12, 7, 19, 3],
            [8, 15, 22, 1, 14],
            [18, 5, 11, 24, 9],
            [2, 20, 13, 6, 21],
            [16, 4, 23, 10, 17]
        ]
        result = shearsort(matrix)
        # Verify all elements are sorted in row-major snake order
        flat_result = []
        for i, row in enumerate(result):
            if i % 2 == 0:
                flat_result.extend(row)
            else:
                flat_result.extend(reversed(row))
        # Check that snake-order traversal is sorted
        self.assertEqual(flat_result, sorted(flat_result))
    
    def test_get_matrix_returns_copy(self):
        """Test that get_matrix returns a copy, not a reference."""
        matrix = [[1, 2], [3, 4]]
        sorter = Shearsort(matrix)
        matrix_copy = sorter.get_matrix()
        matrix_copy[0][0] = 99
        self.assertEqual(sorter.matrix[0][0], 1)
    
    def test_sort_preserves_original_input(self):
        """Test that sorting doesn't modify the original input."""
        original = [[9, 2, 7], [4, 5, 6], [3, 8, 1]]
        matrix_copy = [row[:] for row in original]
        shearsort(original)
        self.assertEqual(original, matrix_copy)


class TestShearsortHelperMethods(unittest.TestCase):
    """Test helper methods in Shearsort class."""
    
    def test_sort_row_ascending(self):
        """Test sorting a row in ascending order."""
        matrix = [[3, 1, 2], [6, 4, 5]]
        sorter = Shearsort(matrix)
        sorter.sort_row(0, ascending=True)
        self.assertEqual(sorter.matrix[0], [1, 2, 3])
    
    def test_sort_row_descending(self):
        """Test sorting a row in descending order."""
        matrix = [[3, 1, 2], [6, 4, 5]]
        sorter = Shearsort(matrix)
        sorter.sort_row(0, ascending=False)
        self.assertEqual(sorter.matrix[0], [3, 2, 1])
    
    def test_sort_column_ascending(self):
        """Test sorting a column in ascending order."""
        matrix = [[3, 6], [1, 4], [2, 5]]
        sorter = Shearsort(matrix)
        sorter.sort_column(0, ascending=True)
        self.assertEqual([sorter.matrix[i][0] for i in range(3)], [1, 2, 3])
    
    def test_sort_column_descending(self):
        """Test sorting a column in descending order."""
        matrix = [[3, 6], [1, 4], [2, 5]]
        sorter = Shearsort(matrix)
        sorter.sort_column(0, ascending=False)
        self.assertEqual([sorter.matrix[i][0] for i in range(3)], [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
