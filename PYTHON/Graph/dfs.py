def dfs(graph, start):
    visited = set([start])
    stack = [start]
    while stack:
        node = stack.pop()
        print(node)
        for n in graph[node]:
            if not n in visited:
                visited.add(n)
                stack.append(n)
graph = {1:[2,3], 2:[1,4], 3:[1,4], 4:[3,2]}
start = 1

dfs(graph,start)