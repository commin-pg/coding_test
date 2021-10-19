def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]
    return ret


print(rotate_90(rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))

