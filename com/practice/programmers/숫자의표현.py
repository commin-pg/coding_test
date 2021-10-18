# def dfs(num, N):
#     if num > N and N // 2 < num:
#         return 0
#     if num == N:
#         return 1
#     sum = num
#     ret = 0
#     for i in range(num + 1, N + 1):
#         if sum > N:
#             ret = 0
#             break
#         elif sum == N:
#             ret = 1
#             break
#         else:
#             sum += i
#     return ret + dfs(num + 1, N)
#
#
# def solution(n):
#     answer = dfs(1, n)
#     return answer

def dfs(num, n, s):
    if sum > n:
        return 0
    elif sum == n:
        return 1

    num + dfs(num + 1, n, sum)


def solution(n):
    answer = 1
    for i in range(1, n):
        if n / 2 < i and i > n:
            continue
        answer += dfs(i, n, 0)
    return answer


print(solution(int(input())))
