from collections import deque

def bfs(graph, start):
    visited = set([start])
    que = deque([start])
    while que:
        node = que.popleft()
        print(node)
        for n in graph[node]:
            if not n in visited:
                visited.add(n)
                que.append(n)
graph = {1:[2,3], 2:[1,4], 3:[1,4], 4:[3,2]}
start = 1

bfs(graph,start)