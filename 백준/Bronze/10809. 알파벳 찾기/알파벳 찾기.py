# 10809 - 알파벳 찾기

import string

lowers = string.ascii_lowercase

word = input()

# find 와 index 의 차이 중요
for i in range(len(lowers)):
    print(word.find(lowers[i]), end = ' ')

