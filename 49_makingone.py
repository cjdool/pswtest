import sys

X = int(sys.stdin.readline())
lst = [0] * (X+1)
retval = 0

if X == 1:
    retval = 0
elif X == 2:
    retval = 1
elif X == 3:
    retval = 1
else:
    lst[2] = 1
    lst[3] = 1
    for i in range(4, X+1):
        lst[i] = lst[i-1] + 1
        if i % 3 == 0 and lst[int(i/3)]+1 < lst[i]:
            lst[i] = lst[int(i/3)] + 1
        if i % 2 == 0 and lst[int(i/2)]+1 < lst[i]:
            lst[i] = lst[int(i/2)] + 1

    retval = lst[X]

print(retval)