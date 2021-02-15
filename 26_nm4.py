def combi_recur(list, r):
    ret = []

    if r == 1:
        for item in list:
            ret.append([item])
    elif r > 1:
        for i in range(len(list)):
            for temp in combi_recur(list[i:], r-1):
                ret.append([list[i]]+temp)

    return ret

inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]

idx = []
for i in range(1, N+1):
    idx.append(i)

olist = combi_recur(idx, M)

for case in olist:
    print(' '.join(map(str, case)))