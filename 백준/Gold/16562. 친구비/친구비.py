import sys

input = sys.stdin.readline

n, m , k = map(int, input().split())
fee_friend = list(map(int, input().split()))
parent = [i for i in range(n)]

def find_parent(u):
    if parent[u] != u:
        parent[u] = find_parent(parent[u])
    return parent[u]

def union(u, v):
    u = find_parent(u)
    v = find_parent(v)
    if fee_friend[u] < fee_friend[v]:
        parent[v] = u
    else:
        parent[u] = v

for i in range(m):
    u, v = map(int, input().split())
    if u == v : continue

    u -= 1
    v -= 1

    union(u, v)

friends = set(find_parent(i) for i in range(n))
fee_sum = 0
for f in friends:
    fee_sum += fee_friend[f]

if fee_sum > k:
    print("Oh no")
else:
    print(fee_sum)