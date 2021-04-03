def solution(priorities, location):
    answer = 0
    lst = [[j, i] for i, j in enumerate(priorities)]
    count = 0
    while True:
        maxValue, idx = max(lst)
        value, idx = lst.pop(0)
        if value < maxValue:
            lst.append([value, idx])
        if value == maxValue:
            count += 1
            if location == idx:
                answer = count
                break

    return answer