import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

queue = deque([])
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

result = box[x][y]

flag = True
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            flag = False
            break

print(result - 1 if flag else -1)