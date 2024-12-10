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

def kmp_search(T, P):
    T += T[:-1]
    n, m = len(T), len(P)
    lps = compute_lps(P)

    count = 0 
    j = 0

    for i in range(n):
        while j > 0 and T[i] != P[j]:
            j = lps[j-1]
        if T[i] == P[j]:
            j += 1
        if j == m:
            count += 1
            j = lps[j-1]

    return count


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N = int(input())
meat_phrase = ''.join(input().strip().split())
currnent_phrase =  ''.join(input().strip().split())

count = kmp_search(currnent_phrase, meat_phrase)
d = gcd(N, count)
N //= d
count //= d
print(f"{count}/{N}")