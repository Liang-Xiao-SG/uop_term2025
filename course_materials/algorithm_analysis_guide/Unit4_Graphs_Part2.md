# Unit 4: Graphs (Part 2) - Shortest Paths and Minimum Spanning Trees

## Introduction

Building on the graph fundamentals from Unit 3, this unit delves into two crucial categories of graph algorithms: finding shortest paths between vertices and constructing Minimum Spanning Trees (MSTs). These algorithms have wide-ranging applications in network routing, logistics, circuit design, and more.

## Learning Objectives

After this unit, you should be able to:
- Understand the concept of shortest path algorithms.
- Describe Dijkstra's algorithm and its use cases.
- Understand the Bellman-Ford algorithm and when it's preferred over Dijkstra's.
- Understand the concept of Minimum Spanning Trees.
- Describe Prim's and Kruskal's algorithms for finding MSTs.
- Implement Dijkstra's algorithm.

## 1. Shortest Path Algorithms

A shortest path algorithm finds a path between two vertices in a graph such that the sum of the weights of its constituent edges is minimized.

### 1.1 Dijkstra's Algorithm
- **Concept:** Finds the shortest paths from a single source vertex to all other vertices in a **weighted graph with non-negative edge weights**.
- **Greedy Approach:** At each step, it picks the unvisited vertex with the smallest known distance from the source and "relaxes" its neighbors.
- **Data Structures Used:**
    - A set or boolean array to keep track of visited vertices.
    - An array to store the shortest distance from the source to each vertex (initialized to infinity for all but the source, which is 0).
    - A priority queue (min-heap) is often used to efficiently select the unvisited vertex with the smallest distance.
- **Steps (Simplified):**
    1. Initialize `dist[source] = 0` and `dist[v] = infinity` for all other `v`.
    2. Add all vertices to a priority queue ordered by `dist` values.
    3. While the priority queue is not empty:
        a. Extract `u` (vertex with the smallest `dist`) from the priority queue.
        b. For each neighbor `v` of `u`:
            If `dist[u] + weight(u, v) < dist[v]`:
                `dist[v] = dist[u] + weight(u, v)` (This is called "relaxation")
                Update `v`'s position in the priority queue (or re-insert).
- **Complexity:**
    - O(V^2) with an adjacency matrix and linear scan for min distance.
    - O((V + E) log V) or O(E log V) with an adjacency list and a binary heap based priority queue.
    - O(E + V log V) with a Fibonacci heap.
- **Limitations:** Does not work correctly if the graph has negative edge weights.

