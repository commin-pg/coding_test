from itertools import combinations_with_replacement  # 조합
import math


def solution(n, s):
    answer = []
    # 각 원소의 합이 S가되는 수의 집합
    # 위 조건을 만족하면서 각 원소의 곱이 최대가 되는 집합
    # n : 자연수의 개수
    # s : 자연수 집합의 합
    if n > s:
        return [-1]
    ll = [i for i in range(1, 9)]
    lst = sorted([i for i in combinations_with_replacement(ll, n) if sum(i) == s], key=lambda x: max(x[0], x[1]),
                 reverse=False)
    print(lst)
    if len(lst) == 0:
        return [-1]
    return sorted(list(map(int, list(lst[0]))))


def solution2(n, s):
    if n > s:
        return [-1]
    answer = []

    p, dv = divmod(s, n)
    answer = [p] * n
    for i in range(dv):
        answer[i] += 1
    return sorted(answer)


n, s = 2, 10002321
print(solution2(n, s))
