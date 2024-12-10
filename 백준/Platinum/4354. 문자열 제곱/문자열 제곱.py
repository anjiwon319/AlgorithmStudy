import sys

input = sys.stdin.readline

def compute_lps(P):
    m = len(P)
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and P[i] != P[j]:
            j = lps[j-1]
        if P[i] == P[j]:
            j += 1
            lps[i] = j

    return lps

def find_max_repeat(s):
    L = len(s)
    lps = compute_lps(s)
    prefix_len = lps[-1]
    a_len = L - prefix_len

    if L % a_len == 0:
        return L // a_len
    else:
        return 1

while True:
    s = input().strip()
    if s == ".":
        break
    print(find_max_repeat(s))