# Unit 6: Linear Programming and Reductions

## Introduction

This unit introduces Linear Programming (LP), a mathematical method for optimizing a linear objective function subject to linear equality and inequality constraints. We will also explore the concept of "reductions," a fundamental idea in computer science for relating the difficulty of one problem to another.

## Learning Objectives

After this unit, you should be able to:
- Define Linear Programming and its components (objective function, constraints, decision variables).
- Convert simple problems into a standard LP formulation.
- Understand the concept of polynomial-time reductions.
- Appreciate how reductions are used to classify problems and prove hardness.

## 1. Linear Programming (LP)

Linear Programming is a technique used to achieve the best outcome (e.g., maximum profit or minimum cost) in a mathematical model whose requirements are represented by linear relationships.

### 1.1 Components of an LP Problem
-   **Decision Variables:** These are the quantities you need to determine. For example, `x_1, x_2, ..., x_n`. They are typically non-negative.
-   **Objective Function:** This is a linear function of the decision variables that you want to maximize or minimize.
    -   Example: `Maximize Z = c_1*x_1 + c_2*x_2 + ... + c_n*x_n`
-   **Constraints:** These are linear equations or inequalities that restrict the values of the decision variables.
    -   Example: `a_11*x_1 + a_12*x_2 <= b_1`
    -   `a_21*x_1 + a_22*x_2 >= b_2`
    -   `a_31*x_1 + a_32*x_2 = b_3`
-   **Non-negativity Constraints:** Typically, decision variables must be non-negative (e.g., `x_i >= 0`).

### 1.2 Standard Form of an LP Problem
A common standard form for an LP problem is:
-   **Maximize** `Z = c^T * x` (Objective function)
-   **Subject to:**
    -   `A * x <= b` (Constraints)
    -   `x >= 0` (Non-negativity constraints)
Where:
-   `x` is the vector of decision variables.
-   `c` is the vector of coefficients for the objective function.
-   `A` is the matrix of coefficients for the constraints.
-   `b` is the vector of right-hand side values for constraints.

**Transformations to Standard Form:**
-   **Minimization to Maximization:** Minimizing `f(x)` is equivalent to maximizing `-f(x)`.
-   **Greater-than-or-equal-to constraints:** `a*x >= b` can be rewritten as `-a*x <= -b`.
-   **Equality constraints:** `a*x = b` can be rewritten as two inequalities: `a*x <= b` and `a*x >= b` (which becomes `a*x <= b` and `-a*x <= -b`).
-   **Unrestricted variables:** If a variable `x_i` is unrestricted in sign, it can be replaced by `x_i' - x_i''`, where `x_i', x_i'' >= 0`.

### 1.3 Example: The Diet Problem
-   **Problem:** A person wants to plan a diet using a set of available foods. Each food has a certain amount of nutrients (e.g., vitamins, protein) and a cost. The goal is to minimize the cost of the diet while meeting minimum daily nutrient requirements.
-   **Decision Variables:** `x_j` = amount of food `j` to consume.
-   **Objective Function:** Minimize `Cost = sum(cost_j * x_j)` over all foods `j`.
-   **Constraints:**
    -   For each nutrient `i`: `sum(nutrient_ij * x_j) >= min_requirement_i` (where `nutrient_ij` is the amount of nutrient `i` in food `j`).
    -   `x_j >= 0` for all `j`.

**Formulation:**
Let `c_j` be the cost of food `j`.
Let `a_ij` be the amount of nutrient `i` in one unit of food `j`.
Let `r_i` be the minimum required amount of nutrient `i`.
Let `x_j` be the quantity of food `j` to buy.

Minimize `Z = c_1*x_1 + c_2*x_2 + ... + c_n*x_n`
Subject to:
`a_11*x_1 + a_12*x_2 + ... + a_1n*x_n >= r_1` (for nutrient 1)
`a_21*x_1 + a_22*x_2 + ... + a_2n*x_n >= r_2` (for nutrient 2)
...
`a_m1*x_1 + a_m2*x_2 + ... + a_mn*x_n >= r_m` (for nutrient m)
`x_j >= 0` for all `j = 1, ..., n`.

