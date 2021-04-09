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
    '(': 1, ')': 1
}

def transition(S):
    opStack = ArrayStack()
    ret = []

    for word in S:
        if word == '(':
            opStack.push(word)
        elif word == ')':
            while opStack.peek() != '(':
                ret.append(opStack.pop())
            opStack.pop()
        elif word in '+-*/':
            while opStack.size() > 0:
                if priority[opStack.peek()] >= priority[word]:
                    ret.append(opStack.pop())
                else:
                    break
            opStack.push(word)
        else:
            ret.append(word)
    
    while not opStack.isEmpty():
        ret.append(opStack.pop())

    return ret

def calc(tokenList):
    valStack = ArrayStack()
    ret = 0
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
    lst = input()
    prefix = transition(lst)
    print('#{} {}'.format(test_case, calc(prefix)))
    break
