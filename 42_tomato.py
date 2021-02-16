import sys

M, N = map(int, sys.stdin.readline().split())
box = []
visited = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))
    visited.append([-1] * M)

queue = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 0

while queue:
    x, y = queue.pop(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == -1 and box[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


maxval = -1
flag = True
for i in range(N):
    for j in range(M):
        if box[i][j] == 0 and visited[i][j] == -1:
            flag = False
            break
        maxval = max(maxval, visited[i][j])
print(maxval if flag else -1)