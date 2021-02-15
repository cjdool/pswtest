def perm_recur (list, r):
    ret = []
    if len(list) < r:
        return ret

    if r == 1:
        for item in list:
            ret.append([item])
    elif r > 1:
        for item in list:
            for p in perm_recur(list, r-1):
                ret.append([item]+p)

    return ret


inlist = list(map(int, input().split()))
N = inlist[0]
M = inlist[1]

idx = []
for i in range(1, N+1):
    idx.append(i)

for case in perm_recur(idx, M):
    print(' '.join(map(str, case)))