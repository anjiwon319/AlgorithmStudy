# 단어 공부

import sys
from collections import Counter
input = sys.stdin.readline

words = Counter(input()[:-1].upper())
count = 0
for i in words:
    if words[i] == max(words.values()):
        frequency = i
        count += 1
print(frequency if count == 1 else '?') 