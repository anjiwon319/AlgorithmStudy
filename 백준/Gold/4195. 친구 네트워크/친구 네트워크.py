# 다시 풀 것

import sys

input = sys.stdin.readline

test_case = int(input())

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(u, v):
    u = find_parent(u)
    v = find_parent(v)

    if u != v:
        parent[v] = u
        network[u] += network[v]
    print(network[u])


for _ in range(test_case):
    n = int(input())
    parent = {}
    network = {}

    for _ in range(n):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            network[a] = 1
        if b not in parent:
            parent[b] = b
            network[b] = 1
        union(a, b)