# 퀸 기물을 총 n개 이고, n*n 행렬을 만든다.
# 퀸은 가로,세로,대각선 으로 움직일 수 있다.
# 같은 행(x)에 다른 퀸이 있으면 안된다. -> 한 행에 무조건 퀸은 하나 존재
# 같은 열(y)에 다른 퀸이 있으면 안된다. -> 한 열에 무조건 퀸은 하나 존재
# 같은 대각선(
def dfs(queen, n, row):
    count = 0
    if n == row:
        return 1

    for col in range(n):
        queen[row] = col

        for x in range(row):
            if queen[x] == queen[row]:
                break
            if abs(queen[x] - queen[row]) == (row - x):
                break
        else:
            count += dfs(queen, n, row + 1)
    return count


def solution(n):
    answer = 0
    queen = [0] * n

    return dfs(queen, n, 0)


n = [ 4,3, 2, 7, 12]
for i in n:
    print(solution(i))
