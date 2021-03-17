import sys

N = int(sys.stdin.readline())

lst = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

if N == 1:
    print(10)
else:
    for i in range(N-1):
        temp = [0] * 10
        for j in range(10):
            temp[j] = sum(lst[i][j:])
        lst.append(temp)

    print(sum(lst[-1]) % 10007)