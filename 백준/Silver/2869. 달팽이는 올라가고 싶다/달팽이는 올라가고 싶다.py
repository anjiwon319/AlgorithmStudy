# a : 올라가는 미터 수, b : 미끄러지는 미터 수, v : 나무 막대 총 높이
a, b, v = map(int, input().split(' '))
# 마지막 날 하루 전까지 몇 번 반복되는 지 계산
day = int((v - a) / (a - b))
# day 계산 시 나머지가 있는 경우 고려 : 있으면 1, 없으면 0
extra = 0 if (v - a) % (a - b) == 0 else 1
# 마지막 날까지 합해서 출력
print(day + 1 + extra)
