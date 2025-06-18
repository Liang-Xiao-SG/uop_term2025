# Unit 1: Review of Data Structures and Algorithms

## Introduction

Welcome to Unit 1! This unit serves as a refresher for fundamental concepts in data structures and algorithms. A solid understanding of these basics is crucial for mastering more advanced topics in algorithm analysis.

## Learning Objectives

After this unit, you should be able to:
- Recall the characteristics and common operations of basic data structures.
- Understand and explain time and space complexity.
- Interpret Big O notation and analyze simple algorithms.

## 1. Review of Common Data Structures

Data structures are specialized formats for organizing, processing, retrieving, and storing data.

### 1.1 Arrays
- **Definition:** A collection of items stored at contiguous memory locations. Elements can be accessed randomly using indices.
- **Characteristics:**
    - Fixed size (in some languages like Java, though Python lists are dynamic).
    - Fast access (O(1)) if the index is known.
    - Insertion/deletion can be slow (O(n)) as elements might need shifting.
- **Common Operations:** Accessing, searching, inserting, deleting.
- **Use Cases:** Storing collections of similar items, implementing other data structures.

### 1.2 Linked Lists
- **Definition:** A linear collection of data elements, called nodes, where each node points to the next node by means of a pointer.
- **Types:** Singly linked list, Doubly linked list, Circular linked list.
- **Characteristics:**
    - Dynamic size.
    - Efficient insertions/deletions (O(1)) if the position is known.
    - Slower access/search (O(n)) as it requires traversal.
- **Common Operations:** Traversing, inserting, deleting, searching.
- **Use Cases:** Implementing stacks, queues, managing dynamic lists of items.

### 1.3 Stacks
- **Definition:** A linear data structure that follows the Last-In-First-Out (LIFO) principle.
- **Characteristics:**
    - Operations happen at one end (the "top").
- **Common Operations:** `push` (add item to top), `pop` (remove item from top), `peek` or `top` (view top item).
- **Implementation:** Can be implemented using arrays or linked lists.
- **Use Cases:** Function call management (call stack), expression evaluation, backtracking algorithms.

### 1.4 Queues
- **Definition:** A linear data structure that follows the First-In-First-Out (FIFO) principle.
- **Characteristics:**
    - Items are added at one end (the "rear" or "enqueue") and removed from the other end (the "front" or "dequeue").
- **Common Operations:** `enqueue` (add item to rear), `dequeue` (remove item from front), `peek` (view front item).
- **Implementation:** Can be implemented using arrays or linked lists.
- **Use Cases:** Task scheduling, print queues, breadth-first search in graphs.

### 1.5 Trees
- **Definition:** A hierarchical data structure consisting of nodes connected by edges. One node is designated as the root. Each node can have zero or more child nodes.
- **Types:**
    - **Binary Tree:** Each node has at most two children (left and right).
    - **Binary Search Tree (BST):** A binary tree where the left child's value is less than the parent's, and the right child's value is greater.
    - **Balanced Trees (AVL, Red-Black):** BSTs that automatically keep their height small for efficient operations.
- **Characteristics:**
    - Efficient for searching (O(log n) in balanced trees) and representing hierarchical data.
- **Common Operations:** Traversal (in-order, pre-order, post-order), search, insert, delete.
- **Use Cases:** File systems, organization charts, syntax trees in compilers, efficient searching (BSTs).

### 1.6 Hash Tables (Hash Maps)
- **Definition:** A data structure that implements an associative array abstract data type, a structure that can map keys to values. Uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
- **Characteristics:**
    - Average O(1) time complexity for search, insert, and delete operations.
    - Worst-case can be O(n) if hash collisions are frequent and poorly handled.
- **Collision Resolution:** Techniques like chaining (linked lists at each bucket) or open addressing (probing for the next empty slot).
- **Common Operations:** `insert(key, value)`, `delete(key)`, `get(key)`.
- **Use Cases:** Implementing dictionaries, caches, database indexing.

## 2. Basic Algorithm Concepts

### 2.1 What is an Algorithm?
An algorithm is a finite sequence of well-defined, computer-implementable instructions, typically to solve a class of problems or to perform a computation.

### 2.2 Time Complexity
- **Definition:** The amount of time an algorithm takes to run as a function of the length of the input. It's usually measured in terms of the number of elementary operations performed.
- **Goal:** To understand how the algorithm's runtime scales with increasing input size.

