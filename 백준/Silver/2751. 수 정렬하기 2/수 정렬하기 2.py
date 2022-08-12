# 수 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())

numbers = [int(input()) for i in range(n)]

for i in sorted(numbers):
    print(i)