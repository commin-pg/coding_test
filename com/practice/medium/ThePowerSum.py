# 21:50 start 22:12 end
def dfs(X, N, num):
    v = X - num ** N
    if v < 0:
        return 0
    elif v == 0:
        return 1
    else:
        return dfs(v, N, num + 1) + dfs(X, N, num + 1)


def powerSum(X, N):
    return dfs(X, N, 1)


if __name__ == '__main__':
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N)
    print(result)
