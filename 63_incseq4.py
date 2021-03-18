import sys

N = int(sys.stdin.readline())
inlist = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(1)
    print(inlist[0])
else:
    lst = [1] * N
    lst2 = []
    for item in inlist:
        lst2.append([item])

    for i in range(N):
        for j in range(i):
            if inlist[i] > inlist[j] and lst[i] < lst[j]+1:
                lst[i] = lst[j] + 1
                lst2[i] = lst2[j] + [inlist[i]]

    x = max(lst)
    ind = lst.index(x)
    print(x)
    print(*lst2[ind])