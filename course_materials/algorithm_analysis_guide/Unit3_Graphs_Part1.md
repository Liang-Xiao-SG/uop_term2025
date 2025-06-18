# Unit 3: Graphs (Part 1) - Representations and Traversals

## Introduction

Graphs are fundamental non-linear data structures used to model relationships between objects. They consist of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. This unit introduces graph theory basics, common representations, and fundamental traversal algorithms.

## Learning Objectives

After this unit, you should be able to:
- Understand basic graph terminology (vertex, edge, directed, undirected, weighted, etc.).
- Represent graphs using Adjacency Matrices and Adjacency Lists.
- Implement and analyze Breadth-First Search (BFS).
- Implement and analyze Depth-First Search (DFS).

## 1. Basic Graph Terminology

-   **Vertex (Node):** A fundamental part of a graph.
-   **Edge (Link/Arc):** A connection between two vertices.
-   **Undirected Graph:** Edges have no orientation (e.g., an edge `(u, v)` is the same as `(v, u)`).
-   **Directed Graph (Digraph):** Edges have a direction (e.g., an edge `(u, v)` goes from `u` to `v`).
-   **Weighted Graph:** Each edge has an associated weight or cost.
-   **Unweighted Graph:** Edges do not have weights.
-   **Path:** A sequence of vertices connected by edges.
-   **Cycle:** A path that starts and ends at the same vertex.
-   **Connected Graph (Undirected):** There is a path between every pair of vertices.
-   **Strongly Connected Graph (Directed):** There is a directed path from any vertex to any other vertex.
-   **Degree of a Vertex (Undirected):** The number of edges incident to it.
-   **In-degree (Directed):** Number of incoming edges.
-   **Out-degree (Directed):** Number of outgoing edges.

## 2. Graph Representations

Choosing the right representation is crucial for efficient graph algorithms.

### 2.1 Adjacency Matrix
- **Definition:** A 2D matrix of size `V x V` (where `V` is the number of vertices).
    - For an unweighted graph, `adj[i][j] = 1` if there is an edge from vertex `i` to vertex `j`, otherwise `0`.
    - For a weighted graph, `adj[i][j] = weight` if there is an edge from `i` to `j`, otherwise `infinity` or `0` (depending on convention if 0 is a valid weight).
- **Pros:**
    - Checking if an edge `(u, v)` exists is O(1).
    - Adding/removing an edge is O(1).
- **Cons:**
    - Space complexity is O(V^2), which can be inefficient for sparse graphs (graphs with few edges).
    - Iterating over all neighbors of a vertex takes O(V) time.
- **Example (Undirected, Unweighted):**
    Consider a graph: 0 -- 1, 1 -- 2, 0 -- 2
    Vertices: {0, 1, 2}
    Matrix:
      0 1 2
    0[0 1 1]
    1[1 0 1]
    2[1 1 0]

### 2.2 Adjacency List
- **Definition:** An array of lists. The size of the array is `V`.
    - `adj[i]` stores a list of vertices adjacent to vertex `i`.
    - For weighted graphs, the list can store pairs `(neighbor, weight)`.
- **Pros:**
    - Space complexity is O(V + E) (where `E` is the number of edges), which is efficient for sparse graphs.
    - Iterating over all neighbors of a vertex is proportional to its degree.
- **Cons:**
    - Checking if an edge `(u, v)` exists can take O(degree(u)) time in the worst case.
- **Example (Undirected, Unweighted):**
    Graph: 0 -- 1, 1 -- 2, 0 -- 2
    Vertices: {0, 1, 2}
    Adjacency List:
    0: -> 1 -> 2
    1: -> 0 -> 2
    2: -> 0 -> 1

