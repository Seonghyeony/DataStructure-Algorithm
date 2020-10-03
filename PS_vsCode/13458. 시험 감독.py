N, A = int(input()), list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for num in A:
    num -= B
    count = 1
    if num <= 0:
        result += count
        continue
    remainder = num // C
    if num % C:
        remainder += 1
    result += (count + remainder)

print(result)
    