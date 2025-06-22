class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

def bubble_sort(arr, counter):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            counter.increment()
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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

def main():
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        data = list(map(int, user_input.strip().split()))
        if not data:
            print("No data entered.")
            return

        print(f"\nOriginal List: {data}")

        # Bubble Sort
        bubble_data = data.copy()
        bubble_counter = Counter()
        bubble_sort(bubble_data, bubble_counter)
        print(f"\nBubble Sorted List: {bubble_data}")
        print(f"Bubble Sort Comparisons: {bubble_counter.count}")

        # Merge Sort
        merge_data = data.copy()
        merge_counter = Counter()
        merge_sort(merge_data, merge_counter)
        print(f"\nMerge Sorted List: {merge_data}")
        print(f"Merge Sort Comparisons: {merge_counter.count}")

    except ValueError:
        print("Invalid input. Please enter a list of integers only.")

# Run the program
main()
