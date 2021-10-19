from itertools import permutations
import math


def solution(n, k):
    G = [i for i in range(1, n + 1)]
    G2 = [i for i in permutations(G)]
    return G2[k - 1]


def solution2(n, k):
    answer = []
    G = [i for i in range(1, n + 1)]
    while n != 0:
        tmp = math.factorial(n - 1)
        idx = k // tmp
        k = k % tmp
        if k == 0:
            answer.append(G.pop(idx - 1))
        else:
            answer.append(G.pop(idx))
        n -= 1
    return answer


n, k = 3, 5
print(solution2(n, k))
