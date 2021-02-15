from itertools import permutations

N = int(input())

W = []
for i in range(N):
    instr = input()
    inlist = instr.split()
    W.append([int(x) for x in inlist])

idx = [x for x in range(N)]
cost = 100000000
odx = map(list, permutations(idx))

for case in odx:
    tempcost = 0
    for i in range(-1, len(case)-1):
        if W[case[i]][case[i+1]] == 0:
            tempcost = -1
            break
        else:
            tempcost += W[case[i]][case[i+1]]
    if tempcost != -1 and tempcost < cost:
        cost = tempcost

print(cost)
