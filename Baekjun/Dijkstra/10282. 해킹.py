import heapq

def dijkstra(graph, n, start):
    distances = [float('inf') for _ in range(n + 1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent, adjacent_distance in graph[current_node]:
            distance = current_distance + adjacent_distance
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    count = 0
    ret = float('-inf')
    for i in range(1, n + 1):
        if distances[i] != float('inf'):
            count += 1
            ret = max(ret, distances[i])
    print(count, ret)


test_case = int(input())
for _ in range(test_case):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append([a, s])
    dijkstra(adj, n, c)
    