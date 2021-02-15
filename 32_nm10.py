from itertools import combinations

inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]

nlist = list(map(int, input().split()))
nlist.sort()
olist = list(set(combinations(nlist, M)))
olist.sort()

for case in olist:
    print(' '.join(map(str, case)))