# 뒤집기

import sys
input = sys.stdin.readline

def count_flip(cards_len, index):
    count = 1
    if cards_len == len(index):
        return 0
    for i in range(len(index)-1):
        if index[i+1] != index[i] + 1:
            count += 1
    return count

# main
cards = input()[:-1]
cards_len = len(cards)
index_0 = [i for i, num in enumerate(cards) if num == '0']
index_1 = [i for i, num in enumerate(cards) if num == '1']

count_0 = count_flip(cards_len, index_0)
count_1 = count_flip(cards_len, index_1)
print(count_0 if count_1 > count_0 else count_1)
    