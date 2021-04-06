def makeTable(pattern):
    patternSize = len(pattern)
    table = [0 for _ in range(patternSize)]
    j = 0
    for i in range(1, patternSize):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def KMP(parent, pattern):
    table = makeTable(pattern)
    parentSize = len(parent)
    patternSize = len(pattern)
    j = 0
    for i in range(parentSize):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == patternSize - 1:
                return True
                # print("[인덱스 %d]에서 매칭 성공!\n", i - patternSize + 2)
                # j = table[j]
            else:
                j += 1
    return False

P = input()
S = input()

if KMP(P, S):
    print(1)
else:
    print(0)