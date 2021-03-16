import sys

N = int(sys.stdin.readline())

inlist = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    for j in range(int((i+1)/2)):
        if inlist[i] > inlist[j] + inlist[i-j-1]:
            inlist[i] = inlist[j] + inlist[i-j-1]

print(inlist[-1])