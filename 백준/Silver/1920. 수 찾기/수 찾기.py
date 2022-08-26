# 수 찾기

import sys
input = sys.stdin.readline

a = int(input())
a_set = set(map(int, input().split()))


m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in a_set:
        print(1)
    else:
        print(0)