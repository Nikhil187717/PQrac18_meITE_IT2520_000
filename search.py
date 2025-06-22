import random

# Global counter class
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

# Linear Search
def linear_search(arr, target, counter):
    for i in range(len(arr)):
        counter.increment()
        if arr[i] == target:
            return i
    return -1

# Binary Search (recursive)
def binary_search(arr, target, left, right, counter):
    if left <= right:
        mid = (left + right) // 2
        counter.increment()
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, left, mid - 1, counter)
        else:
            return binary_search(arr, target, mid + 1, right, counter)
    return -1

# Function to test with different dataset sizes
def test_searches():
    sizes = [10, 100, 1000]
    for size in sizes:
        print(f"\nDataset size: {size}")

        # Worst case for linear search: last element (or not found)
        dataset = list(range(size))
        target = size  # Not in list to force worst case

        # Linear Search
        lin_counter = Counter()
        linear_search(dataset, target, lin_counter)
        print(f"Linear Search comparisons (worst case): {lin_counter.count}")

        # Binary Search requires sorted list
        bin_counter = Counter()
        binary_search(dataset, target, 0, size - 1, bin_counter)
        print(f"Binary Search comparisons (worst case): {bin_counter.count}")

test_searches()
