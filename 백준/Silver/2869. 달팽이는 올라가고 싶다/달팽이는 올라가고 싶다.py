a, b, v = map(int, input().split(' '))
day = int((v - a) / (a - b))
extra = 0 if (v - a) % (a - b) == 0 else 1

print(day + 1 + extra)