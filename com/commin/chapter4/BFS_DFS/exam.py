"""
010
111
010

1을 모두 +로 변경

"""

N, M = map(int, input().split())  # N : 행 , M : 열
G = [list(input()) for _ in range(M)]  # G : 2차원 배열
ck = [[False for _ in range(M)] for _ in range(M)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(x, y):
    global G, ck  # 글로벌 변수 선언
    G[x][y] = '+'
    ck[x][y] = True
    for w in range(4):
        xx, yy = x + dx[w], y + dy[w]
        if xx >= N or xx < 0 or yy >= M or yy < 0 or ck[xx][yy] or G[xx][yy] == '0':
            continue
        dfs(xx, yy)


for x in range(N):  # 행 루프
    for y in range(M):  # 열 루프
        if ck[x][y] or G[x][y] == '0':  # 루프 조건
            continue
        dfs(x, y)  # dfs

for i in G:
    print(''.join(i))
