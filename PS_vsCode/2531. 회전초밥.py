N, d, k, c = map(int, input().split())
belt = list()
for _ in range(N):
    belt.append(int(input()))

temp_belt = belt[0:k]
max_d = len(set(belt[0:k] + [c]))
count = 0

while count < N:
    temp_belt.pop(0)
    temp_belt.append(belt[(count+k) % N])
    temp_d = len(set(temp_belt + [c]))
    if max_d < temp_d:
        max_d = temp_d
    count += 1
print(max_d)
