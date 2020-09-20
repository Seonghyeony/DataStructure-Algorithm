S, tmp = input(), ""
ck = False
ans = ""

for i in S:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + " "
            tmp = ""
        else:
            ans += " "
    elif i == '<':
        ck = True
        ans += tmp[::-1] + '<'
        tmp = ""
    elif i == '>':
        ck = False
        ans += '>'
    else:
        if ck:
            ans += i
        else:
            tmp += i
ans += tmp[::-1]
print(ans)


# S = input()

# if S.find('<') == -1:
#     lst = S.split()
#     for string in lst:
#         print(string[::-1], end=' ')
# else:
#     result, tmp = '', ''
#     state = True
#     for ch in S:
#         if ch == '<' and state:
#             if len(tmp) == 0:
#                 tmp += '<'
#             else:
#                 result += tmp[::-1]
#                 tmp = '<'
#             state = False
#             continue

#         if not state and ch != '>':
#             tmp += ch
#             continue

#         if ch == '>' and not state:
#             tmp += ch
#             state = True
#             result += tmp
#             tmp = ''
#             continue
        
#         if ch == ' ':
#             result += tmp[::-1]
#             result += ' '
#             tmp = ''
#         else:
#             tmp += ch
#     if len(tmp):
#         result += tmp

#     print(result)




