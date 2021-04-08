class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def transition(S):
    opStack = ArrayStack()
    answer = []

    for char in S:
        # '('이면 스택에 push
        if char == '(':
            opStack.push(char)
        
        # ')'이면 '('가 나올 때까지 pop, 출력
        elif char == ')':
            while opStack.peek() != '(':
                answer.append(opStack.pop())
            opStack.pop()
        
        # 연산자가 나올 경우
        elif char in '+-*/':
            # 스택이 비어있으면 push
            if opStack.isEmpty():
                opStack.push(char)
            # 비어있지 않다면 비교
            else:
                while opStack.size() > 0:
                    # 우선 순위 비교 후 밖에 있는 놈이 낮으면 꺼내고 계속 비교
                    if prec[opStack.peek()] >= prec[char]:
                        answer.append(opStack.pop())
                    # 우선 순위가 밖에 있는 놈이 높으면 반복문 탈출
                    else:
                        break
                opStack.push(char)
        # 피연산자일 경우
        else:
            answer.append(char)
    
    # 스택이 빌 때 까지 pop
    while not opStack.isEmpty():
        answer.append(opStack.pop())

    return answer

def calc(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        # 피연산자를 만나면 스택에 push
        if token in '0123456789':
            valStack.push(int(token))
        
        # 연산자를 만나면
        elif token == '+':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2 + n1)
        elif token == '-':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2 - n1)
        elif token == '*':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2 * n1)
        elif token == '/':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2 // n1)

    return valStack.pop()

for test_case in range(1, 11):
    N = int(input())
    S = input()
    prefix = transition(S)
    print('#{} {}'.format(test_case, calc(prefix)))
    