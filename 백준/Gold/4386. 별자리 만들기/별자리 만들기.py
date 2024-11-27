import sys

input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n+1)]
stars = [tuple(map(float, input().split())) for _ in range(n)]

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

def get_distance(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2
    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

nodes = []

for i in range(n-1):
    for j in range(i+1, n):
        nodes.append((get_distance(stars[i], stars[j]), i, j))

nodes.sort()
total_cost = 0

for cost, u, v in nodes:
    if find_parent(u) != find_parent(v):
        union(u, v)
        total_cost += cost

print(f"{total_cost:.2f}")