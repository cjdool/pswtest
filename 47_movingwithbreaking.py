#추가 정보를 다른 데이터로 둘지 array에 축을 1개 더 추가할지 잘 판단할 것

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = []
visited = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]
for _ in range(N):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))
    visited.append([[0]*2 for _ in range(M)])

queue = deque([(0, 0, 1)])
visited[0][0][1] = 1
pos = False

while queue:
    x, y, flag = queue.popleft()

    if x == N-1 and y == M-1:
        pos = True
        print(visited[x][y][flag])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1 and flag == 1:
                visited[nx][ny][0] = visited[x][y][1] + 1
                queue.append((nx, ny, 0))
            elif maze[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                visited[nx][ny][flag] = visited[x][y][flag] + 1
                queue.append((nx, ny, flag))

if not pos:
    print(-1)

'''
6 4
0000
1110
1111
0000
1111
0000


4 4
0111
0000
1111
1110

5 7
0110001
0110101
0110101
0100101
1111100
'''