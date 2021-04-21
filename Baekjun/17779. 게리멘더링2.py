def solve(x, y, d1, d2):
    # 경계선
    temp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    temp[x][y] = 5

    for i in range(1, d1+1):
        temp[x+i][y-i] = 5          # 1
        temp[x+d2+i][y+d2-i] = 5    # 4

    for i in range(1, d2+1):
        temp[x+i][y+i] = 5          # 2
        temp[x+d1+i][y-d1+i] = 5    # 3

    one = 0
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if temp[r][c] == 5:
                break
            one += lst[r][c]

    two = 0
    for r in range(1, x+d2+1):
        for c in range(N, y, -1):
            if temp[r][c] == 5:
                break
            two += lst[r][c]
    
    three = 0
    for r in range(x+d1, N+1):
        for c in range(1, y-d1+d2):
            if temp[r][c] == 5:
                break
            three += lst[r][c]
    
    four = 0
    for r in range(x+d2+1, N+1):
        for c in range(N, y-d1+d2-1, -1):
            if temp[r][c] == 5:
                break
            four += lst[r][c]
    
    five = total_people - one - two - three - four

    maxValue = max(one, two, three, four, five)
    minValue = min(one, two, three, four, five)

    return maxValue - minValue

N = int(input())
lst = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
total_people = sum(map(sum, lst))   # 전체 합
result = float('inf')

for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x + d1 + d2 > N:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > N:
                    continue
                result = min(result, solve(x, y, d1, d2))

print(result)