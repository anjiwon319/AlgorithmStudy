import sys
import heapq

input = sys.stdin.readline

def kahn(adj):
    n = len(adj) - 1
    result = []

    d = [0] * (n+1)
    for i in range(1, n+1):
        for v in adj[i]:
            d[v] += 1
    
    S = []
    for u in range(1, n+1):
        if d[u] == 0:
            heapq.heappush(S, u)
    while len(S) != 0:
        u = heapq.heappop(S)
        result.append(u)

        for v in adj[u]:
            d[v] -= 1
            if d[v] == 0:
                heapq.heappush(S, v)

    return result

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)

result = kahn(edges)
print(*result)