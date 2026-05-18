import heapq
def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {start: 0}
    while pq:
        cost, node = heapq.heappop(pq)
        for nr, weight in graph[node]:
            new_cost = dist[node] + weight
            if new_cost < dist.get(nr, float('inf')):
                dist[nr] = new_cost
                heapq.heappush(pq, (new_cost, nr))
    return dist
graph = {
    0: [(1, 5), (2, 1)],
    1: [(0, 5), (3, 2)],
    2: [(0, 1), (3, 1)],
    3: [(1, 2), (2, 1)]
}
print(dijkstra(graph, 0))
# Expected: {0:0, 1:4, 2:1, 3:2}