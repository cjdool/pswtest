import sys

N = int(sys.stdin.readline())
inlist = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(inlist[0])
else:
    lst = [x for x in inlist]

    for i in range(N-2, -1, -1):
        for j in range(i+1, N):
            if inlist[i] < inlist[j] and lst[i] < lst[j]+inlist[i]:
                lst[i] = lst[j] + inlist[i]

    print(max(lst))