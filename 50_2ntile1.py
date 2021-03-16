import sys

n = int(sys.stdin.readline())
lst = [1] * n
if n == 1:
    print(1)
else:
    lst[1] = 2

    for i in range(2, n):
        lst[i] = lst[i-1] + lst[i-2]

    print(lst[n-1] % 10007)