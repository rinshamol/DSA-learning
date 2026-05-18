def hasCycle(n, edges):
    graph = { i: [] for i in range(n) }
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        stack = [(i, -1)]
        visited.add(i)
        while stack:
            node, parent = stack.pop()
            for nr in graph[node]:
                if not nr in visited:
                    stack.append((nr, node))
                    visited.add(nr)
                elif nr in visited and not nr == parent:
                    return True
    return False

# n = 4
# edges=[[0,1],[1,3],[3,2],[2,0]]
n = 3
edges = [[0,1],[1,2]]  
print(hasCycle(n,edges))