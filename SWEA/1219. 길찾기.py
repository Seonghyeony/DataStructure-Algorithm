from collections import deque

def bfs(graph):
    queue = deque([0])
    while queue:
        node = queue.popleft()
        if node == 99:
            return True
        queue.extend(graph[node])
    return False

while True:
    try:
        test_case, N = map(str, input().split())
        if test_case == '':
            break
        test_case, N = int(test_case), int(N)
        lst = list(map(int, input().split()))
        graph = [[] for _ in range(100)]
        for i in range(0, len(lst), 2):
            graph[lst[i]].append(lst[i+1])
        if bfs(graph):
            print('#{} {}'.format(test_case, 1))
        else:
            print('#{} {}'.format(test_case, 0))
    except:
        break   