**Python Implementation (Adjacency List for an unweighted graph):**
```python
class GraphAdjList:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj = [[] for _ in range(self.V)] # Array of lists

    def add_edge(self, u, v, is_directed=False):
        self.adj[u].append(v)
        if not is_directed:
            self.adj[v].append(u) # For undirected graph, add reverse edge

    def print_graph(self):
        for i in range(self.V):
            print(f"Adjacency list of vertex {i}: {i}", end="")
            for neighbor in self.adj[i]:
                print(f" -> {neighbor}", end="")
            print()

# Example usage:
g = GraphAdjList(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0) # For directed, this would be a separate call if needed
g.add_edge(2, 3)
g.add_edge(3, 3) # Self-loop

# g.print_graph()
# Adjacency list of vertex 0: 0 -> 1 -> 2 -> 2
# Adjacency list of vertex 1: 1 -> 0 -> 2
# Adjacency list of vertex 2: 2 -> 0 -> 1 -> 0 -> 3
# Adjacency list of vertex 3: 3 -> 2 -> 3
```
*(Note: The print output for vertex 0 and 2 in the comment above might vary based on how add_edge handles existing edges if it were a directed graph and we added (2,0) explicitly. The code implements an undirected graph by default, so (0,2) implies (2,0). If `is_directed=True`, the behavior changes.)*

## 3. Graph Traversal Algorithms

Graph traversal means visiting all the nodes of a graph.

### 3.1 Breadth-First Search (BFS)
- **Concept:** Explores the graph layer by layer. It starts at a source vertex, explores all its immediate neighbors, then their unvisited neighbors, and so on.
- **Data Structure Used:** Queue (FIFO).
- **Steps:**
    1.  Initialize all vertices as not visited.
    2.  Create a queue and enqueue the starting source vertex `s`. Mark `s` as visited.
    3.  While the queue is not empty:
        a.  Dequeue a vertex `u` from the queue.
        b.  For each unvisited neighbor `v` of `u`:
            i.  Mark `v` as visited.
            ii. Enqueue `v`.
- **Applications:**
    - Finding the shortest path in an unweighted graph.
    - Testing if a graph is connected.
    - Cheney's algorithm for garbage collection.
    - Web crawlers (exploring web pages).
- **Complexity:** O(V + E) using an adjacency list, O(V^2) using an adjacency matrix.

**Python Example (BFS):**
```python
from collections import deque

class GraphBFS:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, u, v, is_directed=False):
        self.adj[u].append(v)
        if not is_directed:
            self.adj[v].append(u)

    def bfs(self, start_node):
        visited = [False] * self.V
        queue = deque()

        visited[start_node] = True
        queue.append(start_node)

        bfs_traversal = []

        while queue:
            u = queue.popleft()
            bfs_traversal.append(u)

            for v_neighbor in self.adj[u]:
                if not visited[v_neighbor]:
                    visited[v_neighbor] = True
                    queue.append(v_neighbor)
        return bfs_traversal

# Example usage:
g_bfs = GraphBFS(4)
g_bfs.add_edge(0, 1)
g_bfs.add_edge(0, 2)
g_bfs.add_edge(1, 2)
g_bfs.add_edge(2, 0) # Redundant for undirected, but okay
g_bfs.add_edge(2, 3)
g_bfs.add_edge(3, 3)

# print("BFS starting from vertex 2:")
# print(g_bfs.bfs(2)) # Output: [2, 0, 1, 3] (Order of neighbors of 0 and 1 might vary)
```

### 3.2 Depth-First Search (DFS)
- **Concept:** Explores the graph by going as deep as possible along each branch before backtracking. It starts at a source vertex, explores one of its neighbors, then that neighbor's neighbor, and so on, until it hits a dead end or a visited node. Then it backtracks.
- **Data Structure Used:** Stack (LIFO) - often implemented implicitly via recursion.
- **Steps (Recursive):**
    1.  Initialize all vertices as not visited.
    2.  For each vertex `u`: if `u` is not visited, call `DFS_Visit(u)`.
    3.  `DFS_Visit(u)`:
        a.  Mark `u` as visited.
        b.  For each unvisited neighbor `v` of `u`:
            Call `DFS_Visit(v)`.
