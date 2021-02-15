from itertools import combinations

inlist = list(map(int, input().split()))
N = inlist[0]
S = inlist[1]

inlist = list(map(int, input().split()))

cnt = 0
for i in range(N):
    odx = combinations(inlist, i+1)
    for case in odx:
        if sum(case) == S:
            cnt+=1

print(cnt)