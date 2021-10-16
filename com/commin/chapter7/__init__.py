"""
 코딩테스트 수학 이론


"""


def era_prime(N):
    A, P = [0 for _ in range(N + 1)], []
    for i in range(2, N):
        if A[i] == 0:
            P.append(i)
        else:
            continue
        for j in range(i ** 2, N, i):
            A[j] = 1
    return P
print(era_prime(100))
