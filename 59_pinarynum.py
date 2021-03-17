import sys

N = int(sys.stdin.readline())

lst = [[0, 1]]

for i in range(N-1):
    temp = [lst[i][0] + lst[i][1], lst[i][0]]
    lst.append(temp)

print(sum(lst[-1]))