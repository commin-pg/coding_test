def formingMagicSquare(s, ms):
    ret = 0
    for x in range(3):
        for y in range(3):
            if s[x][y] != ms[x][y]:
                ret += abs(s[x][y] - ms[x][y])
    return ret


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]
    return ret


if __name__ == '__main__':
    s = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for idx, j in enumerate(list(map(int, input().split()))):
            s[i][idx] = j

    ms = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    ms2 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    result = []
    for _ in range(4):
        ms = rotate_90(ms)
        result.append(formingMagicSquare(s, ms))
        ms2 = rotate_90(ms2)
        result.append(formingMagicSquare(s, ms2))

    print(min(result))
