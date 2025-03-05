heights = sorted([int(input()) for _ in range(9)])
total = sum(heights)

gap = total - 100
spys = ()
for i in range(9):
    for j in range(1, 9):
        if heights[i] + heights[j] == gap:
            spys = (i, j)
            break

for i in range(9):
    if i not in spys:
        print(heights[i])

