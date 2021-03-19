# 다시 풀기
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    case = []
    case.append(list(map(int, sys.stdin.readline().split())))
    case.append(list(map(int, sys.stdin.readline().split())))

    if n == 1:
        print(max(case[0][0], case[1][0]))
    else:
        case[0][1] += case[1][0]
        case[1][1] += case[0][0]

        for i in range(2,n):
            case[0][i] += max(case[1][i-2], case[1][i-1])
            case[1][i] += max(case[0][i-2], case[0][i-1])

        print(max(case[0][n-1], case[1][n-1]))
