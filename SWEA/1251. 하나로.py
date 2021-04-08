def make_set(node):
    parent[node] = node
    rank[node] = 0

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(edges):
    mst = []

    for node in range(N):
        make_set(node)

    edges.sort()
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
    return mst

for test_case in range(1, int(input()) + 1):
    N = int(input())
    node = [[] for _ in range(N)]
    ylist = list(map(int, input().split()))
    xlist = list(map(int, input().split()))
    for i in range(len(ylist)):
        node[i] = [ylist[i], xlist[i]]
    E = float(input())
    adj = []
    for i in range(N):
        y, x = node[i]
        for j in range(N):
            if i == j:
                continue
            dy, dx = node[j]
            L2 = abs(y - dy)**2 + abs(x - dx)**2
            adj.append([E * L2, i, j])
    
    parent = dict()
    rank = dict()
    mst = kruskal(adj)
    result = 0
    for i in mst:
        result += i[0]
    print('#{} {}'.format(test_case, round(result)))
