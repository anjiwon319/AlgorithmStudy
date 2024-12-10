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

def find_min_len(L, catchphrase):
    lps = compute_lps(catchphrase)
    return L - lps[L-1]

L = int(input().strip())
catchphrase = input().strip()

print(find_min_len(L, catchphrase))