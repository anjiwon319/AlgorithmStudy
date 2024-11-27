import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v)]
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, c))

def find_parent(u):
    if parent[u] != u:
        parent[u] = find_parent(parent[u])
    return parent[u]

def union(u, v):
    u = find_parent(u)
    v = find_parent(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

edges.sort(key=lambda x: x[2])
total_cost = 0

for a, b, cost in edges:
    if find_parent(a) != find_parent(b):
        union(a, b)
        total_cost += cost

print(total_cost)