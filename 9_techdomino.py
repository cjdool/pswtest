def findmaxandadd(sum, lst):
    return sum + max(lst)

instr = input()
inlist = instr.split()
N = int(inlist[0])
M = int(inlist[1])

papermap = []
for i in range(N):
    instr = input()
    inlist = instr.split()
    papermap.append([int(x) for x in inlist])

maxval = 0
#  case1
for row in papermap:
    for i in range(M-3):
        temp = sum(row[i:i+4])
        if maxval < temp:
            maxval = temp

#  case2
for j in range(M):
    for i in range(N-3):
        temp = papermap[i][j] + papermap[i+1][j] + papermap[i+2][j] + papermap[i+3][j]
        if maxval < temp:
            maxval = temp

#  case3
for i in range(N-1):
    for j in range(M-1):
        temp = papermap[i][j] + papermap[i][j+1] + papermap[i+1][j] + papermap[i+1][j+1]
        if maxval < temp:
            maxval = temp

#  case4
for i in range(N):
    for j in range(M-2):
        temp = papermap[i][j] + papermap[i][j+1] + papermap[i][j+2]
        if i == 0:
            p1 = papermap[i+1][j]
            p2 = papermap[i+1][j+1]
            p3 = papermap[i+1][j+2]
            temp = findmaxandadd(temp, [p1, p2, p3])
        elif i == N-1:
            p1 = papermap[i-1][j]
            p2 = papermap[i-1][j+1]
            p3 = papermap[i-1][j+2]
            temp = findmaxandadd(temp, [p1, p2, p3])
        else:
            p1 = papermap[i-1][j]
            p2 = papermap[i-1][j+1]
            p3 = papermap[i-1][j+2]
            p4 = papermap[i+1][j]
            p5 = papermap[i+1][j+1]
            p6 = papermap[i+1][j+2]
            temp = findmaxandadd(temp, [p1, p2, p3, p4, p5, p6])
        if maxval < temp:
            maxval = temp

#  case5
for j in range(M):
    for i in range(N-2):
        temp = papermap[i][j] + papermap[i+1][j] + papermap[i+2][j]
        if j == 0:
            p1 = papermap[i][j+1]
            p2 = papermap[i+1][j+1]
            p3 = papermap[i+2][j+1]
            temp = findmaxandadd(temp, [p1, p2, p3])
        elif j == M-1:
            p1 = papermap[i][j-1]
            p2 = papermap[i+1][j-1]
            p3 = papermap[i+2][j-1]
            temp = findmaxandadd(temp, [p1, p2, p3])
        else:
            p1 = papermap[i][j+1]
            p2 = papermap[i+1][j+1]
            p3 = papermap[i+2][j+1]
            p4 = papermap[i][j-1]
            p5 = papermap[i+1][j-1]
            p6 = papermap[i+2][j-1]
            temp = findmaxandadd(temp, [p1, p2, p3, p4, p5, p6])
        if maxval < temp:
            maxval = temp

#  case6
for i in range(N-2):
    for j in range(M-1):
        temp = papermap[i+1][j] + papermap[i+1][j+1]
        p1 = papermap[i][j] + papermap[i+2][j+1]
        p2 = papermap[i][j+1] + papermap[i+2][j]
        temp = findmaxandadd(temp, [p1, p2])
        if maxval < temp:
            maxval = temp

#  case7
for j in range(M-2):
    for i in range(N-1):
        temp = papermap[i][j+1] + papermap[i+1][j+1]
        p1 = papermap[i][j] + papermap[i+1][j+2]
        p2 = papermap[i+1][j] + papermap[i][j+2]
        temp = findmaxandadd(temp, [p1, p2])
        if maxval < temp:
            maxval = temp

print(maxval)