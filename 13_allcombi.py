def perm_recur(list, r):
    ret = []
    if r > len(list):
        return ret

    if r == 1:
        for item in list:
            ret.append([item])
    elif r>1:
        for i in range(len(list)):
            temp = [i for i in list]
            temp.remove(list[i])
            for p in perm_recur(temp, r-1):
                ret.append([list[i]]+p)

    return ret

N = int(input())
inlist = [x for x in range(1,N+1)]
outlist = perm_recur(inlist, N)

for row in outlist:
    for col in row:
        print(str(col) + ' ', end='')
    print()