n = 5
edges = [[0,1],[0,2],[1,3],[2,4]]
from collections import deque
def shortestPath(n, edges, start):
    graph = { i: [] for i in range(n) }
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    que = deque([start])
    dist = {start: 0}
    while que:
        node = que.popleft()
        for nr in graph[node]:
            if not nr in dist:
                que.append(nr)
                dist[nr] = dist[node] + 1
    return dist
print(shortestPath(n, edges, 0))
