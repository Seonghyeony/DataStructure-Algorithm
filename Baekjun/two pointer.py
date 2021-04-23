# 선형시간 소요. start, end 2개의 포인터.
n, m = 5, 5
data = [1, 2, 3, 2, 5]

result = 0
summary = 0
end = 0

for start in range(n):
    # end를 가능한 만큼 이동시키기
    while summary < m and end < n:
        summary += data[end]
        end += 1
    # 부분 합이 m일 때 카운트 증가
    if summary == m:
        result += 1
    summary -= data[start]
print(result)
