N, M = map(int, input().split())
team_mem, mem_team = {}, {}
for _ in range(N):
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = []
    for _ in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for _ in range(M):
    name, q = input(), int(input())

    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)