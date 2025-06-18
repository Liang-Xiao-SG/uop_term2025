# Unit 2: Divide and Conquer Algorithms

## Introduction

Divide and Conquer (D&C) is a powerful algorithmic paradigm. It involves breaking down a problem into smaller, more manageable subproblems, solving these subproblems (usually recursively), and then combining their solutions to solve the original problem.

## Learning Objectives

After this unit, you should be able to:
- Explain the Divide and Conquer strategy.
- Identify algorithms that use this strategy.
- Implement Merge Sort and Quick Sort.
- Understand the basics of analyzing D&C algorithms, including an introduction to the Master Theorem.

## 1. The Divide and Conquer Strategy

The D&C strategy typically involves three steps:

1.  **Divide:** Break the problem into several smaller subproblems that are smaller instances of the same problem.
2.  **Conquer:** Solve the subproblems recursively. If the subproblem sizes are small enough, solve them directly (base case).
3.  **Combine:** Combine the solutions of the subproblems to create a solution for the original problem.

## 2. Examples of Divide and Conquer Algorithms

### 2.1 Binary Search
- **Concept:** Efficiently finds an item in a **sorted** array by repeatedly dividing the search interval in half.
- **Steps:**
    1.  **Divide:** Compare the target value with the middle element of the array.
    2.  **Conquer:**
        - If the target matches the middle element, the search is successful.
        - If the target is less than the middle element, recurse on the left half.
        - If the target is greater than the middle element, recurse on the right half.
    3.  **Combine:** Not explicitly needed as the "conquer" step finds the solution or narrows the search space.
- **Complexity:** O(log n) time, O(1) space (iterative version) or O(log n) space (recursive version due to call stack).

**Python Example (Iterative Binary Search):**
```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 # Target not found

# Example usage:
my_list = [2, 3, 4, 10, 40]
target_val = 10
result = binary_search(my_list, target_val)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
```

### 2.2 Merge Sort
- **Concept:** A highly efficient, comparison-based sorting algorithm.
- **Steps:**
    1.  **Divide:** Divide the unsorted list of `n` elements into two sublists of about `n/2` elements each.
    2.  **Conquer:** Sort the two sublists recursively using Merge Sort.
    3.  **Combine:** Merge the two sorted sublists back into one sorted list. This is the crucial step.
- **Complexity:** O(n log n) time (worst, average, best), O(n) space (for the merging process).

**Python Example (Merge Sort):**
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]      # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)      # Sorting the first half
        merge_sort(R)      # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example usage:
my_list = [12, 11, 13, 5, 6, 7]
sorted_list = merge_sort(my_list.copy()) # Use .copy() if you don't want to modify original
print(f"Sorted array is: {sorted_list}")
```

### 2.3 Quick Sort
- **Concept:** Another efficient, comparison-based sorting algorithm. It picks an element as a "pivot" and partitions the array around the pivot.
- **Steps:**
    1.  **Divide (Partitioning):** Choose a pivot element from the array. Rearrange the array so that all elements smaller than the pivot come before it, and all elements greater come after it. After partitioning, the pivot is in its final sorted position.
    2.  **Conquer:** Recursively apply Quick Sort to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
    3.  **Combine:** No explicit combine step is needed because the sorting is done in place during partitioning.
- **Complexity:**
    - **Best and Average Case:** O(n log n) time.
    - **Worst Case:** O(n^2) time (occurs with poor pivot choices, e.g., always picking the smallest/largest element in a sorted/reverse-sorted array).
    - **Space Complexity:** O(log n) on average (due to recursion stack), O(n) in the worst case.

**Python Example (Quick Sort):**
```python
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Swap pivot into correct position
    return i + 1

def quick_sort_recursive(arr, low, high):
    if low < high:
        pi = partition(arr, low, high) # pi is partitioning index

        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)

def quick_sort(arr):
    arr_copy = arr[:] # Create a copy to avoid modifying the original list
    quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


