# n : n X n 체스판
# k : 장애물 수
# (r_q,c_q) : 퀸의 위치
# obstacles : 장애물 위치 리스트

dx = [['E', 0], ['N', -1], ['W', 0], ['S', 1], ['NE', -1], ["ES", 1], ["SW", 1], ["WN", -1]]  # 동 남 서 북 오위,오아,왼아,왼위
dy = [['E', 1], ['N', 0], ['W', -1], ['S', 0], ['NE', 1], ["ES", 1], ["SW", -1], ["WN", -1]]
dxy = [True, True, True, True, True, True, True, True]


def queensAttack(n, k, r_q, c_q, obstacles):
    x = r_q - 1
    y = c_q - 1
    ret = 0

    G = [[0 for _ in range(n)] for _ in range(n)]  # queen : 2 , possible : 1 , impossible : 3
    ck = [[False for _ in range(n)] for _ in range(n)]

    G[x][y] = 2

    for ob in obstacles:
        G[ob[0] - 1][ob[1] - 1] = 3
        ck[ob[0] - 1][ob[1] - 1] = False

    while True:
        for w in range(8):
            if not dxy[w]:
                continue
            xx, yy = x + dx[w][1], y + dy[w][1]
            if xx >= n or xx < 0 or yy >= n or yy < 0 or G[xx][yy] == 3 or G[xx][yy] != 0:
                dxy[w] = False
                continue

            ret += 1
            G[xx][yy] = 1
            if dx[w][0] == 'S' or dx[w][0] == 'ES' or dx[w][0] == 'SW':
                dx[w][1] += 1

            if dy[w][0] == 'E' or dy[w][0] == 'NE' or dy[w][0] == 'ES':
                dy[w][1] += 1

            if dx[w][0] == 'N' or dx[w][0] == 'NE' or dx[w][0] == 'WN':
                dx[w][1] -= 1

            if dy[w][0] == 'W' or dy[w][0] == 'SW' or dy[w][0] == 'WN':
                dy[w][1] -= 1

        cnt = dxy.count(True)
        if cnt == 0:
            break

    return ret


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
