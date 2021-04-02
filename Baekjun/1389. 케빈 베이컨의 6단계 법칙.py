import heapq

def dijkstra(start):
    distances = [float('inf') for _ in range(N + 1)]
    queue = []
    distances[start] = 0
    heapq.heappush(queue, [0, start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent in adj[current_node]:
            distance = current_distance + 1
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return sum(distances[1:])

N, M = map(int, input().split())
adj = [set() for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].add(y)
    adj[y].add(x)
for i in range(1, N + 1):
    result[i] = dijkstra(i)
value = min(result[1:])
print(result.index(value))
