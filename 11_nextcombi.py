N = int(input())
instr = input()
inlist = instr.split()
inlist = [int(x) for x in inlist]

if N == 1:
    print(-1)
else:
    newlist = []
    flag = 0
    i = len(inlist) - 1
    while True:
        ii = i
        i -= 1
        if inlist[i] < inlist[ii]:
            j = len(inlist) - 1
            while inlist[i] >= inlist[j]:
                j -= 1
            inlist[i], inlist[j] = inlist[j], inlist[i]
            partlist = list(reversed(inlist[ii:]))
            newlist = list(map(str, inlist[0:ii] + partlist))
            break
        if i == 0:
            flag = 1
            break
    if flag == 1:
        print(-1)
    else:
        print(' '.join(newlist))