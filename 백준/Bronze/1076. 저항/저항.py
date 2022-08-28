# 저항

import sys
input = sys.stdin.readline

colors = ['black', 'brown', 'red', 'orange', 'yellow',
          'green', 'blue', 'violet', 'grey', 'white']

resistance = (colors.index(input()[:-1]) * 10 + colors.index(input()[:-1])) * 10 ** colors.index(input()[:-1])
print(resistance)