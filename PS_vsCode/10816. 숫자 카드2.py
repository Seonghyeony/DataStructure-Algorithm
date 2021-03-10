N = int(input())
cards = list(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

card_dict = dict()
for card in cards:
    if card_dict.get(card, False):
        card_dict[card] += 1
    else:
        card_dict[card] = 1

for ret in lst:
    print(card_dict.get(ret, 0), end=' ')
