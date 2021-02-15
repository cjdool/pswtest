from itertools import product


inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]

nlist = list(map(int, input().split()))
nlist.sort()

for case in product(nlist, repeat=M):
    print(' '.join(map(str, case)))