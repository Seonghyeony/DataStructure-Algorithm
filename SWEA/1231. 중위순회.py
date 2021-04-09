def inorder(root):
    global result
    if root <= N and len(tree[root]):
        inorder(root * 2)
        result += tree[root]
        inorder(root * 2 + 1)


for test_case in range(1, 11):
    N = int(input())
    tree = [''] * (N + 1)
    for _ in range(N):
        temp = list(map(str, input().split()))
        tree[int(temp[0])] = temp[1]
    result = ''
    inorder(1)
    print('#{} {}'.format(test_case, result))
