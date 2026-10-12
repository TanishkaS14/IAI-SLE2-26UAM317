
from collections import deque
import time

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [9, 10],
    5: [11, 12],
    6: [13, 14],
    7: [], 8: [], 9: [], 10: [],
    11: [], 12: [], 13: [], 14: []
}


def bfs(g, start, goal):
    q = deque([start])
    visited = {start}
    parent = {start: None}
    expanded = 0

    while q:
        node = q.popleft()
        expanded += 1

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], expanded

        for nxt in g[node]:
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = node
                q.append(nxt)

    return None, expanded


def dfs(g, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}
    expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        expanded += 1

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], expanded

        for nxt in reversed(g[node]):
            if nxt not in visited:
                parent[nxt] = node
                stack.append(nxt)

    return None, expanded


def measure(function, runs=20000):
    start_time = time.perf_counter()

    for _ in range(runs):
        function(graph, 0, 6)

    elapsed = time.perf_counter() - start_time
    return elapsed * 1000 / runs


bfs_path, bfs_nodes = bfs(graph, 0, 6)
dfs_path, dfs_nodes = dfs(graph, 0, 6)

bfs_times = []
dfs_times = []

for trial in range(1, 4):
    bfs_time = measure(bfs)
    dfs_time = measure(dfs)

    bfs_times.append(bfs_time)
    dfs_times.append(dfs_time)

    print(
        f"Trial {trial}: "
        f"BFS = {bfs_time:.6f} ms, "
        f"DFS = {dfs_time:.6f} ms"
    )

print("\nBFS Path:", bfs_path)
print("DFS Path:", dfs_path)
print("BFS Nodes Expanded:", bfs_nodes)
print("DFS Nodes Expanded:", dfs_nodes)

print(f"BFS Average Time: {sum(bfs_times) / 3:.6f} ms")
print(f"DFS Average Time: {sum(dfs_times) / 3:.6f} ms")
