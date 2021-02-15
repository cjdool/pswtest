from itertools import permutations

N = int(input())
Alist = [int(x) for x in input().split()]
Olist = [int(x) for x in input().split()]

idx = []
for i in range(Olist[0]):
    idx.append(1)
for i in range(Olist[1]):
    idx.append(2)
for i in range(Olist[2]):
    idx.append(3)
for i in range(Olist[3]):
    idx.append(4)

odx = list(set(permutations(idx)))
minval = 1000000000
maxval = -1000000000
for case in odx:
    caseval = Alist[0]
    for i in range(N-1):
        if case[i] == 1:
            caseval += Alist[i+1]
        elif case[i] == 2:
            caseval -= Alist[i+1]
        elif case[i] == 3:
            caseval *= Alist[i+1]
        else:
            caseval = int(caseval/Alist[i+1])
    minval = min(minval, caseval)
    maxval = max(maxval, caseval)

print(maxval)
print(minval)
