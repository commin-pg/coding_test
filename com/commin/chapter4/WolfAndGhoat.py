"""
크기가 R×C인 목장이 있고, 목장은 1×1 크기의 칸으로 나누어져 있다. 각각의 칸에는 비어있거나, 양 또는 늑대가 있다. 양은 이동하지 않고 위치를 지키고 있고, 늑대는 인접한 칸을 자유롭게 이동할 수 있다. 두 칸이 인접하다는 것은 두 칸이 변을 공유하는 경우이다.

목장에 울타리를 설치해 늑대가 양이 있는 칸으로 갈 수 없게 하려고 한다. 늑대는 울타리가 있는 칸으로는 이동할 수 없다. 울타리를 설치해보자.

입력
첫째 줄에 목장의 크기 R, C가 주어진다.

둘째 줄부터 R개의 줄에 목장의 상태가 주어진다. '.'는 빈 칸, 'S'는 양, 'W'는 늑대이다.

출력
늑대가 양이 있는 칸으로 갈 수 없게 할 수 있다면 첫째 줄에 1을 출력하고, 둘째 줄부터 R개의 줄에 목장의 상태를 출력한다. 울타리는 'D'로 출력한다. 울타리를 어떻게 설치해도 늑대가 양이 있는 칸으로 갈 수 있다면 첫째 줄에 0을 출력한다.

제한
1 ≤ R, C ≤ 500
"""

# R, C = map(int, input().split())
# dxy = {}
# isImpossible = False
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
#
# for row in range(R):
#     # print(enumerate(list(input().split())))
#     Y = {idx: y for idx, y in enumerate(list(input()))}
#     dxy[row] = Y
#
# result_str = ''
# for row in range(R):
#     for column in range(C):
#         if dxy[row][column] == '.' or dxy[row][column] == 'D':
#             continue
#
#         if dxy[row][column] == 'W':
#             # 위
#             if row - 1 >= 0 and dxy[row - 1][column] == 'S':
#                 isImpossible = True
#                 break
#             # 아래
#             elif row + 1 <= R - 1 and dxy[row + 1][column] == 'S':
#                 isImpossible = True
#                 break
#             # 좌
#             elif column - 1 >= 0 and dxy[row][column - 1] == 'S':
#                 isImpossible = True
#                 break
#             # 우
#             elif column + 1 <= C - 1 and dxy[row][column + 1] == 'S':
#                 isImpossible = True
#                 break
#             else:
#                 if row - 1 >= 0 and dxy[row - 1][column] == '.': dxy[row - 1][column] = 'D'
#                 if row + 1 <= R - 1 and dxy[row + 1][column] == '.': dxy[row + 1][column] = 'D'
#                 if column - 1 >= 0 and dxy[row][column - 1] == '.': dxy[row][column - 1] = 'D'
#                 if column + 1 <= C - 1 and dxy[row][column + 1] == '.': dxy[row][column + 1] = 'D'
#
# for r_key in dxy.keys():
#     aa = list(map(str, dxy[r_key].values()))
#     result_str += ''.join(aa) + '\n'
# if isImpossible: print(0)
# if not isImpossible: print(1)
# print(result_str)

# 남이 품

R, C = map(int, input().split())
M = [list(input()) for i in range(R)]
# print(M)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ck = False
for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for w in range(4):
                ii, jj = i + dx[w], j + dy[w]
                if ii < 0 or ii == R or jj < 0 or jj == C:
                    continue
                if M[ii][jj] == 'S':
                    ck = True
                    break

if ck:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(R):
            if M[i][j] not in 'SW':
                M[i][j] = 'D'
for i in M:
    print(''.join(i))
