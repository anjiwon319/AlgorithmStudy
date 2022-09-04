# 도비의 난독증 테스트

import sys
input = sys.stdin.readline

words = []
uppers = []
while True:
    n = int(input())
    # 0일시 종료
    if not n:
        break
    word = {}
    for _ in range(n):
        w = input()[:-1]
        word[w.upper()] = w
    words.append(word)

for word in words:
    print(word[sorted(word)[0]])