# 직사각형에서 탈출

x, y, w, h = map(int, input().split(' '))

# a : x축으로의 최단 거리, b : y축으로의 최단 거리
a = (w - x) if x >= w/2 else x
b = (h - y) if y >= h/2 else y

# a, b 둘 중 작은 값이 최단 거리가 됨 
print(a if a < b else b)