# Unit 5: Dynamic Programming

## Introduction

Dynamic Programming (DP) is a powerful algorithmic technique for solving optimization and counting problems by breaking them down into simpler subproblems. Unlike Divide and Conquer, DP is typically used when subproblems overlap. DP solves each subproblem only once and stores its solution, avoiding redundant computations.

## Learning Objectives

After this unit, you should be able to:
- Define Dynamic Programming and its core ideas.
- Identify the two key characteristics of problems solvable with DP: Optimal Substructure and Overlapping Subproblems.
- Differentiate between Memoization (top-down) and Tabulation (bottom-up) approaches.
- Implement DP solutions for classic problems like Fibonacci, 0/1 Knapsack, and Longest Common Subsequence.

## 1. Core Concepts of Dynamic Programming

### 1.1 Optimal Substructure
A problem exhibits optimal substructure if an optimal solution to the problem contains within it optimal solutions to subproblems.
- *Example:* In the shortest path problem, if path `A -> B -> C` is the shortest path from A to C, then `A -> B` must be the shortest path from A to B, and `B -> C` must be the shortest path from B to C.

### 1.2 Overlapping Subproblems
A problem has overlapping subproblems if the algorithm revisits the same subproblem multiple times. DP algorithms solve each subproblem once and store the result in a table (e.g., array or hash map) to avoid re-computation.
- *Example:* Calculating the Fibonacci sequence. `fib(5)` requires `fib(4)` and `fib(3)`. `fib(4)` requires `fib(3)` and `fib(2)`. The subproblem `fib(3)` is computed twice in a naive recursive approach.

## 2. Approaches to Dynamic Programming

There are two main ways to implement a DP algorithm:

### 2.1 Memoization (Top-Down Approach)
- **Concept:** Solve the problem recursively, but store the result of each subproblem in a lookup table the first time it's computed. Subsequent calls for the same subproblem return the stored result.
- **How it works:**
    1. Start with the original problem.
    2. If the solution to a subproblem is already computed (is in the memo table), return it.
    3. Otherwise, compute the solution recursively, store it in the memo table, and then return it.
- **Analogy:** Like using sticky notes to jot down answers to avoid re-calculating.

### 2.2 Tabulation (Bottom-Up Approach)
- **Concept:** Solve the problem by filling up a table (usually an array or a 2D array) iteratively. Start with the smallest subproblems, and use their solutions to build up solutions to larger subproblems.
- **How it works:**
    1. Identify the base cases and fill them into the table.
    2. Iterate through the table, computing solutions for larger subproblems based on previously computed values for smaller subproblems.
    3. The final entry in the table for the original problem size is the answer.
- **Analogy:** Like building a tower brick by brick from the foundation up.

### Memoization vs. Tabulation
| Feature         | Memoization (Top-Down)                     | Tabulation (Bottom-Up)                       |
|-----------------|--------------------------------------------|----------------------------------------------|
| **Approach**    | Recursive, solves on demand                | Iterative, solves all prerequisite subproblems |
| **Subproblems** | Solves only necessary subproblems          | May solve subproblems not needed for the final solution |
| **Overhead**    | Recursion overhead (function calls)        | Loop overhead, potentially larger table      |
| **Ease of Coding**| Often more intuitive if recursion is natural | Can be more complex to set up iteration order |
| **Stack Overflow**| Possible for deep recursion              | Not an issue                                 |

## 3. Classic Dynamic Programming Problems and Examples

### 3.1 Fibonacci Sequence
- **Problem:** Find the nth Fibonacci number. `F(n) = F(n-1) + F(n-2)`, with `F(0)=0, F(1)=1`.
- **Overlapping Subproblems:** `fib(3)` is needed for `fib(5)` and `fib(4)`.
- **Optimal Substructure:** `fib(n)` is built from optimal solutions to `fib(n-1)` and `fib(n-2)`.

**Python Example (Fibonacci - Memoization):**
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# print(f"Fibonacci (Memoization) F(10): {fib_memo(10)}") # Output: 55
```

**Python Example (Fibonacci - Tabulation):**
```python
def fib_tab(n):
    if n <= 1:
        return n

    # Create a table to store Fibonacci numbers up to n
    # dp[i] will store F(i)
    dp = [0] * (n + 1)
    dp[1] = 1 # Base case F(1) = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# print(f"Fibonacci (Tabulation) F(10): {fib_tab(10)}") # Output: 55
```

### 3.2 0/1 Knapsack Problem
- **Problem:** Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit (knapsack capacity) and the total value is as large as possible. In the 0/1 version, you can either take an item or not (no fractions).
- **State:** `dp[i][w]` = maximum value that can be obtained using the first `i` items with a maximum weight capacity of `w`.
- **Recurrence Relation:**
  For item `i` (with `value[i-1]` and `weight[i-1]` as we use 0-based indexing for arrays but 1-based for `i` items):
  - If `weight[i-1] <= w` (current item can fit):
    `dp[i][w] = max(value[i-1] + dp[i-1][w - weight[i-1]],  dp[i-1][w])`
    (Either include item `i` or exclude item `i`)
  - If `weight[i-1] > w` (current item cannot fit):
    `dp[i][w] = dp[i-1][w]` (Exclude item `i`)
- **Base Cases:** `dp[0][w] = 0` (no items, no value), `dp[i][0] = 0` (no capacity, no value).

**Python Example (0/1 Knapsack - Tabulation):**
```python
def knapsack_01(values, weights, capacity):
    n = len(values)
    # dp[i][w] will store the maximum value that can be attained with
    # weight less than or equal to w using items up to i
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1): # i iterates through items (0 to n)
        for w in range(capacity + 1): # w iterates through capacities (0 to W)
            if i == 0 or w == 0: # Base case: no items or no capacity
                dp[i][w] = 0
            elif weights[i-1] <= w: # If current item's weight is less than current capacity
                # Max of:
                # 1. Including the item: current item's value + value from remaining capacity with previous items
                # 2. Excluding the item: value from previous items with same capacity
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else: # Current item's weight is more than current capacity, so exclude it
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example Usage:
# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50
# print(f"Maximum value in Knapsack: {knapsack_01(values, weights, capacity)}") # Output: 220 (items 2 and 3: 100+120=220)

