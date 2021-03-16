import sys

n = int(sys.stdin.readline())

lst = [1] * 11
lst[1] = 2
lst[2] = 4

for i in range(3, 11):
    lst[i] = lst[i-3] + lst[i-2] + lst[i-1]

inlist = []
for i in range(n):
    inlist.append(int(sys.stdin.readline()))

for item in inlist:
    print(lst[item-1])