'''
for test_case in range(1, int(input()) + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    result = set([0])
    for i in scores:
        score = list()
        for j in result:
            if i + j not in result:
                score.append(i + j)
        for j in score:
            result.add(j)
    print('#{} {}'.format(test_case, len(result)))
'''

for test_case in range(1, int(input()) + 1):
    n = int(input())
    scores = list(map(int, input().split()))

    # 가능한 최대 점수까지 리스트를 만들어준다.
    # 인덱스는 내가 얻을 수 있는 점수
    my_scores = [0] * (sum(scores) + 1)
    my_scores[0] = 1

    for score in scores:
        # 만들어둔 리스트의 뒤에서부터 앞으로 하나씩 본다.
        for i in range(len(my_scores) - score, -1, -1):
            # 이미 내가 가능한 점수가 내 점수 리스트에 있으면
            if my_scores[i]:
                # 그 점수에 방금 얻은 점수를 더해서 그 점수에 해당하는 인덱스를 1로 만든다.
                my_scores[i + score] = 1
    
    print('#{} {}'.format(test_case, sum(my_scores)))