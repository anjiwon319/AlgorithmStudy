import sys
import heapq

input = sys.stdin.readline

def kahn(adj, times):
    n = len(adj) - 1
    result = []

    d = [0] * (n+1)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        for v in adj[i]:
            d[v] += 1
    
    S = []
    for u in range(1, n+1):
        if d[u] == 0:
            heapq.heappush(S, (times[u], u))
            dp[u] = times[u]
    while len(S) != 0:

        t, u = heapq.heappop(S)
        result.append(u)

        for v in adj[u]:
            d[v] -= 1
            dp[v] = max(dp[u] + times[v], dp[v])
            if d[v] == 0:
                heapq.heappush(S, (times[v], v))

    return dp

test_num = int(input())
for _ in range(test_num):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    times = [0] + list(map(int, input().split()))

    for _ in range(m):
        u, v = map(int, input().split())
        edges[u].append(v)

    w = int(input())

    dp = kahn(edges, times)
    print(dp[w])