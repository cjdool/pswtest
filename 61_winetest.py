import sys

n = int(sys.stdin.readline())
inlist = []
for _ in range(n):
    inlist.append(int(sys.stdin.readline()))

if n == 1:
    print(inlist[0])
else:
    lst = [[inlist[0], inlist[0], inlist[0], 0, 0, 0, 0]]
    for i in range(n-1):
        temp = [0] * 7
        x = inlist[i+1]
        temp[0] = max(lst[i][3] + x, lst[i][4] + x)
        temp[1] = max(lst[i][5] + x, lst[i][6] + x)
        temp[2] = max(lst[i][0] + x, lst[i][1] + x)
        temp[3] = lst[i][2]
        temp[4] = max(lst[i][0], lst[i][1])
        temp[5] = max(lst[i][3], lst[i][4])
        temp[6] = max(lst[i][5], lst[i][6])
        lst.append(temp)

    print(max(lst[-1]))
