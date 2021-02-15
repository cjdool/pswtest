from itertools import product

inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]

nlist = list(set(map(int, input().split())))
nlist.sort()
olist = product(nlist, repeat=M)

for case in olist:
    print(' '.join(map(str, case)))