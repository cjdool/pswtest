import sys

n = int(sys.stdin.readline())
lst = [1] * n
if n == 1:
    print(1)
else:
    lst[1] = 3

    for i in range(2, n):
        lst[i] = (lst[i-1] + 2*lst[i-2])%10007

    print(lst[-1])