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

# Main function with user input
def main():
    try:
        size = int(input("Enter the size of the dataset: "))
        if size <= 0:
            print("Size must be a positive integer.")
            return

        # Generate random dataset
        dataset = random.sample(range(size * 3), size)  # Ensure unique values
        print("\nOriginal Dataset (unsorted):")
        print(dataset)

        # Sort the dataset for binary search
        dataset.sort()
        print("\nSorted Dataset:")
        print(dataset)

        target = int(input("\nEnter the target value to search for: "))

        # Linear Search
        lin_counter = Counter()
        lin_result = linear_search(dataset, target, lin_counter)
        print(f"\nLinear Search Result: Index = {lin_result}, Comparisons = {lin_counter.count}")

        # Binary Search
        bin_counter = Counter()
        bin_result = binary_search(dataset, target, 0, len(dataset) - 1, bin_counter)
        print(f"Binary Search Result: Index = {bin_result}, Comparisons = {bin_counter.count}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the program
main()
