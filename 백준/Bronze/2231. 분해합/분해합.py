# 분해합

import sys

input = sys.stdin.readline
n = int(input())
min_m = 0

def find_m_sum(m):
    m_str = str(m)
    return m + sum([int(m_str[i]) for i in range(len(m_str))])

for m in range(n):
    if find_m_sum(m) == n:
        min_m = m
        break
    min_m = 0

print(min_m)