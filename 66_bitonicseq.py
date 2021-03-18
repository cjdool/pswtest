import sys
N = int(sys.stdin.readline())
inlist = list(map(int, sys.stdin.readline().split()))

lst = [1] * N
lst2 = [1] * N

for i in range(N):
    for j in range(i):
        if inlist[i] > inlist[j] and lst[i] < lst[j]+1:
            lst[i] = lst[j] + 1

inlist.reverse()
for i in range(N):
    for j in range(i):
        if inlist[i] > inlist[j] and lst2[i] < lst2[j]+1:
            lst2[i] = lst2[j] + 1
lst2.reverse()

result = [sum(x) - 1 for x in zip(lst, lst2)]

print(max(result))