"""
Parallel Binary Search Algorithm Implementation

Parallel binary search divides a sorted array into multiple segments and performs
binary search on each segment simultaneously using parallel processing.

Benefits:
- Utilizes multiple CPU cores for faster search
- Useful for large datasets
- Maintains O(log n) complexity per thread

Approaches:
1. Multi-element search: Search for multiple target values in parallel
2. Segmented search: Divide array into segments and search in parallel
"""

import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Optional, Tuple, Dict
import bisect


class ParallelBinarySearch:
    """Parallel binary search implementation for sorted arrays."""
    
    def __init__(self, sorted_array: List[int]):
        """
        Initialize with a sorted array.
        
        Args:
            sorted_array: A sorted list of integers
            
        Raises:
            ValueError: If array is not sorted
        """
        if not self._is_sorted(sorted_array):
            raise ValueError("Array must be sorted in ascending order")
        
        self.array = sorted_array
        self.size = len(sorted_array)
    
    @staticmethod
    def _is_sorted(arr: List[int]) -> bool:
        """Check if array is sorted in ascending order."""
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    def binary_search(self, target: int, left: int = 0, right: int = None) -> int:
        """
        Standard binary search within a range.
        
        Args:
            target: Value to search for
            left: Left boundary (inclusive)
            right: Right boundary (inclusive)
            
        Returns:
            Index of target if found, -1 otherwise
        """
        if right is None:
            right = self.size - 1
        
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    def parallel_multi_search(self, targets: List[int], num_threads: int = 4) -> Dict[int, int]:
        """
        Search for multiple targets in parallel.
        
        Args:
            targets: List of values to search for
            num_threads: Number of threads to use
            
        Returns:
            Dictionary mapping each target to its index (-1 if not found)
        """
        results = {}
        
        def search_target(target: int) -> Tuple[int, int]:
            """Helper function to search for a single target."""
            index = self.binary_search(target)
            return (target, index)
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = {executor.submit(search_target, target): target 
                      for target in targets}
            
            for future in as_completed(futures):
                target, index = future.result()
                results[target] = index
        
        return results
    
    def parallel_segmented_search(self, target: int, num_segments: int = 4) -> int:
        """
        Divide array into segments and search in parallel.
        First determines which segment contains the target, then searches that segment.
        
        Args:
            target: Value to search for
            num_segments: Number of segments to divide array into
            
        Returns:
            Index of target if found, -1 otherwise
        """
        if self.size == 0:
            return -1
        
        # Calculate segment boundaries
        segment_size = max(1, self.size // num_segments)
        segments = []
        
        for i in range(num_segments):
            start = i * segment_size
            end = min((i + 1) * segment_size - 1, self.size - 1)
            if start < self.size:
                segments.append((start, end))
        
        # Make sure last segment includes any remaining elements
        if segments:
            segments[-1] = (segments[-1][0], self.size - 1)
        
        result_index = -1
        result_lock = threading.Lock()
        
        def search_segment(start: int, end: int):
            """Search within a specific segment."""
            nonlocal result_index
            
            # Check if target could be in this segment
            if self.array[start] <= target <= self.array[end]:
                index = self.binary_search(target, start, end)
                if index != -1:
                    with result_lock:
                        result_index = index
        
        threads = []
        for start, end in segments:
            thread = threading.Thread(target=search_segment, args=(start, end))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        return result_index
    
    def parallel_search_optimized(self, target: int, num_threads: int = 4) -> int:
        """
        Optimized parallel search that first narrows down the segment using parallel
        range checking, then performs binary search.
        
        Args:
            target: Value to search for
            num_threads: Number of threads to use
            
        Returns:
            Index of target if found, -1 otherwise
        """
        if self.size == 0:
            return -1
        
        if self.size <= 100:  # For small arrays, sequential is faster
            return self.binary_search(target)
        
        return self.parallel_segmented_search(target, num_threads)


def parallel_binary_search(sorted_array: List[int], target: int, 
                          num_threads: int = 4) -> int:
    """
    Convenience function for parallel binary search.
    
    Args:
        sorted_array: A sorted list of integers
        target: Value to search for
        num_threads: Number of threads to use
        
    Returns:
        Index of target if found, -1 otherwise
        
    Example:
        >>> arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        >>> index = parallel_binary_search(arr, 13)
        >>> print(index)
        6
    """
    searcher = ParallelBinarySearch(sorted_array)
    return searcher.parallel_search_optimized(target, num_threads)


def parallel_multi_search(sorted_array: List[int], targets: List[int], 
                         num_threads: int = 4) -> Dict[int, int]:
    """
    Search for multiple targets in parallel.
    
    Args:
        sorted_array: A sorted list of integers
        targets: List of values to search for
        num_threads: Number of threads to use
        
    Returns:
        Dictionary mapping each target to its index (-1 if not found)
        
    Example:
        >>> arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        >>> results = parallel_multi_search(arr, [5, 13, 20])
        >>> print(results)
        {5: 2, 13: 6, 20: -1}
    """
    searcher = ParallelBinarySearch(sorted_array)
    return searcher.parallel_multi_search(targets, num_threads)


if __name__ == "__main__":
    import time
    
    print("Parallel Binary Search Algorithm Demo")
    print("=" * 60)
    
    # Example 1: Single target search
    print("\nExample 1: Single Target Search")
    arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    print(f"Array: {arr1}")
    target1 = 13
    print(f"Searching for: {target1}")
    
    searcher1 = ParallelBinarySearch(arr1)
    index1 = searcher1.parallel_search_optimized(target1, num_threads=4)
    print(f"Found at index: {index1}")
    print(f"Value at index: {arr1[index1] if index1 != -1 else 'Not found'}")
    
    # Example 2: Multiple targets search
    print("\nExample 2: Multiple Targets Search")
    arr2 = list(range(0, 100, 2))  # [0, 2, 4, 6, ..., 98]
    print(f"Array: {arr2[:10]}... (50 elements total)")
    targets2 = [10, 25, 50, 75, 99]
    print(f"Searching for: {targets2}")
    
    searcher2 = ParallelBinarySearch(arr2)
    results2 = searcher2.parallel_multi_search(targets2, num_threads=4)
    print(f"Results: {results2}")
    
    # Example 3: Performance comparison
    print("\nExample 3: Performance Comparison (Large Array)")
    large_arr = list(range(0, 1000000, 2))  # 500,000 elements
    search_targets = [100000, 500000, 999998]
    
    print(f"Array size: {len(large_arr)} elements")
    print(f"Searching for: {search_targets}")
    
    # Sequential search
    searcher3 = ParallelBinarySearch(large_arr)
    start = time.time()
    seq_results = {target: searcher3.binary_search(target) for target in search_targets}
    seq_time = time.time() - start
    print(f"\nSequential search time: {seq_time*1000:.4f} ms")
    print(f"Results: {seq_results}")
    
    # Parallel search
    start = time.time()
    par_results = searcher3.parallel_multi_search(search_targets, num_threads=4)
    par_time = time.time() - start
    print(f"\nParallel search time: {par_time*1000:.4f} ms")
    print(f"Results: {par_results}")
    
    # Example 4: Segmented search
    print("\nExample 4: Segmented Search")
    arr4 = list(range(1, 101))
    target4 = 75
    print(f"Array: {arr4[:10]}... (100 elements total)")
    print(f"Searching for: {target4}")
    
    searcher4 = ParallelBinarySearch(arr4)
    index4 = searcher4.parallel_segmented_search(target4, num_segments=4)
    print(f"Found at index: {index4}")
    print(f"Value at index: {arr4[index4] if index4 != -1 else 'Not found'}")
