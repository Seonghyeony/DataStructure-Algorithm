class ArrayStack():
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

priority = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def transition(S):
    opStack = ArrayStack()
    answer = []

    # 문자열을 탐색해서
    for word in S:
        if word == '(':
            opStack.push(word)
        elif word == ')':
            while opStack.peek() != '(':
                answer.append(opStack.pop())
            opStack.pop()
        elif word in '+-/*':
            if opStack.isEmpty():
                opStack.push(word)
            else:
                while opStack.size() > 0:
                    if priority[opStack.peek()] >= priority[word]:
                        answer.append(opStack.pop())
                    else:
                        # 밖에 있는 놈이 우선순위가 더 높으면 빠져나온다.
                        break
                opStack.push(word)
        else:
            answer.append(word)
    
    while not opStack.isEmpty():
        answer.append(opStack.pop())

    return answer

def calc(tokenList):
    valStack = ArrayStack()
    for token in tokenList:
        if token in '0123456789':
            valStack.push(int(token))
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
    # print(prefix)
    print('#{} {}'.format(test_case, calc(prefix)))
