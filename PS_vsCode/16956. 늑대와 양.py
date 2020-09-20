def check(nr, nc):
    if nr < 0 or nr >= R or nc < 0 or nc >= C:
        return False
    return True

R, C = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
lst = []

for _ in range(R):
    input_data = list(input())
    for idx, data in enumerate(input_data):
        if data == '.':
            input_data[idx] = 'D'
    lst.append(input_data)

result = 1

for r in range(R):
    if not result:
        break
    for c in range(C):
        if not result:
            break
        if lst[r][c] == 'W':
            for i in range(4):
                nr = r + dy[i]
                nc = c + dx[i]
                if check(nr, nc) and lst[nr][nc] == 'S':
                    result = 0
                    break
print(result)

for i in range(R):
    print(''.join(lst[i]))