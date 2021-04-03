def solution(progresses, speeds):
    answer = []
    while True:
        if len(progresses) == 0:
            break
        progresses = [i + j for i, j in zip(progresses, speeds)]
        count = 0
        while len(progresses):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break
        if count:
            answer.append(count)
    return answer