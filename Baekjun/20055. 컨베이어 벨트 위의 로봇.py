# 길이가 N인 컨베이어 벨트
# 1번칸: 올라가는 위치, N번칸: 내려가는 위치
# N번 칸에 로봇이 있으면 반드시 내려야 함.
# 로봇이 어떤 칸에 올라가거나 이동하면 그 칸의 내구도는 즉시 1만큼 감소.
# 내구도가 0이면 로봇이 못 올라감.
from collections import deque
N, K = map(int, input().split())
lst = deque([False for _ in range(2*N)])
A = deque(list(map(int, input().split())))

time = 0
while True:
    time += 1

    # 벨트가 한 칸 회전
    A.rotate(1)
    lst.rotate(1)

    # 내리는 칸에 로봇이 있다면 내린다.
    if lst[N-1]:
        lst[N-1] = False

    # 로봇이 이동한다.
    for i in range(2*N-2, -1, -1):
        if lst[i] == True:
            # 앞으로 이동할 수 없으면 넘김.
            if lst[i+1] == True or A[i+1] < 1:
                continue
            # 앞으로 이동
            lst[i], lst[i+1] = False, True
            # 내구도 까임.
            A[i+1] -= 1
            # 앞으로 이동한 칸이 내리는 위치이면 내린다.
            if (i+1) == (N-1):
                lst[i+1] = False
    
    # 올라가는 위치에 로봇이 없다면 로봇을 올림
    if lst[0] == False and A[0] >= 1:
        lst[0] = True
        A[0] -= 1
    
    if A.count(0) >= K:
        break

print(time)



                