### 2.3 Space Complexity
- **Definition:** The total amount of memory space used by an algorithm, including the space of the input values and any auxiliary space used during computation, as a function of the input size.
- **Components:**
    - **Instruction Space:** Space to store the compiled version of instructions.
    - **Data Space:** Space to store constants, variables, and dynamically allocated memory.
    - **Environment Stack Space:** Space used to store information for function calls.

### 2.4 Big O Notation
- **Definition:** A mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. In computer science, it's used to classify algorithms according to how their run time or space requirements grow as the input size grows.
- **Purpose:** Provides an upper bound on the growth rate of the function.
- **Common Big O Complexities:**
    - **O(1) - Constant Time:** Runtime is constant, regardless of input size.
        - *Example:* Accessing an array element by index.
    - **O(log n) - Logarithmic Time:** Runtime grows logarithmically with input size. Often seen in algorithms that divide the problem into smaller pieces.
        - *Example:* Binary search.
    - **O(n) - Linear Time:** Runtime grows linearly with input size.
        - *Example:* Traversing a list or array.
    - **O(n log n) - Linearithmic Time:** Common in efficient sorting algorithms.
        - *Example:* Merge sort, quicksort (average case).
    - **O(n^2) - Quadratic Time:** Runtime grows quadratically. Often seen in algorithms with nested loops.
        - *Example:* Bubble sort, insertion sort, naive matrix multiplication.
    - **O(2^n) - Exponential Time:** Runtime doubles with each addition to the input data set. Very slow for even moderately sized inputs.
        - *Example:* Recursive Fibonacci calculation without memoization, some brute-force algorithms.
    - **O(n!) - Factorial Time:** Runtime grows factorially. Extremely slow; only feasible for very small `n`.
        - *Example:* Traveling Salesperson Problem solved by brute force.

**Why Big O?**
- **Abstraction:** Ignores machine-specific constants and focuses on the growth rate.
- **Scalability:** Helps predict performance for large inputs.
- **Comparison:** Allows for a standardized way to compare the efficiency of different algorithms.

## 3. Example Questions (Conceptual)

1.  **Question:** You have an algorithm that processes a list of `n` items. For each item, it performs a constant number of operations. What is the Big O time complexity of this algorithm?
    **Answer:** O(n) - Linear time.

2.  **Question:** If an algorithm has a time complexity of O(log n), how does its runtime change if the input size doubles?
    **Answer:** The runtime increases by a constant amount (e.g., if `n` goes from 1000 to 2000, `log n` might go from ~10 to ~11, not doubling).

3.  **Question:** Explain the difference between best-case, average-case, and worst-case time complexity. Why is worst-case complexity often the most important?
    **Answer:**
    *   **Best-case:** The minimum time an algorithm takes for any input of a given size. (e.g., quicksort on an already sorted array with a good pivot strategy).
    *   **Average-case:** The expected time an algorithm takes, averaged over all possible inputs of a given size.
    *   **Worst-case:** The maximum time an algorithm takes for any input of a given size. (e.g., quicksort on a reverse-sorted array with a naive pivot).
    Worst-case is often most important because it provides an upper bound guarantee on performance, crucial for critical applications.

4.  **Question:** Why is inserting an element at the beginning of an array typically O(n), while for a linked list it can be O(1)?
    **Answer:** In an array, all subsequent elements must be shifted one position to make space, taking O(n) time. In a linked list, only a few pointer assignments are needed (update `head` and the new node's `next`), taking O(1) time.

5.  **Question:** When would you choose a Hash Table over a Binary Search Tree for storing and retrieving data? When might a BST be preferred?
    **Answer:**
    *   **Hash Table:** Preferred for faster average-case lookups, insertions, and deletions (O(1)). If order doesn't matter and speed is paramount.
    *   **BST:** Preferred when ordered traversal of elements is needed, or when worst-case O(log n) performance guarantee is required (for balanced BSTs). Hash tables can degrade to O(n) in the worst case. Also useful for operations like finding min/max, predecessor/successor.

6.  **Question:** What is a hash collision in a Hash Table, and name one way to resolve it.
    **Answer:** A hash collision occurs when two different keys hash to the same index in the underlying array. One way to resolve it is **chaining**, where each array slot (bucket) stores a linked list of items that hash to that slot.

## Summary

This unit provided a quick recap of essential data structures and the fundamentals of algorithmic analysis, particularly time/space complexity and Big O notation. These concepts will be applied and expanded upon in the subsequent units. Ensure you are comfortable with this material before proceeding.

---
Next Unit: [Unit 2: Divide and Conquer Algorithms](./Unit2_Divide_and_Conquer.md)
```
