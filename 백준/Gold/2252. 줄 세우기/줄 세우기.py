import sys

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
            S.append(u)
    while len(S) != 0:
        u = S.pop()
        result.append(u)

        for v in adj[u]:
            d[v] -= 1
            if d[v] == 0:
                S.append(v)
    return result

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)

result = kahn(edges)
print(*result, sep=' ')