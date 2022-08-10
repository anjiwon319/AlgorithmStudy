# 블랙잭

import sys
input = sys.stdin.readline

# n(3 ≤ n ≤ 100) m(10 ≤ m ≤ 300,000)
n, m = map(int, input().split())
cards = list(map(int, input().split()))

sums = []
# blackjack : 카드 3장의 합 즉, 나올 수 있는 합들(sums) 중 m보다 작은 최대값
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sums.append(cards[i]+cards[j]+cards[k])

print(max(i for i in set(sums) if i <= m))