### 1.4 Solving LP Problems
LP problems can be solved using algorithms like:
-   **Simplex Method:** An older, widely used algorithm. Efficient in practice but can have exponential worst-case time complexity.
-   **Interior-Point Methods:** A class of algorithms (e.g., Karmarkar's algorithm) that are polynomial-time in the worst case and often competitive with Simplex in practice.

Solving LPs by hand is feasible only for very small problems. In practice, specialized software (LP solvers) is used.

## 2. Reductions in Algorithm Design

A reduction is a way to solve one problem using an algorithm for another problem. It's a central concept in computational complexity theory, particularly for proving problem hardness.

### 2.1 Polynomial-Time Reductions
If problem A can be reduced to problem B (denoted `A <=_p B`), it means:
1.  We can transform any instance of problem A into an instance of problem B in polynomial time.
2.  The solution to the instance of problem B can be transformed back into a solution for the original instance of problem A in polynomial time.

**Significance:**
-   If `A <=_p B` and B has a polynomial-time algorithm, then A also has a polynomial-time algorithm.
-   If `A <=_p B` and A is known to be hard (e.g., no known polynomial-time algorithm, or proven NP-hard), then B is also at least as hard as A. If B were easy, A would be easy too.

### 2.2 How Reductions Work (Conceptual)
Imagine you have a "black box" solver for problem B. To solve an instance of problem A:
1.  **Transform:** Take your instance of A (`input_A`) and apply a polynomial-time transformation function `t` to get an instance of B: `input_B = t(input_A)`.
2.  **Solve:** Feed `input_B` to the black box solver for B, which returns `solution_B`.
3.  **Convert Back:** Apply another polynomial-time function `c` to `solution_B` to get the solution for the original problem A: `solution_A = c(solution_B)`.

If `t` and `c` are polynomial-time, and the solver for B is polynomial-time, then the whole process for solving A is polynomial-time.

### 2.3 Examples of Reductions

#### Example 1: Independent Set to Vertex Cover
-   **Independent Set Problem:** Given a graph G, find a largest set of vertices such that no two vertices in the set are adjacent.
-   **Vertex Cover Problem:** Given a graph G, find a smallest set of vertices such that every edge in G is incident to at least one vertex in the set.

**Reduction:** A set `S` is an independent set in `G=(V,E)` if and only if `V-S` (all vertices not in `S`) is a vertex cover in `G`.
-   If `S` is an independent set, take any edge `(u,v)`. `u` and `v` cannot both be in `S`. So at least one of `u` or `v` must be in `V-S`. Thus, `V-S` covers all edges.
-   If `V-S` is a vertex cover, then for any two vertices `u,v` in `S`, there cannot be an edge between them (otherwise that edge wouldn't be covered by `V-S`). So `S` is an independent set.

This means finding a maximum independent set is equivalent to finding a minimum vertex cover. `MAX_INDEPENDENT_SET <=_p MIN_VERTEX_COVER` and vice-versa. These problems are NP-hard.

#### Example 2: Shortest Path in an Unweighted Graph to BFS
- The problem of finding the shortest path (in terms of number of edges) in an unweighted graph can be *solved by* (or reduced to) using Breadth-First Search (BFS). BFS naturally finds shortest paths from a source in unweighted graphs. Here, the "reduction" is essentially just using BFS directly.

#### Example 3: Network Flow to Linear Programming
Many network flow problems (like finding the maximum flow from a source to a sink in a capacitated network) can be formulated as Linear Programming problems.
-   **Decision Variables:** `f_uv` = flow on edge `(u,v)`.
-   **Objective Function:** Maximize `sum(f_su)` for all edges `(s,u)` from source `s` (or `sum(f_vt)` into sink `t`).
-   **Constraints:**
    -   Capacity constraints: `0 <= f_uv <= capacity_uv` for each edge.
    -   Flow conservation: For every intermediate vertex `v` (not source or sink), `sum(f_uv)` (incoming flow) = `sum(f_vx)` (outgoing flow).

If you have an LP solver, you can solve max-flow problems. This shows `MAX_FLOW <=_p LP_SOLVER`. Since LP is solvable in polynomial time, this provides one way to see that max-flow is also solvable in polynomial time.

## 3. Why are LP and Reductions Taught Together?

-   **Problem Formulation:** Many combinatorial optimization problems can be formulated as Integer Linear Programs (ILPs), where variables must be integers. If the integrality constraint can be relaxed to get an LP, and the LP solution happens to be integer, or can be rounded effectively, this is powerful.
-   **Complexity:** LP is solvable in polynomial time (P). If a problem X can be reduced to LP (`X <=_p LP`), then X is also in P (or no harder than LP).
-   **Hardness Proofs:** To show a problem Y is NP-hard, one often reduces a known NP-hard problem (like 3-SAT) to Y (`3-SAT <=_p Y`). This shows Y is at least as hard as 3-SAT. LP itself is in P, so we don't reduce NP-hard problems *to* LP to prove *their* hardness. Instead, LP serves as a powerful algorithmic tool.

## 4. Example Questions

1.  **Question:** What are the three main components of a Linear Programming problem?
    **Answer:** Decision variables, objective function (linear), and constraints (linear equalities/inequalities).

2.  **Question:** A company produces two products, A and B. Product A yields a profit of $3 per unit, and Product B yields $5 per unit. Product A requires 2 hours of machine time and 1 hour of labor. Product B requires 1 hour of machine time and 1 hour of labor. The company has 100 hours of machine time and 80 hours of labor available per week. Formulate an LP to maximize profit.
    **Answer:**
    Let `x_A` = number of units of Product A to produce.
    Let `x_B` = number of units of Product B to produce.

    Maximize `Profit Z = 3*x_A + 5*x_B`
    Subject to:
    `2*x_A + 1*x_B <= 100` (Machine time constraint)
    `1*x_A + 1*x_B <= 80`  (Labor constraint)
    `x_A >= 0`
    `x_B >= 0`

3.  **Question:** What does it mean for problem `P1` to be polynomial-time reducible to problem `P2` (`P1 <=_p P2`)? What can you conclude if `P2` is solvable in polynomial time? What if `P1` is NP-hard?
    **Answer:**
    *   `P1 <=_p P2` means an instance of `P1` can be transformed into an instance of `P2` in polynomial time, and the solution to `P2`'s instance can be transformed back to a solution for `P1`'s instance in polynomial time.
    *   If `P2` is solvable in polynomial time, then `P1` is also solvable in polynomial time.
    *   If `P1` is NP-hard, then `P2` must also be NP-hard (or harder). If `P2` were easy (poly-time), then `P1` would also be easy, which contradicts `P1` being NP-hard.

4.  **Question:** Can the problem of finding the shortest path in a graph with negative edge weights (but no negative cycles) be solved using a standard LP formulation? (Hint: Think about Bellman-Ford's structure).
    **Answer:** Yes, it can. The Bellman-Ford algorithm's relaxation steps have a structure that can be translated into LP constraints.
    Let `d_v` be the shortest distance from source `s` to vertex `v`.
    Objective: Minimize `sum(d_v)` (or specifically `d_t` if a target `t` is given, though LP usually finds all `d_v`).
    Constraints:
    `d_s = 0`
    For each edge `(u,v)` with weight `w_uv`: `d_v <= d_u + w_uv`.
    This is a system of difference constraints, which is a special case of LP.

5.  **Question:** Why is the Simplex method not considered a "polynomial-time algorithm" in the theoretical sense, even though it's often efficient in practice?
    **Answer:** In the worst-case scenario, the Simplex algorithm can take an exponential number of steps (vertices of the feasible region polytope) to find the optimal solution for certain crafted LP instances. Polynomial-time algorithms (like interior-point methods) have a worst-case runtime bounded by a polynomial function of the input size.

## Summary

Linear Programming provides a general framework for solving optimization problems with linear objectives and constraints. Reductions are a vital tool for understanding the relationships between different computational problems, establishing their relative difficulties, and leveraging existing algorithms to solve new problems. While LP itself is in P, many problems reduce *to* LP formulations, making LP solvers powerful tools.

---
Next Unit: [Unit 7: Limits to Computation (Part 1)](./Unit7_Limits_to_Computation_Part1.md)
```
