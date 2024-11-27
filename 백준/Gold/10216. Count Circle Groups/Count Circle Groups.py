import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

test_case = int(input())

def find_parent(u):
    if parent[u] != u:
        parent[u] = find_parent(parent[u])
    return parent[u]

def union(u, v):
    u = find_parent(u)
    v = find_parent(v)
    if u != v:
        parent[u] = v

def get_distance(loc1, loc2):
    x1, y1, _ = loc1
    x2, y2, _ = loc2
    return (x1 - x2)**2 + (y1 - y2)**2

for _ in range(test_case):
    n = int(input())
    parent = [i for i in range(n)]
    locations = [tuple(map(int, input().split())) for _ in range(n)]

    ans = n
    for i in range(n-1):
        for j in range(i + 1, n):
            if get_distance(locations[i], locations[j]) <= (locations[i][2] + locations[j][2])**2:
                if find_parent(i) != find_parent(j):
                    union(i, j)
                    ans -= 1
    print(ans)