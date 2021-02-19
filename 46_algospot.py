# dijkstra로 다시 풀것

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
maze = []
cost = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]
for _ in range(N):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))
    cost.append([-1]*M)

queue = deque([(0, 0)])
cost[0][0] = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if cost[nx][ny] == -1 and maze[nx][ny] == 0:
                cost[nx][ny] = cost[x][y]
                queue.append((nx, ny))
            elif cost[nx][ny] == -1 and maze[nx][ny] == 1:
                cost[nx][ny] = cost[x][y] + 1
                queue.append((nx, ny))
            else: # cost[nx][ny] != -1
                if maze[nx][ny] == 0 and cost[x][y] < cost[nx][ny]:
                    cost[nx][ny] = cost[x][y]
                    queue.append((nx, ny))
                elif cost[x][y]+1 < cost[nx][ny]:
                    cost[nx][ny] = cost[x][y]+1
                    queue.append((nx, ny))


print(cost[N-1][M-1])


'''
25 2
0100010001000100010001000
0001000100010001000100010
'''