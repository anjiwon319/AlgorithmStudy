# 카드2

import sys
from collections import deque
# 빠른 입력
input = sys.stdin.readline
n = int(input())
cards = deque([i+1 for i in range(n)])

for i in range(n-1):
  cards.popleft()
  cards.append(cards.popleft())
print(cards.pop())