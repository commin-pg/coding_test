"""
3
1 2 3 5
9 6 7 8
4 3 2 1

3
1 1 1 1
1 1 1 1
1 1 1 1

4
9 5 2 3
9 8 6 7
8 9 7 1
100 9 8 1
"""

# def solution(land):
#     answer = 0
#     # print(land)
#     N = len(land)
#     c = -1
#     for row in land:
#         if c != -1:
#             row[c] = (-1, c)
#             print(row)
#         choice = max(row)
#         answer += choice[0]
#         c = choice[1]
#         # print(row, answer, c)
#     return answer

import copy


def solution(land):
    answer = 0
    N = len(land)
    DP = copy.deepcopy(land)
    for i in range(N - 1):
        DP[i + 1][0] += max(DP[i][1], DP[i][2], DP[i][3])
        DP[i + 1][1] += max(DP[i][0], DP[i][2], DP[i][3])
        DP[i + 1][2] += max(DP[i][0], DP[i][1], DP[i][3])
        DP[i + 1][3] += max(DP[i][0], DP[i][1], DP[i][2])
    for i in DP:
        print(i)
    return max(DP[N-1])


N = int(input())
land = [[i for i in list(map(int, (input().split())))] for _ in range(N)]
print(solution(land))
# land = [[(i, idx) for idx, i in enumerate(list(map(int, l)))] for l in land]
# for l in land:
#     print(l)

