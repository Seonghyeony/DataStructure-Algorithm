from itertools import permutations
from itertools import combinations

def skill(lst):
    ret = 0
    for y, x in lst:
        ret += S[y][x]
    return ret

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')
people = set()
for i in range(N):
    people.add(i)
divide_team = list(combinations(people, N // 2))
for i in range(len(divide_team) // 2):
    team1 = divide_team[i]
    team2 = people - set(team1)
    score1 = skill(list(permutations(team1, 2)))
    score2 = skill(list(permutations(team2, 2)))
    if result > abs(score1 - score2):
        result = abs(score1 - score2)

print(result)