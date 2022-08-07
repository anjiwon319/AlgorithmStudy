# 단어 정렬

import sys
# 빠른 입력
input = sys.stdin.readline

n = int(input())
words = [input().replace('\n', '') for i in range(n)]
# 중복 제거 및 단어 정렬(짧은 길이 우선)
for word in sorted(set(words), key = lambda x :(len(x), x)):
    print(word)