# Implementing Breadth-First Search (BFS) Algorithm in Python
# BFS is commonly used for Graph Traversal , Shortest path Finding
# Typically using FIFO  (First In , First Out)
# Time complexity  Worst Case = O(V+E)   V= Number of Vertices , E= Number of edges
from collections import deque

def bfs(graph, start):
    """Performs Breadth-First Search (BFS) on a graph from a given start node."""
    visited = set()  # Track visited nodes
    queue = deque([start])  # Initialize queue with the starting node
    bfs_order = []  # Store BFS traversal order

    while queue:
        node = queue.popleft()  # Dequeue a node from the front
        if node not in visited:
            visited.add(node)  # Mark node as visited
            bfs_order.append(node)  # Process the node
            # Add all unvisited neighbors to the queue
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return bfs_order

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Perform BFS starting from node 'A'
bfs_result = bfs(graph, 'A')
print("BFS Traversal Order:", bfs_result)