# values_2 = [1, 4, 5, 7]
# weights_2 = [1, 3, 4, 5]
# capacity_2 = 7
# print(f"Maximum value in Knapsack: {knapsack_01(values_2, weights_2, capacity_2)}") # Output: 9 (items with value 4 and 5)
```

### 3.3 Longest Common Subsequence (LCS)
- **Problem:** Given two sequences, find the length of the longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
- **State:** `dp[i][j]` = length of the LCS of `X[0...i-1]` and `Y[0...j-1]`.
- **Recurrence Relation:**
  Let `X` and `Y` be the two strings.
  - If `X[i-1] == Y[j-1]` (last characters match):
    `dp[i][j] = 1 + dp[i-1][j-1]`
  - If `X[i-1] != Y[j-1]` (last characters don't match):
    `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
- **Base Cases:** `dp[0][j] = 0`, `dp[i][0] = 0` (if one string is empty, LCS is 0).

**Python Example (LCS - Tabulation):**
```python
def lcs_tab(X, Y):
    m = len(X)
    n = len(Y)

    # dp[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Build dp[][] in bottom-up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0: # Base case
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]: # If last characters match
                dp[i][j] = 1 + dp[i-1][j-1]
            else: # If last characters don't match
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Example Usage:
# X = "AGGTAB"
# Y = "GXTXAYB"
# print(f"Length of LCS: {lcs_tab(X, Y)}") # Output: 4 ("GTAB")

# X2 = "ABCDGH"
# Y2 = "AEDFHR"
# print(f"Length of LCS: {lcs_tab(X2, Y2)}") # Output: 3 ("ADH")
```

## 4. Steps to Solve a DP Problem

1.  **Identify if it's a DP Problem:** Look for optimal substructure and overlapping subproblems. Often involves optimization (min/max) or counting.
2.  **Define the State:** Determine what parameters uniquely identify a subproblem (e.g., `dp[i]`, `dp[i][j]`). This will be the dimensions of your DP table.
3.  **Formulate the Recurrence Relation:** Express the solution to a state in terms of solutions to smaller/previous states.
4.  **Identify Base Cases:** Determine the smallest subproblems whose solutions are known directly.
5.  **Choose Approach (Memoization or Tabulation):** Decide whether to implement recursively with memoization or iteratively with tabulation.
6.  **Implement and Test:** Write the code and test with examples.
7.  **Analyze Complexity:** Determine time and space complexity.

## 5. Example Questions

1.  **Question:** What are the two key properties a problem must have to be solvable by dynamic programming? Explain them briefly.
    **Answer:**
    *   **Optimal Substructure:** An optimal solution to the problem contains optimal solutions to its subproblems.
    *   **Overlapping Subproblems:** The algorithm solves the same subproblems repeatedly if not for memoization or tabulation.

2.  **Question:** Explain the difference between the "Divide and Conquer" paradigm and "Dynamic Programming."
    **Answer:** Both break problems into subproblems.
    *   **Divide and Conquer:** Subproblems are typically independent (non-overlapping). It solves subproblems recursively and combines results. (e.g., Merge Sort, Quick Sort).
    *   **Dynamic Programming:** Subproblems often overlap. It solves each subproblem once, stores the result, and reuses it, avoiding redundant work. (e.g., Fibonacci, Knapsack).

3.  **Question:** For the 0/1 Knapsack problem, if you are using a tabulation approach `dp[i][w]`, what does `dp[i][w]` typically represent?
    **Answer:** `dp[i][w]` represents the maximum value that can be achieved using a subset of the first `i` items, given that the total weight of the selected items does not exceed `w`.

4.  **Question:** When might memoization be preferred over tabulation? When might tabulation be preferred?
    **Answer:**
    *   **Memoization:** Preferred if the state space is large and many states might not be visited (i.e., only a fraction of subproblems need to be solved). It can also be more intuitive to write if the problem has a natural recursive structure.
    *   **Tabulation:** Preferred if all or most subproblems need to be solved. It avoids recursion overhead and potential stack overflow issues. Sometimes, space optimization is easier to see/implement in tabulation (e.g., if `dp[i]` only depends on `dp[i-1]` and `dp[i-2]`, you might only need to store a few previous states).

5.  **Question:** Can all recursive problems be solved using dynamic programming? Why or why not?
    **Answer:** No. Dynamic programming is suitable for recursive problems that exhibit both optimal substructure and *overlapping subproblems*. If the subproblems are unique and don't overlap (like in standard Merge Sort recursion on distinct array halves), DP doesn't offer an advantage over a direct recursive solution; in fact, the overhead of storing results would be unnecessary.

## Summary

Dynamic Programming is a versatile and powerful technique for tackling a wide range of optimization and combinatorial problems. By recognizing optimal substructure and overlapping subproblems, and by choosing an appropriate memoization or tabulation strategy, you can develop efficient solutions to complex challenges.

---
Next Unit: [Unit 6: Linear Programming and Reductions](./Unit6_Linear_Programming_Reductions.md)
```
