import sys

N = int(sys.stdin.readline())

lst = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

if N == 1:
    print(9)
else:
    for i in range(N-1):
        temp = [0] * 10
        temp[0] = lst[i][1]
        temp[9] = lst[i][8]
        for j in range(1, 9):
            temp[j] = lst[i][j-1] + lst[i][j+1]
        lst.append(temp)

    print(sum(lst[-1]) % 1000000000)