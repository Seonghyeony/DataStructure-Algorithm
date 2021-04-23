n = 5
data = [10, 20, 30, 40, 50]

# Prefix sum 계산
summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])