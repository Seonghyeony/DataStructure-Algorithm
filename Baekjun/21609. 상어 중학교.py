def solution(n, k, cmd):
    lst = [1 for _ in range(n)]
    answer = ''
    st = []
    
    for c in cmd:
        command = c.split(" ")
        if command[0] == 'D':
            count = int(command[1])
            for _ in range(count):
                temp = lst[k+1:]
                idx = temp.index(1)
                k = k + idx + 1
        elif command[0] == 'U':
            count = int(command[1])
            for _ in range(count):
                temp = lst[:k]
                temp.reverse()
                idx = temp.index(1)
                index = len(temp) - 1 - idx
                k = index
        elif command[0] == 'C':
            lst[k] = 0
            st.append(k)
            isEnd = sum(lst[k+1:])
            # 선택된 행이 마직막 행일 경우
            if isEnd == 0:
                temp = lst[:k]
                temp.reverse()
                idx = temp.index(1)
                index = len(temp) - 1 - idx
                k = index
            else:
                temp = lst[k+1:]
                idx = temp.index(1)
                k = k + idx + 1
        elif command[0] == 'Z':
            row = st.pop()
            lst[row] = 1
    
    for i in range(n):
        if lst[i]:
            answer += 'O'
        else:
            answer += 'X'
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))