import sys

N, M = map(int, sys.stdin.readline().split())
smeb = []
visited =[]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(N):
    smeb.append(list(map(int, list(sys.stdin.readline().strip()))))
    visited.append([0]*M)

queue = [(0, 0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and smeb[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))



'''
mincnt = 10000000

def basic_dfs(curx, cury, cnt):
    global mincnt
    if curx == N-1 and cury == M-1:
        cnt += 1
        mincnt = min(mincnt, cnt)
        return

    if smeb[curx][cury] == 0:
        return

    if not visited[curx][cury]:
        visited[curx][cury] = True
        cnt += 1
        if curx != N-1:
            basic_dfs(curx+1, cury, cnt)
        if cury != M-1:
            basic_dfs(curx, cury+1, cnt)
        if curx != 0:
            basic_dfs(curx-1, cury, cnt)
        if cury != 0:
            basic_dfs(curx, cury-1, cnt)
        visited[curx][cury] = False
    return


N, M = map(int, sys.stdin.readline().split())
smeb = []
visited =[]
for _ in range(N):
    smeb.append(list(map(int, list(sys.stdin.readline().strip()))))
    visited.append([False]*M)

basic_dfs(0, 0, 0)
print(mincnt)
'''