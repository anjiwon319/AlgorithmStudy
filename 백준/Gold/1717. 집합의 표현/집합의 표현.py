
import sys

def make_set(n):
    return [i for i in range(n + 1)]

def union(u, v):
    u = find_set(u)
    v = find_set(v)
    if u != v:
        parent[v] = u

def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]

n, m = map(int, sys.stdin.readline().split())
parent = make_set(n)
    
for line in sys.stdin:
    operation, u, v = map(int, line.split()) 

    if operation == 0:
        union(u, v) 

    elif operation == 1:
        if find_set(u) == find_set(v): 
            print("YES")
        else: 
            print("NO")