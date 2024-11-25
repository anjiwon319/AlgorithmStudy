n = int(input())
cnt = 0
meetings = []

for i in range(n):
    meetings.append(tuple(map(int, input().split())))
    
meetings.sort(key=lambda x : (x[1], x[0]))
pre_end = 0
for start, end in meetings:
    if start < pre_end:
        continue
    cnt += 1
    pre_end = end

print(cnt)