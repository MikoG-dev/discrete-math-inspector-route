# Relay Station Inspector Route Optimization (TSP)

<p align="center">
  <img src="graph.png"/>
</p>

## 📌 Problem Description

The network diagram represents seven electricity relay stations (**A, B, C, D, E, F, and G**) and the distances (in km) of the cables connecting them.

An inspector needs to visit **every relay station** starting and finishing at **Station A** while traveling the **minimum possible distance**.

### The Mathematical Challenge

While this graph can be used to find a **Minimum Spanning Tree (MST)** using Prim's or Kruskal's algorithm (ideal for laying cables), the inspector's task is a **Traveling Salesperson Problem (TSP)**.

Unlike an MST, the inspector's route:

1. Must be a **Hamiltonian Cycle** (a single continuous loop).
2. Cannot "branch" like a cable network.
3. Must account for the total distance of the travel path, not just the connection weights.

---

## 🚀 How We Solved It

Because the graph is relatively small (7 nodes), we used a **Brute Force approach** to ensure we find the absolute global minimum.

### Algorithm Steps:

1. **Graph Representation**: The network is modeled as an adjacency list where each node stores its neighboring stations and the weight (distance) of the edges.
2. **Permutation Generation**: The script generates all possible permutations of the stations $\{B, C, D, E, F, G\}$.
3. **Route Validation**: For every permutation, the code constructs a path starting at `A`, visiting the permuted stations in order, and returning to `A`.
4. **Distance Calculation**: It checks if a direct edge exists between each consecutive station in the path. If an edge is missing, the route is marked as `INVALID`.
5. **Optimization**: The script tracks the `min_distance` and stores the route(s) that achieve this minimum.

---

## 💻 How to Run the Code

### Prerequisites

- Python 3.x installed on your machine.
- No external libraries are required (uses the built-in `itertools` module).

### Execution

1. Clone this repository or download the `tsp.py` file.
2. Open your terminal or command prompt.
3. Run the script using the following command:

```bash
python tsp.py
```
