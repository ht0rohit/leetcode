# Graph Traversal (BFS / DFS / Union-Find)

## Recognition signals
- Explicit graph, grid-as-graph, or "connected components" / "shortest path"
  / "reachability" language
- **BFS**: shortest path in unweighted graph, level-order processing
- **DFS**: exhaustive exploration, cycle detection, topological sort, connected
  components without needing shortest path
- **Union-Find**: dynamic connectivity, "will these end up connected",
  redundant connection / cycle detection in undirected graphs

## Templates
```python
# BFS
from collections import deque
q = deque([start])
visited = {start}
while q:
    node = q.popleft()
    for nxt in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)

# DFS
def dfs(node, visited):
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, visited)

# Union-Find
parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[ra] = rb
```

## Common pitfalls
- Using DFS recursion on inputs large enough to hit recursion limits
- Forgetting to mark visited before enqueueing (BFS re-adding the same node)
- Union-Find without path compression/union by rank degrading to O(n) per op

## Linked problems
- (add slugs as you tag/confirm them)
