"""
Flood Fill 문제

"""
import sys

sys.setrecursionlimit(10000)  # 재귀함수의 깊이를 제한함

T = int(input())
B, ck = [], []  # 배추, 탐색완료체크

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(x, y):
    global ck
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if B[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        dfs(xx, yy)


def process():
    global B, ck
    M, N, K = map(int, input().split())  # M : 배추밭 가로길이, N : 세로길이, K : 배추가 심어진 개수
    B = [[0 for i in range(M + 2)] for _ in range(N + 2)]  # 바깥에 존재하는 가상의 영역을 추가한다.
    ck = [[0 for i in range(M + 2)] for _ in range(N + 2)]  # 바깥에 존재하는 가상의 영역을 추가한다.
    for _ in range(K):
        X, Y = map(int, input().split())  # X,Y 배추의 위치
        B[Y + 1][X + 1] = 1  # 가상의 영역을 내가 임의로 추가했으니, 입력값에 +1을 하여서 초기화 해준다.

    ans = 0
    # DFS 의 핵심은 전체탐색을 하되, 탐색한부분은 다시 탐색하지 않는것이 핵심이다.
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if B[i][j] == 0 or ck[i][j]:  # 이미 탐색했으면 1이므로 continue
                continue
            dfs(i, j)
            ans += 1
    print(ans)


for _ in range(T):
    process()
