from itertools import permutations

inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]

nlist = list(map(int, input().split()))
olist = list(set(permutations(nlist, M)))
olist.sort()

for case in olist:
    print(' '.join(map(str, case)))

'''
import sys
def f(n, m, l, s):
    if len(s) == m:
        print(' '.join([str(i) for i in s]))
        return
    i = 0
    while i < len(l):
        s.append(l[i])
        while i + 1 < len(l) and l[i] == l[i + 1]:
            i += 1
        f(n - 1, m, l[:i] + l[(i + 1):], s)
        s.pop()
        i += 1

input = sys.stdin.readline
N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
S = []
f(N, M, L, S)
'''