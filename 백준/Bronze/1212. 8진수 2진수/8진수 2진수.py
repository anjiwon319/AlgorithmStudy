# oct to bin
import sys
input = sys.stdin.readline

oct = int('0o'+input()[:-1], 8)
print(format(oct, 'b'))