import sys


def basic_dfs(curx, cury, cnt):
    if smeb[curx][cury] == 0:
        visited[curx][cury] = True
        return cnt

    if not visited[curx][cury]:
        visited[curx][cury] = True
        cnt += 1
        if curx != N-1:
            cnt = basic_dfs(curx+1, cury, cnt)
        if cury != N-1:
            cnt = basic_dfs(curx, cury+1, cnt)
        if curx != 0:
            cnt = basic_dfs(curx-1, cury, cnt)
        if cury != 0:
            cnt = basic_dfs(curx, cury-1, cnt)
    return cnt


N = int(sys.stdin.readline())
smeb = []
visited =[]
for _ in range(N):
    smeb.append(list(map(int, list(sys.stdin.readline().strip()))))
    visited.append([False]*N)

housenum = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and smeb[i][j] != 0:
            temphouse = basic_dfs(i, j, 0)
            housenum.append(temphouse)

housenum.sort()

print(len(housenum))
for item in housenum:
    print(item)