def solution(prices):
    answer = []
    length = len(prices)
    for i in range(length):
        time = 0
        for j in range(i + 1, length):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)
    return answer