"""
Unit tests for Parallel Binary Search algorithm implementation.
"""

import unittest
from parallel_binary_search import (
    ParallelBinarySearch, 
    parallel_binary_search, 
    parallel_multi_search
)


class TestParallelBinarySearch(unittest.TestCase):
    """Test cases for Parallel Binary Search algorithm."""
    
    def test_unsorted_array_raises_error(self):
        """Test that unsorted array raises ValueError."""
        unsorted = [3, 1, 2, 5, 4]
        with self.assertRaises(ValueError):
            ParallelBinarySearch(unsorted)
    
    def test_empty_array(self):
        """Test searching in an empty array."""
        arr = []
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(5)
        self.assertEqual(result, -1)
    
    def test_single_element_found(self):
        """Test finding element in single-element array."""
        arr = [5]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(5)
        self.assertEqual(result, 0)
    
    def test_single_element_not_found(self):
        """Test not finding element in single-element array."""
        arr = [5]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(3)
        self.assertEqual(result, -1)
    
    def test_binary_search_found_beginning(self):
        """Test finding element at the beginning."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(1)
        self.assertEqual(result, 0)
    
    def test_binary_search_found_middle(self):
        """Test finding element in the middle."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(7)
        self.assertEqual(result, 3)
    
    def test_binary_search_found_end(self):
        """Test finding element at the end."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(15)
        self.assertEqual(result, 7)
    
    def test_binary_search_not_found(self):
        """Test not finding element in array."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(6)
        self.assertEqual(result, -1)
    
    def test_binary_search_not_found_too_small(self):
        """Test searching for value smaller than all elements."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(0)
        self.assertEqual(result, -1)
    
    def test_binary_search_not_found_too_large(self):
        """Test searching for value larger than all elements."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(20)
        self.assertEqual(result, -1)
    
    def test_binary_search_with_duplicates(self):
        """Test binary search with duplicate values."""
        arr = [1, 2, 2, 2, 5, 7, 9]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(2)
        # Should find one of the duplicate positions
        self.assertIn(result, [1, 2, 3])
        self.assertEqual(arr[result], 2)
    
    def test_parallel_segmented_search_found(self):
        """Test parallel segmented search finding element."""
        arr = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        searcher = ParallelBinarySearch(arr)
        result = searcher.parallel_segmented_search(50, num_segments=4)
        self.assertEqual(result, 25)
    
    def test_parallel_segmented_search_not_found(self):
        """Test parallel segmented search not finding element."""
        arr = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        searcher = ParallelBinarySearch(arr)
        result = searcher.parallel_segmented_search(51, num_segments=4)
        self.assertEqual(result, -1)
    
    def test_parallel_search_optimized_small_array(self):
        """Test optimized parallel search with small array."""
        arr = [1, 3, 5, 7, 9]
        searcher = ParallelBinarySearch(arr)
        result = searcher.parallel_search_optimized(5, num_threads=4)
        self.assertEqual(result, 2)
    
    def test_parallel_search_optimized_large_array(self):
        """Test optimized parallel search with large array."""
        arr = list(range(0, 10000, 2))
        searcher = ParallelBinarySearch(arr)
        result = searcher.parallel_search_optimized(5000, num_threads=4)
        self.assertEqual(result, 2500)
    
    def test_parallel_multi_search_all_found(self):
        """Test searching for multiple targets, all found."""
        arr = list(range(0, 20, 2))  # [0, 2, 4, ..., 18]
        searcher = ParallelBinarySearch(arr)
        targets = [0, 10, 18]
        results = searcher.parallel_multi_search(targets, num_threads=2)
        
        self.assertEqual(results[0], 0)
        self.assertEqual(results[10], 5)
        self.assertEqual(results[18], 9)
    
    def test_parallel_multi_search_some_not_found(self):
        """Test searching for multiple targets, some not found."""
        arr = list(range(0, 20, 2))  # [0, 2, 4, ..., 18]
        searcher = ParallelBinarySearch(arr)
        targets = [0, 5, 18, 25]
        results = searcher.parallel_multi_search(targets, num_threads=2)
        
        self.assertEqual(results[0], 0)
        self.assertEqual(results[5], -1)
        self.assertEqual(results[18], 9)
        self.assertEqual(results[25], -1)
    
    def test_parallel_multi_search_empty_targets(self):
        """Test searching for empty list of targets."""
        arr = [1, 3, 5, 7, 9]
        searcher = ParallelBinarySearch(arr)
        results = searcher.parallel_multi_search([], num_threads=2)
        self.assertEqual(results, {})
    
    def test_convenience_function_parallel_binary_search(self):
        """Test convenience function for single search."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        result = parallel_binary_search(arr, 9, num_threads=4)
        self.assertEqual(result, 4)
    
    def test_convenience_function_parallel_multi_search(self):
        """Test convenience function for multi search."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        targets = [3, 9, 15]
        results = parallel_multi_search(arr, targets, num_threads=2)
        
        self.assertEqual(results[3], 1)
        self.assertEqual(results[9], 4)
        self.assertEqual(results[15], 7)
    
    def test_large_array_search(self):
        """Test with a large array."""
        arr = list(range(0, 100000, 2))
        searcher = ParallelBinarySearch(arr)
        
        # Test various positions
        result1 = searcher.parallel_search_optimized(0, num_threads=4)
        self.assertEqual(result1, 0)
        
        result2 = searcher.parallel_search_optimized(50000, num_threads=4)
        self.assertEqual(result2, 25000)
        
        result3 = searcher.parallel_search_optimized(99998, num_threads=4)
        self.assertEqual(result3, 49999)
        
        result4 = searcher.parallel_search_optimized(99999, num_threads=4)
        self.assertEqual(result4, -1)
    
    def test_negative_numbers(self):
        """Test searching array with negative numbers."""
        arr = [-10, -5, -3, 0, 2, 5, 10]
        searcher = ParallelBinarySearch(arr)
        
        self.assertEqual(searcher.binary_search(-10), 0)
        self.assertEqual(searcher.binary_search(-5), 1)
        self.assertEqual(searcher.binary_search(0), 3)
        self.assertEqual(searcher.binary_search(10), 6)
        self.assertEqual(searcher.binary_search(-8), -1)
    
    def test_all_same_elements(self):
        """Test array with all same elements."""
        arr = [5, 5, 5, 5, 5]
        searcher = ParallelBinarySearch(arr)
        result = searcher.binary_search(5)
        # Should find one of the positions
        self.assertIn(result, [0, 1, 2, 3, 4])
        self.assertEqual(arr[result], 5)
    
    def test_two_elements(self):
        """Test array with two elements."""
        arr = [1, 5]
        searcher = ParallelBinarySearch(arr)
        
        self.assertEqual(searcher.binary_search(1), 0)
        self.assertEqual(searcher.binary_search(5), 1)
        self.assertEqual(searcher.binary_search(3), -1)
    
    def test_search_with_different_thread_counts(self):
        """Test parallel search with different thread counts."""
        arr = list(range(0, 1000, 2))
        searcher = ParallelBinarySearch(arr)
        target = 500
        
        # Test with different thread counts
        for num_threads in [1, 2, 4, 8]:
            result = searcher.parallel_search_optimized(target, num_threads=num_threads)
            self.assertEqual(result, 250, 
                           f"Failed with {num_threads} threads")


class TestHelperMethods(unittest.TestCase):
    """Test helper methods."""
    
    def test_is_sorted_true(self):
        """Test _is_sorted with sorted array."""
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(ParallelBinarySearch._is_sorted(arr))
    
    def test_is_sorted_false(self):
        """Test _is_sorted with unsorted array."""
        arr = [1, 3, 2, 4, 5]
        self.assertFalse(ParallelBinarySearch._is_sorted(arr))
    
    def test_is_sorted_empty(self):
        """Test _is_sorted with empty array."""
        arr = []
        self.assertTrue(ParallelBinarySearch._is_sorted(arr))
    
    def test_is_sorted_single_element(self):
        """Test _is_sorted with single element."""
        arr = [5]
        self.assertTrue(ParallelBinarySearch._is_sorted(arr))
    
    def test_is_sorted_with_duplicates(self):
        """Test _is_sorted with duplicates (valid)."""
        arr = [1, 2, 2, 3, 3, 3, 4]
        self.assertTrue(ParallelBinarySearch._is_sorted(arr))


if __name__ == '__main__':
    unittest.main()
