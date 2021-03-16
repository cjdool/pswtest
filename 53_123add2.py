import sys

n = int(sys.stdin.readline())

inlist = []
for i in range(n):
    inlist.append(int(sys.stdin.readline()))

m = max(inlist)
lst = [1] * m
lst[1] = 2
lst[2] = 4

for i in range(3, m):
    lst[i] = (lst[i-3] + lst[i-2] + lst[i-1]) % 1000000009

for item in inlist:
    print(lst[item-1])