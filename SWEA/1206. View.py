def process(test_case):
    n = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, n-1):
        left = min(building[i] - building[i-2], building[i] - building[i-1])
        if left < 0:
            continue
        right = min(building[i] - building[i+1], building[i] - building[i+2])
        if right < 0:
            continue
        result += min(left, right)
     
    print(f'#{test_case} {result}')
 
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    process(test_case)
