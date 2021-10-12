C, M = list(), list()

for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)

for i in range(100):
    idx = i % 3
    nxt = (idx + 1) % 3
    if C[nxt] >= (M[nxt] + M[idx]):
        M[nxt] = M[nxt] + M[idx]
        M[idx] = 0
    else:
        M[idx] = M[idx] - (C[nxt] - M[nxt])
        M[nxt] = C[nxt]

for i in M:
    print(i)

# 남 답

C, M = [0, 0, 0], [0, 0, 0]

for i in range(3):
    C[i], M[i] = map(int, input().split())

for i in range(100):
    idx, nxt = i % 3, (idx + 1) % 3
    M[idx], M[nxt] = max(C[nxt] + M[nxt] - M[idx], 0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)