- **Applications:**
    - Detecting cycles in a graph.
    - Topological sorting (for Directed Acyclic Graphs - DAGs).
    - Finding connected components.
    - Solving puzzles like mazes.
- **Complexity:** O(V + E) using an adjacency list, O(V^2) using an adjacency matrix.

**Python Example (DFS):**
```python
class GraphDFS:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj = [[] for _ in range(self.V)]
        self.dfs_traversal_result = []

    def add_edge(self, u, v, is_directed=False):
        self.adj[u].append(v)
        if not is_directed:
            self.adj[v].append(u)

    def _dfs_util(self, v, visited):
        visited[v] = True
        self.dfs_traversal_result.append(v)

        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)

    def dfs(self, start_node):
        visited = [False] * self.V
        self.dfs_traversal_result = [] # Reset for multiple calls
        self._dfs_util(start_node, visited)
        return self.dfs_traversal_result

    def dfs_disconnected(self): # Handles disconnected graphs
        visited = [False] * self.V
        self.dfs_traversal_result = []
        for i in range(self.V):
            if not visited[i]:
                self._dfs_util(i, visited)
        return self.dfs_traversal_result


# Example usage:
g_dfs = GraphDFS(5) # A graph with 5 vertices
g_dfs.add_edge(0, 1)
g_dfs.add_edge(0, 2)
g_dfs.add_edge(1, 3)
# Vertex 4 is disconnected initially

# print("DFS starting from vertex 0:")
# print(g_dfs.dfs(0))  # Output: e.g., [0, 1, 3, 2] (order can vary)

# g_dfs.add_edge(2,4)
# print("DFS for potentially disconnected graph (visiting all components):")
# print(g_dfs.dfs_disconnected()) # Output: e.g., [0, 1, 3, 2, 4]
```

## 4. Example Questions

1.  **Question:** When would you prefer an Adjacency Matrix over an Adjacency List to represent a graph?
    **Answer:** An Adjacency Matrix is preferred when the graph is dense (number of edges `E` is close to `V^2`), or when frequent checks for the existence of a specific edge `(u,v)` are needed (O(1) time). For sparse graphs, Adjacency Lists are usually better due to O(V+E) space complexity.

2.  **Question:** If you need to find the shortest path between two nodes in an unweighted graph, which traversal algorithm would you use and why?
    **Answer:** Breadth-First Search (BFS). BFS explores the graph layer by layer, guaranteeing that the first time you reach the target node, it will be via the shortest path in terms of the number of edges.

3.  **Question:** How can DFS be used to detect a cycle in an undirected graph?
    **Answer:** During a DFS traversal, if you encounter a visited vertex that is not the parent of the current vertex in the DFS tree, then a cycle exists. You need to keep track of the parent of each node in the DFS traversal.

4.  **Question:** What is the main difference in the exploration strategy between BFS and DFS?
    **Answer:**
    *   **BFS:** Explores "wide" before "deep." It visits all neighbors at the current depth before moving to neighbors at the next depth level.
    *   **DFS:** Explores "deep" before "wide." It goes as far as possible along one path before backtracking.

5.  **Question:** Consider a graph represented by an adjacency list. What is the time complexity to find all direct neighbors of a vertex `v`? What if it's an adjacency matrix?
    **Answer:**
    *   **Adjacency List:** O(degree(v)), where degree(v) is the number of neighbors of `v`. You just iterate through the list `adj[v]`.
    *   **Adjacency Matrix:** O(V), as you need to iterate through the entire row `adj[v]` to find which entries are 1 (or non-zero for weighted graphs).

## Summary

This unit covered the essentials of graph representation and the two fundamental traversal algorithms: BFS and DFS. These concepts form the building blocks for solving many complex graph problems, which will be explored in the next unit.

---
Next Unit: [Unit 4: Graphs (Part 2)](./Unit4_Graphs_Part2.md)
```
