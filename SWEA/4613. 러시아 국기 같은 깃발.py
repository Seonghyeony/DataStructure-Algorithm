for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    
    result = []

    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            # (0, i) (i+1, j) (j+1, N-1)
            count = 0
            for row in lst[:i+1]:
                for w in row:
                    if w != 'W':
                        count += 1
            
            for row in lst[i+1:j+1]:
                for b in row:
                    if b != 'B':
                        count += 1
            
            for row in lst[j+1:]:
                for r in row:
                    if r != 'R':
                        count += 1
            result.append(count)
    print('#{} {}'.format(test_case, min(result)))
