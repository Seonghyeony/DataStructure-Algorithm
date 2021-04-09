from collections import deque

def bfs(adj, start):
    number, distance = -1, 0
    queue = deque([[0, start]])
    visited = [False] * 101
    while queue:
        value, node = queue.popleft()

        if distance < value:
            distance = value
            number = node
        elif distance == value:
            number = max(number, node)

        if not visited[node]:
            visited[node] = True
            if adj.get(node, 0):
                for next_node in adj[node]:
                    if not visited[next_node]:
                        queue.append([value + 1, next_node])
    return number

test_case = 0

while True:
    try:
        test_case += 1
        N, start = map(int, input().split())
        adj = dict()
        lst = list(map(int, input().split()))
        for i in range(0, len(lst), 2):
            x, y = lst[i], lst[i+1]
            if adj.get(x, 0):
                if y in adj[x]:
                    continue
                adj[x].append(y)
            else:
                adj[x] = [y]
        result = bfs(adj, start)
        print('#{} {}'.format(test_case, result))
    except:
        break