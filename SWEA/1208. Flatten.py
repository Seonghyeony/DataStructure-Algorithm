for test_case in range(1, 11):
    n, lst = int(input()), list(map(int, input().split()))
    
    high, low = 0, 0
    for _ in range(n):
        high, low = max(lst), min(lst)
        if high - low == 0:
            break
        if high - low == 1:
            break

        high_idx, low_idx = lst.index(high), lst.index(low)
        lst[high_idx] -= 1
        lst[low_idx] += 1

    print(f"#{test_case} {max(lst) - min(lst)}")
        