# Example usage:
my_list = [10, 7, 8, 9, 1, 5]
sorted_list = quick_sort(my_list)
print(f"Sorted array is: {sorted_list}")
```

## 3. Analysis of Divide and Conquer Algorithms

The runtime of D&C algorithms is often described by a recurrence relation. A recurrence relation is an equation or inequality that describes a function in terms of its value on smaller inputs.

For example, Merge Sort's recurrence is `T(n) = 2T(n/2) + O(n)`.
- `T(n)`: Time to sort `n` elements.
- `2T(n/2)`: Time to solve two subproblems of size `n/2`.
- `O(n)`: Time to merge the solutions.

### The Master Theorem (Introduction)
The Master Theorem provides a "cookbook" method for solving recurrence relations of the form:
`T(n) = aT(n/b) + f(n)`
where `a >= 1` and `b > 1` are constants, and `f(n)` is an asymptotically positive function.

There are three cases (simplified):

1.  **Case 1:** If `f(n) = O(n^(log_b a - ε))` for some constant `ε > 0`, then `T(n) = Θ(n^(log_b a))`.
    *(The work done at the leaves dominates)*
2.  **Case 2:** If `f(n) = Θ(n^(log_b a))`, then `T(n) = Θ(n^(log_b a) * log n)`.
    *(The work is distributed fairly evenly across levels of the recursion tree)*
3.  **Case 3:** If `f(n) = Ω(n^(log_b a + ε))` for some constant `ε > 0`, and if `a * f(n/b) <= c * f(n)` for some constant `c < 1` and sufficiently large `n` (regularity condition), then `T(n) = Θ(f(n))`.
    *(The work done at the root dominates)*

**Applying to Merge Sort:**
`T(n) = 2T(n/2) + O(n)`
Here, `a = 2`, `b = 2`, `f(n) = O(n)`.
`n^(log_b a) = n^(log_2 2) = n^1 = n`.
Since `f(n) = O(n)` is `Θ(n^(log_b a))`, this fits **Case 2**.
So, `T(n) = Θ(n log n)`.

We will delve deeper into recurrence relations and the Master Theorem in later algorithm analysis discussions.

## 4. Example Questions

1.  **Question:** Explain how the "divide" step in Quick Sort differs from the "divide" step in Merge Sort.
    **Answer:**
    *   **Merge Sort:** The "divide" step is trivial: it simply splits the array into two halves (e.g., left and right). The main work happens in the "combine" (merge) step.
    *   **Quick Sort:** The "divide" step is the crucial part (partitioning). It rearranges the array around a pivot, placing the pivot in its sorted position. The "combine" step is trivial (or non-existent) as sorting is done in place.

2.  **Question:** What is the worst-case scenario for Quick Sort, and how can it be mitigated?
    **Answer:** The worst-case is O(n^2), occurring when the pivot selection consistently results in highly unbalanced partitions (e.g., picking the smallest or largest element in an already sorted or reverse-sorted array).
    Mitigation strategies include:
    *   **Randomized Pivot:** Choosing a random element as the pivot.
    *   **Median-of-Three:** Choosing the median of the first, middle, and last elements as the pivot.
    *   Using an algorithm like IntroSort (hybrid) which switches to HeapSort or MergeSort if QuickSort's recursion depth exceeds a certain limit.

3.  **Question:** Why is Merge Sort generally preferred over Quick Sort for external sorting (sorting data that doesn't fit in memory)?
    **Answer:** Merge Sort is more suitable for external sorting because it accesses data sequentially during the merge phase. This is efficient for data on disk (tapes or HDDs). Quick Sort's random access pattern during partitioning is less efficient for external storage. Also, Merge Sort's O(n) space complexity is predictable, while Quick Sort's worst-case O(n) space can be an issue.

4.  **Question:** Given the recurrence `T(n) = 4T(n/2) + n`, use the Master Theorem to find the asymptotic bound for `T(n)`.
    **Answer:**
    *   `a = 4`, `b = 2`, `f(n) = n`.
    *   `n^(log_b a) = n^(log_2 4) = n^2`.
    *   Compare `f(n) = n` with `n^2`.
    *   Since `n = O(n^(2 - ε))` for `ε = 1` (i.e., `n` is polynomially smaller than `n^2`), this fits **Case 1** of the Master Theorem.
    *   Therefore, `T(n) = Θ(n^(log_b a)) = Θ(n^2)`.

5.  **Question:** Can Binary Search be applied to an unsorted array? Why or why not?
    **Answer:** No, Binary Search cannot be reliably applied to an unsorted array. It relies on the property that if the target is not the middle element, you can definitively say whether it should be in the left or right half. This is only possible if the array is sorted.

## Summary

The Divide and Conquer paradigm is a fundamental technique in algorithm design, leading to efficient solutions for many problems like sorting and searching. Understanding how to analyze these algorithms, often using recurrence relations and tools like the Master Theorem, is key to appreciating their efficiency.

---
Next Unit: [Unit 3: Graphs (Part 1)](./Unit3_Graphs_Part1.md)
```
