import sys

N = int(sys.stdin.readline())
inlist = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(1)
else:
    lst = [1] * N

    for i in range(N-2, -1, -1):
        for j in range(i+1, N):
            if inlist[i] < inlist[j] and lst[i] < lst[j]+1:
                lst[i] = lst[j] + 1

    print(max(lst))