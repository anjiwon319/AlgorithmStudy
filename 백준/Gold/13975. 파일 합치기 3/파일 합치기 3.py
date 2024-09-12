import heapq as hq

t = int(input())
sizes = []
tmp_sizes = []

for i in range(t):
    n = int(input())
    sizes.append(sorted(list(map(int, input().split()))))

for case in sizes:
    sum = 0

    while len(case) > 1:
        X1 = hq.heappop(case)
        X2 = hq.heappop(case)

        sum += X1+X2
        hq.heappush(case, X1+X2)
    print(sum)