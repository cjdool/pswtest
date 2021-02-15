def perm_recur(list, r):
    ret = []
    if len(list) < r:
        return ret

    if r == 1:
        for item in list:
            ret.append([item])
    elif r > 1:
        for i in range(len(list)):
            temp = [x for x in list]
            temp.remove(list[i])
            for p in perm_recur(temp, r-1):
                ret.append([list[i]]+p)

    return ret

N = int(input())
instr = input()
inlist = instr.split()
inlist = [int(x) for x in inlist]
idxlist = [x for x in range(N)]
outlist = perm_recur(idxlist, N)

cost = 0
for case in outlist: # 3 4 0 2 1
    tempcost = 0
    for i in range(N-1):
        tempcost += abs(inlist[case[i]] - inlist[case[i+1]])
    if tempcost > cost:
        cost = tempcost

print(cost)