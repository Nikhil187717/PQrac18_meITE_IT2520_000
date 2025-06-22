import random

# Global counter class
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

# Bubble Sort with comparison counter
def bubble_sort(arr, counter):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            counter.increment()
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Merge Sort with comparison counter
def merge_sort(arr, counter):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, counter)
        merge_sort(R, counter)

        i = j = k = 0
        while i < len(L) and j < len(R):
            counter.increment()
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Function to test on different datasets
def test_sorts():
    sizes = [10, 100, 500]
    for size in sizes:
        print(f"\nDataset size: {size}")
        worst_case = list(range(size, 0, -1))  # descending order

        # Bubble Sort
        bs_data = worst_case.copy()
        bs_counter = Counter()
        bubble_sort(bs_data, bs_counter)
        print(f"Bubble Sort comparisons (worst case): {bs_counter.count}")

        # Merge Sort
        ms_data = worst_case.copy()
        ms_counter = Counter()
        merge_sort(ms_data, ms_counter)
        print(f"Merge Sort comparisons (worst case): {ms_counter.count}")

test_sorts()
