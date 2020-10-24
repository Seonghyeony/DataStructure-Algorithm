from collections import deque

N, K = map(int, input().split())
lst = deque(map(int, input().split()))
people = deque([0 for _ in range(N)])
result = 0

while True:
    lst.rotate(1)
    people.rotate(1)
    result += 1

    if people[N-1]:
        people[N-1] = 0
    
    for index in range(N-2, -1, -1):
        if people[index] and not people[index+1] and lst[index+1] >= 1:
            lst[index+1] -= 1
            people[index], people[index+1] = people[index+1], people[index]
        
        if people[N-1]:
            people[N-1] = 0
    
    if lst[0] >= 1 and not people[0]:
        lst[0] -= 1
        people[0] = 1
    
    if lst.count(0) >= K:
        break

print(result)


