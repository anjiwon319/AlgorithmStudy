# 수 정렬하기 3 - input 시 메모리 초과에 유의

import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num_dict = {}

for i in range(n):
    number = int(input())
    if number in num_dict:
        num_dict[number] += 1
    else:
        num_dict[number] = 1

for key, value in sorted(num_dict.items()):
    for i in range(value):
        print(key)