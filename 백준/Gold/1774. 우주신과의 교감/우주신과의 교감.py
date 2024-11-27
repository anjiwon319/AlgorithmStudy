import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(u, v):
    u = find_parent(u)
    v = find_parent(v)

    if u != v:
        parent[v] = u
    else:
        parent[u] = v

def get_distance(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2
    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5


locations = [0] + [tuple(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

edges = []
for i in range(1, n):
    for j in range(i+1, n+1):
        edges.append((get_distance(locations[i], locations[j]), i, j))

edges.sort()
total_cost = 0

for cost, u, v in edges:
    if find_parent(u) != find_parent(v):
        union(u, v)
        total_cost += cost

print(f"{total_cost:.2f}")