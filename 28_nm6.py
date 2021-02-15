from itertools import combinations

inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]

nlist = list(map(int, input().split()))
nlist.sort()

for case in combinations(nlist, M):
    print(' '.join(map(str, case)))