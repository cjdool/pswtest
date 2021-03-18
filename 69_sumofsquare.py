import sys
import math

N = int(sys.stdin.readline())
M = int(math.sqrt(N))

lst = [1] * 100000
lst[1] = 2
lst[2] = 3

for i in range(2, M+1):
    if (i+1)*(i+1)-1 > 100000:
        cut = 100000
    else:
        cut = (i+1)*(i+1)-1
    for j in range(i*i, cut):
        temp = []
        for k in range(1, i+1):
            temp.append(j-k*k)
        temp = [lst[x] for x in temp]
        lst[j] = 1 + min(temp)

print(lst[N-1])
