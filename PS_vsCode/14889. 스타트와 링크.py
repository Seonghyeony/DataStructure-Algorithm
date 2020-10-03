from collections import deque
from itertools import combinations
from itertools import permutations

def stet(team):
    tmp = deque(permutations(team, 2))
    ret = 0
    for y, x in tmp:
        ret += lst[y][x]
    return ret
    

N = int(input())
member = [i for i in range(N)]
lst = [list(map(int, input().split())) for _ in range(N)]

team = deque(combinations(member, N // 2))
result = float('inf')
length = len(team)

for i in range(len(team) // 2):
    result = min(result, abs(stet(team[i]) - stet(team[length-1-i])))

print(result)
