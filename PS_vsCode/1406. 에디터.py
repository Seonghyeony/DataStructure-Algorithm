from collections import deque

stack1 = deque(input())
stack2 = deque()
M = int(input())

for _ in range(M):
    command = list(input())
    if len(command) == 1:
        if command[0] == 'L':
            if len(stack1) == 0:
                continue
            stack2.append(stack1.pop())
        elif command[0] == 'D':
            if len(stack2) == 0:
                continue
            stack1.append(stack2.pop())
        elif command[0] == 'B':
            if len(stack1) == 0:
                continue
            stack1.pop()
    else:
        stack1.append(command[2])
stack2.reverse()
result = list(stack1) + list(stack2)
print(''.join(result))