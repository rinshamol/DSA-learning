# Given an undirected graph, find the length of the longest path (in terms of number of edges) from node 0 using BFS.
from collections import deque
n = 5
edges = [[0,1],[0,2],[1,3],[3,4]]
# answer = 3 (0→1→3→4)
def longest_path(n,edges):
    graph = {i:[] for i in range(n)}
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = {}
    maxi = 0
    for i in range(n):
        if i in visited:
            continue
        que = deque([i])
        visited[i] = 0
        while que:
            node = que.popleft()
            for nr in graph[node]:
                if nr not in visited:
                    visited[nr] = visited[node] + 1
                    que.append(nr)
       
        for _,v in visited.items():
          maxi = max(maxi,v)
    return maxi
                
print(longest_path(n,edges))