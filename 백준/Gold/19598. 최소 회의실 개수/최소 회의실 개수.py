import heapq as hq

n = int(input())
meetings = []
cnt = 0

for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x : (x[0], x[1]))
rooms = [meetings[0][1]]
cnt += 1

for i in range(1, n):
    start, end = map(int, meetings[i])
    if rooms and rooms[0] <= start:
        hq.heappop(rooms)
    else:
        cnt += 1
    hq.heappush(rooms, end)

print(cnt)