**Python Example (Dijkstra's Algorithm using a Min-Heap):**
```python
import heapq

class GraphDijkstra:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj = [[] for _ in range(self.V)] # List of lists of tuples (neighbor, weight)

    def add_edge(self, u, v, weight):
        # For directed graph
        self.adj[u].append((v, weight))
        # If undirected, add self.adj[v].append((u, weight)) as well

    def dijkstra(self, src):
        # dist[i] will hold the shortest distance from src to i
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Min-priority queue to store vertices being preprocessed.
        # Stores (distance, vertex_id)
        pq = [(0, src)] # (distance from src, vertex)

        while pq:
            # Pop the vertex with the smallest distance
            d, u = heapq.heappop(pq)

            # If we have already found a shorter path to u, skip
            if d > dist[u]:
                continue

            # Iterate through all adjacent vertices of u
            for v_neighbor, weight in self.adj[u]:
                # If there is a shorter path to v_neighbor through u
                if dist[u] + weight < dist[v_neighbor]:
                    dist[v_neighbor] = dist[u] + weight
                    heapq.heappush(pq, (dist[v_neighbor], v_neighbor))

        # Print shortest distances
        # print("Vertex 	Distance from Source")
        # for i in range(self.V):
        #     print(f"{i}	{dist[i] if dist[i] != float('inf') else 'Infinity'}")
        return dist

# Example usage:
g_dijkstra = GraphDijkstra(5)
g_dijkstra.add_edge(0, 1, 10)
g_dijkstra.add_edge(0, 2, 3)
g_dijkstra.add_edge(1, 2, 1)
g_dijkstra.add_edge(1, 3, 2)
g_dijkstra.add_edge(2, 1, 4)
g_dijkstra.add_edge(2, 3, 8)
g_dijkstra.add_edge(2, 4, 2)
g_dijkstra.add_edge(3, 4, 7)
g_dijkstra.add_edge(4, 3, 9)

# source_node = 0
# shortest_paths = g_dijkstra.dijkstra(source_node)
# print(f"Shortest paths from node {source_node}: {shortest_paths}")
# Expected output for source 0: [0, 7.0, 3, 9.0, 5.0] (Path 0->2->1 is 3+4=7, 0->2->1->3 is 3+1+2=6 not 9, let's recheck example)
# Path 0->2 (3), 0->2->1 (3+1=4), 0->2->4 (3+2=5)
# From 1: 0->2->1->3 (3+1+2=6)
# Corrected expected: dist from 0: {0:0, 1:4, 2:3, 3:6, 4:5}

# Re-evaluating the example trace for source 0:
# dist = [0, inf, inf, inf, inf]
# pq = [(0,0)]
# Pop (0,0). u=0.
#   Neighbor 1 (w=10): dist[0]+10 < inf. dist[1]=10. pq.push((10,1)).
#   Neighbor 2 (w=3): dist[0]+3 < inf. dist[2]=3. pq.push((3,2)).
# pq = [(3,2), (10,1)]
# Pop (3,2). u=2. (dist[2]=3)
#   Neighbor 1 (w=4): dist[2]+4=7 < dist[1]=10. dist[1]=7. pq.push((7,1)).
#   Neighbor 3 (w=8): dist[2]+8=11 < inf. dist[3]=11. pq.push((11,3)).
#   Neighbor 4 (w=2): dist[2]+2=5 < inf. dist[4]=5. pq.push((5,4)).
# pq = [(5,4), (7,1), (10,1), (11,3)] (Note: (10,1) is stale)
# Pop (5,4). u=4. (dist[4]=5)
#   Neighbor 3 (w=9): dist[4]+9=14 not < dist[3]=11. No change.
# pq = [(7,1), (10,1), (11,3)]
# Pop (7,1). u=1. (dist[1]=7)
#   Neighbor 2 (w=1): dist[1]+1=8 not < dist[2]=3. No change.
#   Neighbor 3 (w=2): dist[1]+2=9 < dist[3]=11. dist[3]=9. pq.push((9,3)).
# pq = [(9,3), (10,1), (11,3)] (Note: (10,1), (11,3) are stale)
# Pop (9,3). u=3. (dist[3]=9)
#   Neighbor 4 (w=7): dist[3]+7=16 not < dist[4]=5. No change.
# pq = [(10,1), (11,3)]
# Pop (10,1) -> d=10 > dist[1]=7. Skip.
# Pop (11,3) -> d=11 > dist[3]=9. Skip.
# pq is empty.
# Final dist: [0, 7, 3, 9, 5]
```

### 1.2 Bellman-Ford Algorithm
- **Concept:** Finds the shortest paths from a single source vertex to all other vertices in a weighted graph. **Crucially, it can handle graphs with negative edge weights.**
- **Dynamic Programming Approach:** It iteratively relaxes all edges `V-1` times. After `k` iterations, it finds all shortest paths of at most `k` edges.
- **Steps:**
    1. Initialize `dist[source] = 0` and `dist[v] = infinity` for all other `v`.
    2. Repeat `V-1` times:
        For each edge `(u, v)` with weight `w`:
            If `dist[u] + w < dist[v]`:
                `dist[v] = dist[u] + w`
    3. **Check for negative weight cycles:** Repeat step 2 one more time (the V-th iteration). If any `dist` value is updated, then there is a negative weight cycle reachable from the source.
- **Complexity:** O(V * E). Slower than Dijkstra's for graphs without negative edges.
- **Use Cases:**
    - When graphs have negative edge weights (e.g., currency exchange arbitrage).
    - Detecting negative weight cycles.

## 2. Minimum Spanning Trees (MST)

- **Definition:** For a given connected, undirected, weighted graph, a Minimum Spanning Tree (MST) is a subgraph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Properties:**
    - An MST has `V-1` edges.
    - It is always a tree (no cycles).
    - It may not be unique if multiple edges have the same weight.

### 2.1 Prim's Algorithm
- **Concept:** A greedy algorithm that builds the MST one vertex at a time, starting from an arbitrary vertex. At each step, it adds the cheapest possible connection from the set of visited vertices to an unvisited vertex.
- **Analogy:** Similar to Dijkstra's algorithm for shortest paths.
- **Steps (Simplified):**
    1. Initialize a set `MST_edges` to empty.
    2. Choose an arbitrary starting vertex `s`.
    3. Maintain an array `key[v]` storing the minimum weight of an edge connecting `v` to the currently built tree (init `key[s]=0`, others `infinity`).
    4. Use a priority queue to store vertices not yet in MST, ordered by `key` values.
    5. While the priority queue is not empty:
        a. Extract `u` (vertex with min `key`) from PQ. Add `u` to MST.
        b. For each neighbor `v` of `u` not yet in MST:
            If `weight(u, v) < key[v]`:
                Set `key[v] = weight(u, v)`.
                Set `parent[v] = u` (to reconstruct the MST).
                Update `v` in PQ.
- **Complexity:** Similar to Dijkstra's: O(V^2) or O(E log V) depending on implementation.

### 2.2 Kruskal's Algorithm
- **Concept:** Another greedy algorithm. It sorts all the edges in non-decreasing order of their weights. Then, it picks the smallest edge and checks if adding it to the current MST forms a cycle. If no cycle is formed, include the edge. Otherwise, discard it.
- **Data Structure Used:** Disjoint Set Union (DSU) or Union-Find data structure to efficiently detect cycles.
- **Steps:**
    1. Create a DSU structure, with each vertex in its own set.
    2. Sort all edges in the graph by weight in non-decreasing order.
    3. Initialize `MST_edges` to empty.
    4. For each edge `(u, v)` with weight `w` (in sorted order):
        If `find(u)` is not equal to `find(v)` (i.e., `u` and `v` are in different connected components):
            Add edge `(u, v)` to `MST_edges`.
            Perform `union(u, v)`.
    5. Stop when `V-1` edges are added or all edges are processed.
- **Complexity:** O(E log E) for sorting edges. DSU operations with path compression and union by rank/size are nearly constant time on average (O(α(V)), where α is the inverse Ackermann function, very slow growing). So, dominated by sort: O(E log E) or O(E log V) as E can be up to V^2.

## 3. Example Questions

1.  **Question:** Why can't Dijkstra's algorithm handle negative edge weights correctly? Give a simple example.
    **Answer:** Dijkstra's is greedy and assumes that once a vertex is marked as "visited" (i.e., its shortest path from the source is finalized), that path is indeed the shortest. A negative edge encountered later could create a shorter path to an already "visited" node, which Dijkstra's won't revisit.
    *Example:* `S -> A (cost 3)`, `S -> B (cost 5)`, `B -> A (cost -4)`.
    Dijkstra picks `S->A` (cost 3) first. `dist[A]=3`.
    Then it might explore other paths. If it processes `S->B` (cost 5), then `B->A` (cost -4), the path `S->B->A` has cost `5 - 4 = 1`. This is shorter than 3, but Dijkstra might have already finalized `A`.

2.  **Question:** If all edge weights in a graph are positive and unique, is the Minimum Spanning Tree unique? Is the shortest path between two nodes unique?
    **Answer:**
    *   **MST:** Yes, if all edge weights are unique, the MST is unique. (This can be proven using properties of cuts and cycles).
    *   **Shortest Path:** Not necessarily. Consider `A -> B (2)`, `A -> C (1)`, `C -> B (1)`. The shortest path from A to B is `A->C->B` with cost 2. If there was another path `A->D->B` also with cost 2, the shortest path value is unique (2), but the path itself isn't. However, if *all path sums* are unique, then the path is unique. The question is about edge weights being unique.

3.  **Question:** Describe a real-world scenario where Bellman-Ford would be more appropriate than Dijkstra's.
    **Answer:** Detecting arbitrage opportunities in currency exchange. Vertices are currencies, and edges are exchange rates. If `USD -> EUR -> JPY -> USD` results in more USD than started, it's an arbitrage (a negative weight cycle if logs of rates are used). Bellman-Ford can detect such cycles.

4.  **Question:** What is the "cut property" in the context of MSTs, and how do Prim's and Kruskal's algorithms utilize it (implicitly or explicitly)?
    **Answer:** The cut property states: For any cut (a partition of vertices into two disjoint sets), if the weight of an edge `(u,v)` is strictly smaller than the weights of all other edges with one endpoint in each set, then this edge `(u,v)` belongs to every MST.
    *   **Prim's:** Implicitly uses it. It always picks the minimum weight edge connecting the current tree (one set of the cut) to a vertex not yet in the tree (the other set of the cut).
    *   **Kruskal's:** Explicitly uses it. By sorting edges and adding the smallest edge that doesn't form a cycle, it's always picking the minimum-weight edge crossing some cut (the cut between the components it connects).

5.  **Question:** If a graph has `V` vertices and `V-1` edges, and it's connected, is it always an MST?
    **Answer:** No. It is always a spanning tree, but not necessarily an MST unless its total weight is the minimum possible. For example, three vertices A, B, C with edges (A,B, weight 1), (B,C, weight 10), (A,C, weight 2). A spanning tree could be (A,B) and (B,C) with total weight 11. But the MST would use (A,B) and (A,C) with total weight 3.

## Summary

Shortest path algorithms and Minimum Spanning Tree algorithms are cornerstone tools for network analysis and optimization. Dijkstra's and Bellman-Ford address different variants of the shortest path problem, while Prim's and Kruskal's offer distinct greedy strategies to find MSTs. Understanding their mechanisms, complexities, and limitations is vital for any algorithmist.

---
Next Unit: [Unit 5: Dynamic Programming](./Unit5_Dynamic_Programming.md)
```
