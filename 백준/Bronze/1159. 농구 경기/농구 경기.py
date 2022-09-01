# 농구 경기

import sys
input = sys.stdin.readline

num = int(input())
players = {}
for i in range(num):
    player = input()[:-1]
    if player[0] not in players:
        players[player[0]] = [player]
    else:
        players[player[0]].append(player)

participate = []
for k, v in players.items():
    if len(v) >= 5:
        participate.append(k)

print(*sorted(participate), sep='') if participate else print("PREDAJA")