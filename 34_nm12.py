from itertools import combinations_with_replacement

inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]

nlist = list(set(map(int, input().split())))
nlist.sort()
olist = combinations_with_replacement(nlist, M)

for case in olist:
    print(' '.join(map(str, case)))