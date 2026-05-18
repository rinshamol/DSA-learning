n = 5
edges = [[0,1], [1,2], [3,4]]
def countComponents(n, edges):
    graph = { i: [] for i in range(n) }
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    count = 0
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        count += 1
        stack = [i]
        visited.add(i)
        while stack:
            node = stack.pop()
            for nr in graph[node]:
                if not nr in visited:
                    visited.add(nr)
                    stack.append(nr)
    return count
print(countComponents(n,edges))