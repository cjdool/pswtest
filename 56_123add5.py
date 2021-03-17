import sys

lst = []
lst.append([1, 0, 0])
lst.append([0, 1, 0])
lst.append([1, 1, 1])

for i in range(3, 100000):
    temp = [(lst[i-1][1] + lst[i-1][2]) % 1000000009, (lst[i-2][0] + lst[i-2][2]) % 1000000009, (lst[i-3][0] + lst[i-3][1]) % 1000000009]
    lst.append(temp)

n = int(sys.stdin.readline())

inlist = []
for i in range(n):
    inlist.append(int(sys.stdin.readline()))

for item in inlist:
    val = sum(lst[item-1]) % 1000000009
    print(val)