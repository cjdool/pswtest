def combi_recur(list, r):
    ret = []
    if len(list) < r:
        return ret

    if r == 1:
        for item in list:
            ret.append([item])
    elif r > 1:
        for i in range(len(list)-r+1):
            for p in combi_recur(list[i+1:], r-1):
                ret.append([list[i]]+p)

    return ret


inlist = input().split()
L = int(inlist[0])
C = int(inlist[1])
inlist = input().split()
inlist.sort()

vowels = {'a', 'e', 'i', 'o', 'u'}
outlist = combi_recur(inlist, L)

for case in outlist:
    vowelcnt = 0
    for letter in case:
        if letter in vowels:
            vowelcnt += 1

    if 0 < vowelcnt < L-1:
        print(''.join(case))

